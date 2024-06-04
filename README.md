# Parking Detection

This project uses Pixy2, Roboflow, and Firebase to detect car parking, capture license plate images, and store the data in a Firebase database.

## Features
- Detect car parking using Pixy2
- Capture license plate images
- Analyze images with Roboflow
- Store license plate data in Firebase
- Update parking slot status (occupied/vacant)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/nuttooo/parking_detection.git
   cd parking_detection
   
2. Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   
3. Install the required packages:
   ```sh
   pip install pixy2 opencv-python roboflow firebase-admin pytesseract python-dotenv google-cloud-storage

4. Set up your environment variables:
   - Create a file named `.env` in the root directory of your project.
   - Add the following content to the `.env` file:
   ```env
   # Roboflow API Key
   ROBOFLOW_API_KEY=your_roboflow_api_key
  
   # Path to Firebase service account credentials JSON file
   FIREBASE_CREDENTIALS_PATH=path/to/your/firebase/credentials.json
  
   # Firebase Database URL
   FIREBASE_DATABASE_URL=https://your-database-name.firebaseio.com
  
   # Google Cloud Storage bucket name
   GCS_BUCKET_NAME=your_bucket_name
   
5. Place your Firebase credentials file in the root directory.

## Usage

1. Activate the virtual environment:
   ```sh
   source venv/bin/activate
   
2. Run the main script:
   ```sh
   python main.py

## Project Structure
   ```bash
   parking_detection/
  │
  ├── venv/                        # virtual environment
  │
  ├── .env                         # environment variables
  │
  ├── your_firebase_credentials.json  # Firebase credentials
  │
  └── main.py                      # main script
  ```

## Contributing
Feel free to submit issues or pull requests if you find any bugs or have feature requests.

## License
This project is licensed under the MIT License.

