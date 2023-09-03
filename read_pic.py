import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from fpdf import FPDF

# counter = 0 
def output(array, counter):
    
    img = cv2.imread('./samples/Board.png')
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #outside_center_coordinates = (750,750) #44
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
                #print("array[i][j] != 0")
                #print("global_len: ", len(global_array[i][j]))

                if len(global_array[i][j]) == 1:
                    #print("global len == 1")
                    counter = counter + 1
                    #print("counter: ", counter)

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

    #print("黑棋總數量: ", total_blackNum)
    #print("白棋總數量: ", total_whiteNum)

#===========================================================================

#========== Draw ===============    
    for i in range(len(Black_board_coordinate)): #draw black

        #print(Black_board_coordinate[i][0])
        img = cv2.circle(img, (Black_board_coordinate[i][0], Black_board_coordinate[i][1]), radius, (0, 0, 0), thinkness) #center
        
    for i in range(len(White_board_coordinate)): #draw white

        img = cv2.circle(img, (White_board_coordinate[i][0], White_board_coordinate[i][1]), radius, (250, 250, 250), thinkness) #center
        img = cv2.circle(img, White_board_coordinate[i], radius, (0, 0, 0), 2)


    for i in range(len(White_board_coordinate)): #white number
            if global_array[White[i][0]][White[i][1]][1][1] < 10:
                #print(counter, "if statement")
                coordinate = (White_board_coordinate[i][0]-14 , White_board_coordinate[i][1] + 15),
                fontScale = 1.4
                img = cv2.putText(img, str(global_array[White[i][0]][White[i][1]][1][1]), coordinate[0], fontFace, fontScale, (0,0,0), number_thinkness, lineType)
            else:
                #print(counter, "else statement")
                fontScale = 1.1
                coordinate = (White_board_coordinate[i][0]-24 , White_board_coordinate[i][1] + 12),
                img = cv2.putText(img, str(global_array[White[i][0]][White[i][1]][1][1]), coordinate[0], fontFace, fontScale, (0,0,0), number_thinkness, lineType)
        #white_sequence_number += 2


    for i in range(len(Black_board_coordinate)): #black number
        if global_array[Black[i][0]][Black[i][1]][1][1] < 10:
            coordinate = (Black_board_coordinate[i][0]-14 , Black_board_coordinate[i][1] + 15),
            fontScale = 1.4
        #print(Black_board_coordinate[i])
        else:
            fontScale = 1.1
            coordinate = (Black_board_coordinate[i][0]-24 , Black_board_coordinate[i][1] + 12),
        img = cv2.putText(img, str(global_array[Black[i][0]][Black[i][1]][1][1]), coordinate[0], fontFace, fontScale, (250,250,250), number_thinkness, lineType)
        #counter += 2

    



    # for i in range(counter):
    #     if counter < 10:
    #         fontScale = 14.
    #         W_coordinate = (White_board_coordinate[i][0]-14 , White_board_coordinate[i][1] + 15)
    #         B_coordinate = (Black_board_coordinate[i][0]-14 , Black_board_coordinate[i][1] + 15)

    #         print(W_coordinate)
    #         print(B_coordinate)
    #     else:
    #         fontScale = 1.1
    #         W_coordinate = (White_board_coordinate[i][0]-24 , White_board_coordinate[i][1] + 12)
    #         B_coordinate = (Black_board_coordinate[i][0]-24 , Black_board_coordinate[i][1] + 12)

    #         print(W_coordinate)
    #         print(B_coordinate)
            
    #     if counter %2 != 0: #black
    #         img = cv2.putText(img, str(global_array[Black[i][0]][Black[i][1]][1][1]), B_coordinate[0], fontFace, fontScale, (250,250,250), number_thinkness, lineType)
    #     else: #white
    #         img = cv2.putText(img, str(global_array[White[i][0]][White[i][1]][1][1]), W_coordinate[0], fontFace, fontScale, (0,0,0), number_thinkness, lineType)


#=================================
    cv2.imwrite('output.png', img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

 
 
    plt.show()  

    return counter



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

counter = 0
array = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]
# counter = output(array, counter)

# array[15][16] = 1 #1
# counter = output(array,counter)

# array[3][4] = 2 #2
# counter = output(array,counter)

# array[2][4] = 1 #3
# counter = output(array,counter)

# array[15][15] = 2 #4
# counter = output(array,counter)

# array[3][5] = 1 #5
# counter = output(array,counter)

# array[16][16] = 2 #6
# counter = output(array,counter)

# array[4][4] = 1 #7
# counter = output(array,counter)

# array[17][17] = 2 #8
# counter = output(array,counter)

# array[12][4] = 1 #9
# counter = output(array,counter)

# # array[18][18] = 2
# # counter = output(array,counter)

# array[3][3] = 2 #10
# counter = output(array,counter)

# array[3][3] = 1 #11
# counter = output(array,counter)

# array[3][3] = 2 #12
# counter = output(array,counter)

# array[3][4] = 1 #13
# counter = output(array,counter)

# print(global_array[3][4][:])
print("finish!")






