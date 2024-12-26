from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import face_recognition
from PIL import Image
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Function to load images and encode faces
def load_and_encode_images(image_paths):
    encodings = []
    for image_path in image_paths:
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        encodings.append(encoding)
    return encodings

# List of images to check
image_paths = ["Miri.jpg", "Ayala.jpg", "Shira.jpg"]
known_face_encodings = load_and_encode_images(image_paths)

# Function to save uploaded image with custom name and update the encodings
def save_uploaded_image(file, name):
    filename = f"{name}.jpg"  # Save the image with the chosen name
    file.save(filename)  # Save the image in the current directory

    # Add the image name to the image_paths array
    image_paths.append(filename)

    # Load and encode the new image
    new_image = face_recognition.load_image_file(filename)
    new_encoding = face_recognition.face_encodings(new_image)[0]
    known_face_encodings.append(new_encoding)

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    file.save('unknown.jpg')

    # Load the captured unknown image
    unknown_picture = face_recognition.load_image_file("unknown.jpg")

    # Convert the image to RGB format using PIL
    img_pil = Image.fromarray(unknown_picture)
    rgb_img = img_pil.convert("RGB")

    # Convert the image to a numpy array and encode the captured image
    unknown_face_encoding = face_recognition.face_encodings(np.array(rgb_img))[0]

    # Compare the captured face encoding with the known faces
    results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)

    if True in results:
        first_match_index = results.index(True)
        return jsonify({"match": True, "person": image_paths[first_match_index]})
    else:
        return jsonify({"match": False, "person": None})

@app.route('/upload-custom', methods=['POST'])
def upload_custom_image():
    file = request.files['image']
    name = request.form['name']

    save_uploaded_image(file, name)

    return jsonify({"message": "Image uploaded and added to image_paths successfully"})

if __name__ == '__main__':
    app.run(debug=True)
