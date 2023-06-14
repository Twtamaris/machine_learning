# this is spectacles in Video mode
import cv2

# Load the overlay image of the spectacles
spectacles_image = cv2.imread('spectacle.jpg')

# Create a VideoCapture object to capture video from the default camera
video_capture = cv2.VideoCapture(0)

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Read the video frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

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
                frame[y_offset + i, x_offset + j] = resized_spectacles[i, j, 0:3]

    # Display the resulting frame
    cv2.imshow('Spectacles on Face', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
video_capture.release()
cv2.destroyAllWindows()
