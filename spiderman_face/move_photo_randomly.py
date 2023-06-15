import cv2
import numpy as np
import random
import os 

images_name = os.listdir('spiderman_face/images')

images = []
for i in images_name:
    images.append(cv2.imread('spiderman_face/images/'+i))
# Open the video capture
video_capture = cv2.VideoCapture(0)

# Get the frame dimensions
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Resize the images to (30, 50)
resized_images = [cv2.resize(image, (30, 50)) for image in images]

while True:
    # Read the frame from the video capture
    ret, frame = video_capture.read()


    # Overlay the images at random positions
    for image in resized_images:
        # Randomly select x, y position for the image
        x = random.randint(0, frame_width - image.shape[1])
        y = random.randint(0, frame_height - image.shape[0])

        # frame ma china spiderman ko portion khaligareko so that tyo
        # spiderman ko image ata basna sakos.
        roi = frame[y:y + image.shape[0], x:x + image.shape[1]]

        # Add the image to the ROI
        # roi pachadi ko 0.5 le sautration dinxa image ko lagi
        # image pachi ko 1 le ni color kai chij dinxa 0 bhayo bhaney purai black
        # 1 bhayo bhaney purai clear image
        blended = cv2.addWeighted(roi, 0, image, 1, 0)
        # frame ko ati portion ma image add gareko
        # Add the blended ROI back to the frame
        frame[y:y + image.shape[0], x:x + image.shape[1]] = blended

    # Display the frame
    cv2.imshow('Camera', frame)

    # Check for the "q" key press
    key = cv2.waitKey(100)
    if key == ord('q'):
        break

# Release the video capture and close the window
video_capture.release()
cv2.destroyAllWindows()


# frame[y:y + image.shape[0], x:x + image.shape[1]].shape gives images
# u can see using maplotlib.
# plt.imshow(frame[y:y + image.shape[0], x:x + image.shape[1]])