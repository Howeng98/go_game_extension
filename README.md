# Go game board recognition :black_circle: :white_circle:
This is a repo that can recognize a continuous frames from video and generate the board state into PDF files in ascending.


<p align="center">
  <img src='imgs/output.png'>
</p>


## Run
```
python main.py
```

## TODO list :heavy_check_mark: 
Idx | Content | State | Note
:------------ | :-------------| :-------------| :-------------
1 | Split video into frames | :heavy_check_mark: | 
2 | Recognize frames and generate board, black point and white point | :heavy_check_mark: | only detect pieces, make a version with predict pieces condition
3 | Select valid frames and remove duplicate, occlusion frames | | 
4 | Draw output frame with specific input and output | :heavy_check_mark: |
5 | Generate PDF file |  |
## LOG
### 11/25
- Calculate corner pixel and corresponding R,G,B values
---

### 11/26
- Achieved perspective homography transformation
- GO board line detection
- TODO: calibration on parameters to obtain a precise detection results
---

### 12/10
- recognize black and white point
- some defect error
---

### 12/25
- use CNN model to generate board coordinates and pieces existence
- [TOFIX] our model can only detect pieces existence, add labels to show each position condition probability
- generate board graph with pieces numbers
- extract board images in PDF format
---

### 02/19
  
  Accomplished
  - use conventional CV to remove light reflection effect
  - successful detect all pieces with correct outputs
  - generate board with pieces numbers and states    
---

### 02/28

  Accomplished
  - Make a function to handle input array of board state, and draw circles in an standard form

---
### 03/04
Accomplished
  - Consider multiple frames inputs, and update the current board state. (Rewrite function)
  - Ensure pieces algo is accurate without hand cases.
  
  Future Works:  
  - Solve the hand occlusion problem by checking the saved global board to detect whether have any missing pieces 
  - Consider the eaten pieces case and label
  - Output into PDF format
    
  TODO and Discussions:
  - Remove hand case by checking pixel RGB values and remove hand frames (Ho)
  - Remove redundant frames by adding delay into videocaptured (Zac)  
  - Output board and string information into PDF (Zac)
  
---
### 03/26
Accomplished
  - Remove redundant frames by adding delay into videocaptured (Zac)  
  - Output board and string information into PDF (Zac)
  
  Future Works:  
  - Solve the hand occlusion problem by checking the saved global board to detect whether have any missing pieces 
  - Consider the eaten pieces case and label
    
  TODO and Discussions:
  - Remove hand case by checking pixel RGB values and remove hand frames
  
---
### 04/02
Accomplished    
  - Consider the eaten pieces case and label
  
  Future Works:  
  - Solve the hand occlusion problem by checking the saved global board to detect whether have any missing pieces 
  - My dict need to store peices color and counter number, build a global board to store the pieces coming time.
    
---
### 04/09
Accomplished    
  - Fix global array with eaten pieces case.
  
  Future Works:  
  - PDF write eaten pieces statement
  - Solve the hand occlusion problem by checking the saved global board to detect whether have any missing pieces 

---
### 04/16
Accomplished    
  - PDF write eaten pieces statement
  
  Future Works:  
  - Reunion all the components
  - Solve the hand occlusion problem by checking the saved global board to detect whether have any missing pieces 


## References
1. [Kifu Snap](https://www.crazy-sensei.com/?lang=en)
2. [Pix Spy](https://pixspy.com/)
3. [PDF Generate](https://github.com/PyFPDF/fpdf2)
4. [PDF Generate Document](https://pyfpdf.github.io/fpdf2/Shapes.html)
6. https://tw511.com/a/01/36832.html
7. https://auzhu.com/sports/1025003.html

