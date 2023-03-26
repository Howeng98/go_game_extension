import cv2
import os

cam = cv2.VideoCapture("E:\python_test\GO\go_game_extension-main (2)\go_game_extension-main\samples\GO.MOV")

try:
    if not os.path.exists('E:\python_test\GO\go_game_extension-main (2)\go_game_extension-main/data'):
        os.makedirs('E:\python_test\GO\go_game_extension-main (2)\go_game_extension-main/data')
        
except OSError:
    print("Error: Creating Directory for Data is fail")
    
currentframe = 0

prev_frame = None

while(True):
    ret, frame = cam.read()
        
    if ret:
        prev_frame = frame
        print("success")
        if currentframe % 80 == 0:
            name = 'E:\python_test\GO\go_game_extension-main (2)\go_game_extension-main./data/frame' + str(currentframe) + '.jpg'
            cv2.imwrite(name, frame)
            
        currentframe +=1
        
    else:
        print("last")
        
        name = 'E:\python_test\GO\go_game_extension-main (2)\go_game_extension-main/data/last.jpg'
        print(prev_frame)
        cv2.imwrite(name, prev_frame)
        break


cam.release()