import os
import numpy as np

os.system('')


cv2.imwrite('./output.png', img)
def read_and_preprocess_img(IMG_PATH):
    
    img = cv2.imread(IMG_PATH)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 先轉成灰階處理
    ret, thresh = cv2.threshold(img_gray, 200, 255, 0)  # 利用 threshold 過濾出高光的部分，目前設定高於 200 即為高光
    contours, hierarchy  = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_zero = np.zeros(img.shape, dtype=np.uint8) 
    
#     print(len(contours))

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour) 
        img_zero[y:y+h, x:x+w] = 255 
        mask = img_zero     
    
    # alpha，beta 共同決定高光消除後的模糊程度
    # alpha: 亮度的缩放因子，默認是 0.2， 範圍[0, 2], 值越大，亮度越低
    # beta:  亮度缩放後加上的参数，默認是 0.4， 範圍[0, 2]，值越大，亮度越低
    result = cv2.illuminationChange(img, mask, alpha=0.2, beta=0.4) 
    
    pts1 = np.float32([(513,55),(583,1040),(1603,57),(1554,981)])
    pts2 = np.float32([(0,0), (0,1100), (1100,10), (1100,1100)])
    m = cv2.getPerspectiveTransform(pts1, pts2) 
    fixed_rgb_img = cv2.warpPerspective(result, m, (1105, 1105))
    return fixed_rgb_img

def show_phase(phase):
    """显示局面"""
    
    for i in range(19):
        for j in range(19):
            if phase[i,j] == 1: 
                chessman = chr(0x25cf)
            elif phase[i,j] == 2:
                chessman = chr(0x25cb)
            elif phase[i,j] == 9:
                chessman = chr(0x2606)
            else:
                if i == 0:
                    if j == 0:
                        chessman = '%s '%chr(0x250c)
                    elif j == 18:
                        chessman = '%s '%chr(0x2510)
                    else:
                        chessman = '%s '%chr(0x252c)
                elif i == 18:
                    if j == 0:
                        chessman = '%s '%chr(0x2514)
                    elif j == 18:
                        chessman = '%s '%chr(0x2518)
                    else:
                        chessman = '%s '%chr(0x2534)
                elif j == 0:
                    chessman = '%s '%chr(0x251c)
                elif j == 18:
                    chessman = '%s '%chr(0x2524)
                else:
                    chessman = '%s '%chr(0x253c)
            print('\033[0;30;43m' + chessman + '\033[0m', end='')
        print()
    
phase = np.array([
    [0,0,2,1,1,0,1,1,1,2,0,2,0,2,1,0,1,0,0],
    [0,0,2,1,0,1,1,1,2,0,2,0,2,2,1,1,1,0,0],
    [0,0,2,1,1,0,0,1,2,2,0,2,0,2,1,0,1,0,0],
    [0,2,1,0,1,1,0,1,2,0,2,2,2,0,2,1,0,1,0],
    [0,2,1,1,0,1,1,2,2,2,2,0,0,2,2,1,0,1,0],
    [0,0,2,1,1,1,1,2,0,2,0,2,0,0,2,1,0,0,0],
    [0,0,2,2,2,2,1,2,2,0,0,0,0,0,2,1,0,0,0],
    [2,2,2,0,0,0,2,1,1,2,0,2,0,0,2,1,0,0,0],
    [1,1,2,0,0,0,2,2,1,2,0,0,0,0,2,1,0,0,0],
    [1,0,1,2,0,2,1,1,1,1,2,2,2,0,2,1,1,1,1],
    [0,1,1,2,0,2,1,0,0,0,1,2,0,2,2,1,0,0,1],
    [1,1,2,2,2,2,2,1,0,0,1,2,2,0,2,1,0,0,0],
    [2,2,0,2,2,0,2,1,0,0,1,2,0,2,2,2,1,0,0],
    [0,2,0,0,0,0,2,1,0,1,1,2,2,0,2,1,0,0,0],
    [0,2,0,0,0,2,1,0,0,1,0,1,1,2,2,1,0,0,0],
    [0,0,2,0,2,2,1,1,1,1,0,1,0,1,1,0,0,0,0],
    [0,2,2,0,2,1,0,0,0,0,1,0,0,0,0,1,1,0,0],
    [0,0,2,0,2,1,0,1,1,0,0,1,0,1,0,1,0,0,0],
    [0,0,0,2,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0]
], dtype=np.ubyte)

show_phase(phase)
