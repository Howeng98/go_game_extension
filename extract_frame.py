import cv2
import os


ROOT_PATH = 'GO_2_frames'

try:
    if not os.path.exists('GO_2_frames'):
        os.makedirs('GO_2_frames')
except OSError:
    print("Error: Creating Directory for Data is fail")


cam = cv2.VideoCapture("./GO_2.mp4")
currentframe = 0
prev_frame = None

while(True):
    ret, frame = cam.read()
        
    if ret:
        prev_frame = frame        
        if currentframe % 10 == 0:
            name = 'GO_2_frames/frame_' + str(currentframe) + '.jpg'
            cv2.imwrite(name, frame)
            
        currentframe +=1    
    else:        
        break

cam.release()