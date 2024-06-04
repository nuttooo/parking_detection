# Parking Detection System

This project uses Pixy2, Roboflow, and Firestore Database to detect car parking, capture license plate images, and store the data in a Firestore Database on Raspberry Pi.

## Features

- Detect car parking using Pixy2
- Capture license plate images
- Analyze images with Roboflow
- Store license plate data in Firestore Database
- Update parking slot status (occupied/vacant)

## Requirements

- Raspberry Pi
- Pixy2 Camera
- Python 3.x
- Virtual Environment (optional but recommended)

## Installation

### 1. Set up Raspberry Pi

Update and upgrade your Raspberry Pi:

```sh
sudo apt update
sudo apt upgrade
sudo apt install python3-pip python3-opencv libopencv-dev
```
### 2. Clone the Repository
```sh
git clone https://github.com/YOUR_USERNAME/parking_detection.git
cd parking_detection
```

###  3. Set up Virtual Environment
Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```

###  4. Install Required Libraries
Install the required libraries:
```sh
pip install -r requirements.txt
```
###  5. Install Pixy2 Python API
Clone the Pixy2 repository and install the Pixy2 Python API:
```sh
git clone https://github.com/charmedlabs/pixy2.git
cd pixy2/scripts
python3 get-pixy-python-api.sh
cd ../..
```

### 6. Set Up Firebase
1. Go to [Firebase Console](https://firebase.google.com) and create a new project or select an existing project.
2. Click on "Firestore Database" and create a database.
3. Go to "Project settings" and select "Service accounts".
4. Click on "Generate new private key" to download the JSON file with your Firebase credentials.
5. Move the downloaded JSON file to the project directory and rename it to `firebase_credentials.json.`

###  7. Set Up Environment Variables
Create a `.env` file in the project directory and add the following content:
```sh
# Roboflow API Key
ROBOFLOW_API_KEY=your_roboflow_api_key

# Path to Firebase service account credentials JSON file
FIREBASE_CREDENTIALS_PATH=firebase_credentials.json

# Firebase Database URL
FIREBASE_DATABASE_URL=https://your-database-name.firebaseio.com

# Google Cloud Storage bucket name
GCS_BUCKET_NAME=your_bucket_name
```

## Usage
1. Activate the virtual environment:
```sh
source venv/bin/activate
```

2. Run the main script:
```sh
python main.py
```

## Project Structure
```bash
parking_detection/
│
├── venv/                        # virtual environment
│
├── .env                         # environment variables
│
├── firebase_credentials.json    # Firebase credentials
│
├── main.py                      # main script
│
├── requirements.txt             # list of required libraries
└── pixy2/                       # Pixy2 Python API from GitHub
```

## Contributing
Feel free to submit issues or pull requests if you find any bugs or have feature requests.

## License
This project is licensed under the MIT License.