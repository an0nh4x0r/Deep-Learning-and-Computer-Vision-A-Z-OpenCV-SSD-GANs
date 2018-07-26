# Face Recognition

# Importing the libraries
import cv2

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

