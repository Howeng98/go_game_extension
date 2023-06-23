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

# 讀取圖像
# img = cv2.imread("./data/frame580.jpg") #BGR
root_img = cv2.imread("./data/frame200.jpg")  #BGR
img = cv2.cvtColor(root_img, cv2.COLOR_BGR2RGB)  #RGB


img_w_h = 1100
pts1 = np.float32([(520,64),(587,1034),(1592,52),(1561,987)])
pts2 = np.float32([(0,0), (0,img_w_h), (img_w_h,10), (img_w_h,img_w_h)])


m = cv2.getPerspectiveTransform(pts1, pts2) 
aligned_img = cv2.warpPerspective(img, m, (img_w_h, img_w_h))

# 轉為灰度圖像
gray = cv2.cvtColor(aligned_img, cv2.COLOR_RGB2GRAY)

# 使用Canny邊緣檢測算法檢測圖像邊緣
edges = cv2.Canny(gray, 20, 150, apertureSize=3)

# 尋找圖像中的輪廓
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 找到最大的矩形（即棋盤外框）
max_area = 0
max_rect = None
for cnt in contours:
    rect = cv2.boundingRect(cnt)
    area = rect[2] * rect[3]
    if area > max_area:
        max_area = area
        max_rect = rect

# 繪製最大的矩形（即棋盤外框的邊緣）
x, y, w, h = max_rect
# cv2.rectangle(aligned_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(x,y,w,h)
print(aligned_img.shape)

count = 0
flag = 0

# for new_h in range(h):
#     # print(new_x, y)
#     #img[y,x,rgb] 才能得到你現實看到的x，y坐標上的RGB數值!
    
#     y_hat = y + new_h
#     r, g, b = aligned_img[x, y_hat, :]
#     print(x, y_hat, r, g, b)
#     if r > 130 and g > 90 and b > 90:
#         aligned_img = cv2.circle(aligned_img, (x, y_hat), radius=20, color=(0, 255, 0), thickness=-1)        
#         count += 1
    
#     if count > 200:
#         print("Occlusion!")
#         flag = 1
#         break

for new_w in range(w):

    x_hat = x + new_w
    r, g, b = aligned_img[x_hat, y+h, :]
    print(x_hat, y+h, r, g, b)
    if r > 100 and g > 100 and b > 30:
        aligned_img = cv2.circle(aligned_img, (x_hat, y+h), radius=20, color=(0, 255, 255), thickness=-1)        
        count += 1
    
    if count > 200:
        print("Occlusion!")
        flag = 1
        break

if not flag:
    print("Safe")

# 輸出圖像
aligned_img = cv2.cvtColor(aligned_img, cv2.COLOR_BGR2RGB)
cv2.imwrite('perfect_detected_result.jpg', aligned_img)
# cv2.imwrite('perfect_detected_result_gt.jpg', img2)