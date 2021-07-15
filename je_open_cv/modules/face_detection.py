import cv2

'''
OpenCV comes with a trainer as well as detector. 
If you want to train your own classifier for any object like car, planes etc. 
you can use OpenCV to create one. 
Its full details are given here: Cascade Classifier Training.

OpenCV already contains many pre-trained classifiers for face, eyes, smile etc. 
Those XML files are stored in opencv/data/haarcascades/ folder. 
Let’s create face and eye detector with OpenCV.
'''


def detection(image):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    return image
