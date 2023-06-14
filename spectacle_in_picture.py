# This is spectacle in picture mode
import cv2
import numpy as np

# Load the input image and the overlay image of the spectacles
face_image = cv2.imread('face.jpg')
spectacles_image = cv2.imread('spectacles.png')

# Detect faces in the image using a pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Iterate over detected faces
for (x, y, w, h) in faces:
    # Resize the spectacles image to fit the face
    resized_spectacles = cv2.resize(spectacles_image, (w, int(h/2)))

    # Calculate the position to overlay the spectacles on the face
    x_offset = x
    y_offset = int(y + h/3)

    # Overlay the spectacles on the face region
    for i in range(resized_spectacles.shape[0]):
        for j in range(resized_spectacles.shape[1]):
            face_image[y_offset + i, x_offset + j] = resized_spectacles[i, j, 0:3]

# Display the result
cv2.imshow('Spectacles on Face', face_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
