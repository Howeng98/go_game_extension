import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
from glob import glob
import re


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

def main():
    DATA_DIR = './data'
    IMG_PATHS = glob(os.path.join(DATA_DIR, '*.jpg'))
    
    # IMG_PATHS = ['./data/frame30.jpg', './data/frame164.jpg', './data/frame243.jpg', './data/frame250.jpg', './data/frame392.jpg', './data/frame555.jpg', './data/frame687.jpg', './data/frame821.jpg', './data/frame1000.jpg']
    
    IMG_PATHS.sort(key=lambda f: int(re.sub('\D', '', f)))
    
    mesh = np.linspace(0, 19, 19, dtype=int)
    rows, cols = np.meshgrid(mesh, mesh)
    BOARD = np.zeros_like(rows, dtype=np.uint8)
    step = 0
    for IMG_PATH in IMG_PATHS:

        print(IMG_PATH)
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
        phase = np.zeros_like(rows, dtype=np.uint8)
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
            print(row, col)
            if r < 100 and g < 100 and b < 100:
                phase[row, col] = 1  #黑棋
                black_count += 1

            elif r > 200 and g > 200 and b > 200:
                phase[row, col] = 2  #白棋
                white_count += 1


        # GO board prediction
        print("白棋：{} |  黑棋：{}\n".format(white_count, black_count))
    
    print(phase)

if __name__ == '__main__':
    main()