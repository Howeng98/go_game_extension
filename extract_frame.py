import cv2
import os

cam = cv2.VideoCapture("./samples/GO.mp4")

try:
    if not os.path.exists('data'):
        os.makedirs('data')
        
except OSError:
    print("Error: Creating Directory for Data is fail")
    
currentframe = 0

while(True):
    ret, frame = cam.read()
    
    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'
        cv2.imwrite(name, frame)
        currentframe +=1
        
    else:
        break
    
cam.release()