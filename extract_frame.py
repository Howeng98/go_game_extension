import cv2
import os
import time

cam = cv2.VideoCapture("./samples/GO.MOV")

try:
    if not os.path.exists('data2'):
        os.makedirs('data2')
        
except OSError:
    print("Error: Creating Directory for Data is fail")
    
currentframe = 0
start_time = time.time()
frames = []
DELAY_SECONDS = 3

while(True):
    ret, frame = cam.read()

    if ret:
        print("cc")
        if time.time() - start_time > DELAY_SECONDS:
            print("Checks")
            # cv2.imshow("frame", frames.pop(0))
            name = './data2/frame' + str(currentframe) + '.jpg'
            cv2.imwrite(name, frames.pop(0))
            currentframe += 1
        
        
        
        # name = './data2/frame' + str(currentframe) + '.jpg'
        # cv2.imwrite(name, frame)
        # currentframe +=1
        
    else:
        break
    
cam.release()







# while True:

#     ret, frame = cap.read()
#     frames.append(frame)

#     if time.time() - start_time > DELAY_SECONDS:
#         cv2.imshow("frame", frames.pop(0))

#     key = cv2.waitKey(1)
#     if key == 27:
#         break