import cv2 as cv
from time import sleep

# initialize the camera
def take_picture():
    cam_port = 0

    cam = cv.VideoCapture(cam_port)
    result, image = cam.read()
    if result:
        print('Image taken and saved')
        image_name = 'current_image.png'
        cv.imwrite(str('./rekognition/' + image_name), image)
    else:
        print("ERROR! No image detected.") 

take_picture()