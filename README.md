# go_game_extension
This is a repo that can recognize a continuous frames from video and generate the board state into PDF files in ascending.

### TODO list :heavy_check_mark: 
Idx | Content | State | Note
:------------ | :-------------| :-------------| :-------------
1 | Split video into frames | :heavy_check_mark: | 
2 | Select valid frames and remove duplicate, occlusion frames | | let CNN fix it, by adding detail labels
3 | Recognize frames and generate board, black point and white point | :heavy_check_mark: | only detect pieces, make a version with predict pieces condition
4 | Draw output frame with specific input and output | :heavy_check_mark: |
5 | Generate PDF file | :heavy_check_mark: |

#### IDEA
Regarding how to idendity hand location and reflect.
  - Solution: Saved all the reflect coordinates during the first frame (blank board)

#### LOG

11/25
- Calculate corner pixel and corresponding R,G,B values

11/26
- Achieved perspective homography transformation
- GO board line detection
- TODO: calibration on parameters to obtain a precise detection results

12/10
- recognize black and white point
- some defect error

12/25
- use CNN model to generate board coordinates and pieces existence
- [TOFIX] our model can only detect pieces existence, add labels to show each position condition probability
- generate board graph with pieces numbers
- extract board images in PDF format
