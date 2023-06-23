import os
import re
import cv2
import matplotlib.pyplot as plt
import numpy as np

from glob import glob
from tqdm import tqdm
from PIL import Image

'''
# hyperparameters
'''
exit_black_array = []
exit_white_array = []
White = []
Black = []
global_array = [[[0 for col in range(1)] for col in range(19)] for row in range(19)]

radius =25
thinkness = -1

board_ratio = 56

fontFace = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 1.5
number_thinkness = 3
space_coordinate = 10
lineType = cv2.LINE_AA



def reduce_highlights(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    ret, thresh = cv2.threshold(img_gray, 200, 255, 0)  
    contours, hierarchy  = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_zero = np.zeros(img.shape, dtype=np.uint8) 
    
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour) 
        img_zero[y:y+h, x:x+w] = 0 
        mask = img_zero     

    result = cv2.illuminationChange(img, mask, alpha=0.2, beta=0.4) 
        
    return result


def generate_output(array, counter):
    
    img = cv2.imread('./samples/board.png')
    
    white_sequence_number = 2
    black_sequence_number = 1

    total_blackNum = 0
    total_whiteNum = 0

    my_dict = {}
    #center_coordinate = (548, 548)
    #left_top_coordinate = (44, 45)
    Black_board_coordinate = []
    White_board_coordinate = []
   

    for i in range(len(array)): #create dic to store value
        for j in range(len(array[i])):
        
            my_dict[(i, j)] = array[i][j] #0/1/2

            if array[i][j] != 0:
                # print("array[i][j] != 0")
                # print("global_len", len(global_array[i][j]))

                if len(global_array[i][j]) == 1:
                    # print("global len == 1")
                    counter = counter + 1
                    # print("counter: ", counter)

                    global_array[i][j].append((array[i][j], counter))

                else:
                    #print(global_array[i][j][-1][0])
                    if global_array[i][j][-1][0] != array[i][j]:
                        counter = counter + 1
                        global_array[i][j].append((array[i][j], counter))

    for key, value in my_dict.items(): #checking 0 / 1 / 2
        if value == 1:
            # counter += 1
            #print("value == 1")
            if key not in exit_black_array:
                #if key not in exit_white_array:
                Black.append(key)
                exit_black_array.append(key)
                #else:
                    #eaten_peice.append()
            #print("added")
            #print("exit: ", exit_black_array)

        elif value == 2:
            if key not in exit_black_array:
                White.append(key)
                exit_black_array.append(key)
            #print("added")
            #print("exit: ", exit_black_array)

    for item in Black:
        if item not in exit_white_array:
            exit_white_array.append(item)

    #print("Black -sorted", Black)
    #print("Black_array: ", Black) # return the location of black peices
    #print("White_array: ", White) # return the location of white peices
    #=========================== Checking eaten peices =======================
        #if 
    #==========================================================================
    #changing the location into actual board coordinate
    for i in range(len(Black)):
        Black_board_coordinate.append((int(44+board_ratio * Black[i][1]) , int(44+board_ratio * Black[i][0])))
        #print("board coordinate: ", Black_board_coordinate)
        #img = cv2.circle(img, Black_board_coordinate, radius, (0, 0, 0), thinkness)
        total_blackNum += 1

    for i in range(len(White)):
        White_board_coordinate.append((int(44+board_ratio * White[i][1]) , int(44+board_ratio * White[i][0])))
        #img = cv2.circle(img, White_board_coordinate, radius, (255, 255, 255), thinkness)
        total_whiteNum += 1

    # print("黑棋總數量: ", total_blackNum)
    # print("白棋總數量: ", total_whiteNum)

    #===========================================================================

    #========== Draw ===============
    for i in range(len(Black_board_coordinate)): #draw black

        #print(Black_board_coordinate[i][0])
        img = cv2.circle(img, (Black_board_coordinate[i][0], Black_board_coordinate[i][1]), radius, (0, 0, 0), thinkness) #center
        
    for i in range(len(White_board_coordinate)): #draw white

        img = cv2.circle(img, (White_board_coordinate[i][0], White_board_coordinate[i][1]), radius, (250, 250, 250), thinkness) #center
        img = cv2.circle(img, White_board_coordinate[i], radius, (0, 0, 0), 2)

    for i in range(len(Black_board_coordinate)): #black number
        coordinate = (Black_board_coordinate[i][0]-14 , Black_board_coordinate[i][1] + 15),
        fontScale = 1.4
        if black_sequence_number >= 10:
            fontScale = 1.1
            coordinate = (Black_board_coordinate[i][0]-24 , Black_board_coordinate[i][1] + 12),
        img = cv2.putText(img, str(black_sequence_number), coordinate[0], fontFace, fontScale, (250,250,250), number_thinkness, lineType)
        black_sequence_number += 2

    for i in range(len(White_board_coordinate)): #white number
        coordinate = (White_board_coordinate[i][0]-14 , White_board_coordinate[i][1] + 15),
        fontScale = 1.4
        if white_sequence_number >= 10:
            fontScale = 1.1
            coordinate = (White_board_coordinate[i][0]-24 , White_board_coordinate[i][1] + 12),
        img = cv2.putText(img, str(white_sequence_number), coordinate[0], fontFace, fontScale, (0,0,0), number_thinkness, lineType)
        white_sequence_number += 2
    #=================================    
    cv2.imwrite('output.png', img)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img)
    # plt.show()  

    return counter



def main():    
    counter = 0
    
    DATA_DIR = './pure_data'
    IMG_PATHS = glob(os.path.join(DATA_DIR, '*.jpg'))
    
    # IMG_PATHS = ['./data/frame30.jpg', './data/frame164.jpg', './data/frame243.jpg', './data/frame250.jpg', './data/frame392.jpg', './data/frame555.jpg', './data/frame687.jpg', './data/frame821.jpg', './data/frame1000.jpg']
    
    IMG_PATHS.sort(key=lambda f: int(re.sub('\D', '', f)))
    
    mesh = np.linspace(0, 19, 19, dtype=int)
    rows, cols = np.meshgrid(mesh, mesh)
    BOARD = np.zeros_like(rows, dtype=np.uint8)
    
    prev_bundle = None
    bundle_result = list()
    valid_bundle_interval = 10
    
    for IMG_PATH in tqdm(IMG_PATHS):
        
        root_img = cv2.imread(IMG_PATH)
        # root_img = cv2.cvtColor(root_img, cv2.COLOR_BGR2RGB)
        img = reduce_highlights(root_img)

        gray = cv2.cvtColor(root_img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (9,9), 3)
        gray = cv2.Canny(gray, 70, 70)
        
        img_w_h = 1100
        pts1 = np.float32([(520,64),(587,1034),(1592,52),(1561,987)])
        pts2 = np.float32([(0,0), (0,img_w_h), (img_w_h,10), (img_w_h,img_w_h)])
        
        
        m = cv2.getPerspectiveTransform(pts1, pts2) 
        fixed_rgb_img = cv2.warpPerspective(img, m, (img_w_h, img_w_h))
        fixed_gray_img = cv2.warpPerspective(gray, m, (img_w_h, img_w_h))

        circle1 = cv2.HoughCircles(fixed_gray_img, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=13, minRadius=5, maxRadius=35)
        circles = circle1[0, :, :]
        circles = np.uint16(np.around(circles))
        
        # prune strange circles by checking RGB values
        pure_circles = []
        
        for idx, i in enumerate(circles):
            r, g, b = fixed_rgb_img[i[1], i[0], :]
            if r < 80 and g < 80 and b < 80:
                pure_circles.append((i[0],i[1],i[2]))
            elif r > 210 and g > 210 and b > 210:
                pure_circles.append((i[0],i[1],i[2]))
        
        # draw circles
        pure_circles = np.array(pure_circles)
        for i in pure_circles:
            cv2.circle(fixed_rgb_img, (i[0], i[1]), i[2], (255,0,0), 5)
        
        mesh = np.linspace(0, img_w_h, 19, dtype=int)
        rows, cols = np.meshgrid(mesh, mesh)
        board_condition = np.zeros_like(rows, dtype=np.uint8)
        im_hsv = cv2.cvtColor(fixed_rgb_img, cv2.COLOR_RGB2HSV_FULL)

        white_count, black_count = 0, 0
        
        for circle in pure_circles:    
            row = int(round((circle[1]-10)/58))
            col = int(round((circle[0]-10)/58))
        
            # size = 3
            # hsv_ = im_hsv[cols[row,col]-size:cols[row,col]+size, rows[row,col]-size:rows[row,col]+size]
            # s = np.mean(hsv_[:,:,1])
            # v = np.mean(hsv_[:,:,2])
        
            # check RGB values
            r, g, b = fixed_rgb_img[circle[1], circle[0], :]
            # print(row, col)
            if r < 100 and g < 100 and b < 100:
                board_condition[row, col] = 1  #黑棋
                black_count += 1

            elif r > 200 and g > 200 and b > 200:
                board_condition[row, col] = 2  #白棋
                white_count += 1


        # GO board prediction
        tqdm.write("IMG_NAMES: {} | 白棋：{} |  黑棋：{}\n".format(os.path.basename(IMG_PATH), white_count, black_count))
        
        
        # Calibrate pieces prediction
        current_bundle = int(os.path.basename(IMG_PATH).replace("frame", "").replace(".jpg", ""))
        if prev_bundle is None and len(bundle_result) == 0:                        
            bundle_result.append((IMG_PATH, white_count, black_count, board_condition)) 
            prev_bundle = current_bundle           
        else:            
            if current_bundle - prev_bundle > valid_bundle_interval: #check whether is consecutive frames of bundle
                bundle_result.append((IMG_PATH, white_count, black_count, board_condition))
            else: # next of bundle                
                pass
            prev_bundle = current_bundle
        # print(board_condition)        
    
    # print(bundle_result)
    
    for result in bundle_result:
        board_condition = result[3] # [IMG_PATH, white_count, black_count, board_condition]
        counter = generate_output(array=board_condition, counter=counter)

if __name__ == '__main__':
    main()