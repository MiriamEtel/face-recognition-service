
# Face Recognition Service

The **Face Recognition Service** is a state-of-the-art web application built with Flask, providing a robust and efficient platform for face recognition. This service uses advanced machine learning techniques to identify individuals by comparing uploaded images against a predefined database of known faces. The system determines whether the uploaded image matches an existing record, and if so, it provides the name associated with the recognized individual.

Additionally, the service offers the capability to dynamically expand the database of recognized individuals by uploading new images and associating them with unique names. This makes the system adaptable and scalable for various real-world use cases such as:
- Employee attendance systems.
- Secure access control.
- Personalized user experiences.

By leveraging powerful libraries like `face_recognition`, `OpenCV`, and `Pillow`, the service ensures high accuracy and performance, even with large datasets. Its simple API design and extensibility make it an ideal solution for organizations seeking a reliable face recognition tool.

## Features
- **Face Matching**: Compares uploaded images against a known database and identifies matches.
- **Dynamic Database Expansion**: Allows users to add new face images with custom names to the recognition database.
- **High Accuracy**: Utilizes advanced encoding and matching algorithms for precise identification.
- **Cross-Platform Compatibility**: Built with Python and Flask, ensuring seamless deployment across diverse environments.

## Requirements
- Python 3.10 or above
- Flask
- Flask-CORS
- OpenCV
- face_recognition
- Pillow
- numpy

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/face-recognition-service.git
   cd face-recognition-service
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Add your known face images to the project directory with filenames (e.g., `Miri.jpg`, `Ayala.jpg`, `Shira.jpg`).

2. Run the application:
   ```bash
   python app.py
   ```

3. Access the application via:
   - **POST /upload**: Upload an image to compare against known faces.
   - **POST /upload-custom**: Upload an image with a custom name to add to the database.

### Endpoints
#### 1. `/upload` (POST)
Uploads an image to compare it with known faces.

- **Request**:
  - `image`: The face image to compare.
- **Response**:
  - `match`: `true` if a match is found, `false` otherwise.
  - `person`: The name of the matched person or `null`.

#### 2. `/upload-custom` (POST)
Uploads a new image with a custom name and adds it to the known faces database.

- **Request**:
  - `image`: The face image to upload.
  - `name`: The name associated with the face.
- **Response**:
  - `message`: Success message.

## Example
### Uploading and Matching an Image
Using `curl`:
```bash
curl -X POST -F "image=@unknown.jpg" http://127.0.0.1:5000/upload
```

### Adding a Custom Image
Using `curl`:
```bash
curl -X POST -F "image=@new_face.jpg" -F "name=John" http://127.0.0.1:5000/upload-custom
```

## Notes
- Ensure the images used for encoding are clear and well-lit for optimal recognition accuracy.
- The service compares faces based on encodings and may have limitations with low-quality images or occlusions.
#
