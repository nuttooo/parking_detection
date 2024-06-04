import os
import time
import threading
import cv2
import numpy as np
from dotenv import load_dotenv
from roboflow import Roboflow
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
import pixy

# Load environment variables
load_dotenv()

# Initialize Pixy2 camera
pixy.init()
pixy.change_prog("color_connected_components")

# Initialize Firestore
cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS_PATH"))
firebase_admin.initialize_app(cred)
db = firestore.Client()

# Initialize Roboflow
rf = Roboflow(api_key=os.getenv("ROBOFLOW_API_KEY"))
project = rf.workspace().project("MODEL_ENDPOINT")
model = project.version("VERSION").model

# Function to upload image to Google Cloud Storage (if needed)
def upload_to_gcs(file_path, bucket_name, destination_blob_name):
    from google.cloud import storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(file_path)
    print(f'File {file_path} uploaded to {destination_blob_name}.')

# Function to capture image and process it with Roboflow
def capture_and_process_image(slot_id):
    # Capture an image from Pixy2
    pixy.get_raw_frame()
    frame = pixy.raw_frame

    # Convert the raw frame to an OpenCV image
    height, width = frame.height, frame.width
    image = np.frombuffer(frame.raw_frame, dtype=np.uint8).reshape((height, width, 3))

    # Save the captured image to a file
    image_path = "captured_image.jpg"
    cv2.imwrite(image_path, image)

    # Infer on the captured image using Roboflow
    prediction = model.predict(image_path, confidence=40, overlap=30).json()
    print(prediction)

    # Extract license plate text from the prediction
    # (Assuming that the prediction contains the text)
    license_plate_text = prediction['predictions'][0]['label']
    print(f'License Plate: {license_plate_text}')

    # Save to Firestore
    doc_ref = db.collection('parking_lots').document(slot_id)
    doc_ref.set({
        'status': 'occupied',
        'license_plate': license_plate_text
    })

    # Upload image to Google Cloud Storage (if needed)
    gcs_path = "path/in/gcs/captured_image.jpg"
    upload_to_gcs(image_path, os.getenv("GCS_BUCKET_NAME"), gcs_path)

# Function to wait and capture image after 30 seconds
def wait_and_capture(slot_id):
    time.sleep(30)
    capture_and_process_image(slot_id)

# Function to update parking slot status to vacant
def set_slot_vacant(slot_id):
    doc_ref = db.collection('parking_lots').document(slot_id)
    doc_ref.set({
        'status': 'vacant',
        'license_plate': ''
    })

# Main loop to detect car parking
while True:
    blocks = pixy.ccc_get_blocks()
    count = len(blocks)

    if count > 0:
        for i in range(count):
            block = blocks[i]
            print(f'Block {i}: Signature {block.signature}, X {block.x}, Y {block.y}, Width {block.width}, Height {block.height}')
            slot_id = f'slot_{block.signature}'  # Assuming each block signature represents a unique slot
            threading.Thread(target=wait_and_capture, args=(slot_id,)).start()
    else:
        # Assuming no blocks mean all slots are vacant, adjust logic as per actual requirements
        for i in range(1, 10):  # Assuming 10 slots for example
            slot_id = f'slot_{i}'
            set_slot_vacant(slot_id)

    time.sleep(0.1)
