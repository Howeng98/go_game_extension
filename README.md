# go_game_extension
This is a repo that can recognize a continuous frames from video and generate the board state into PDF files in ascending.

### TODO list :heavy_check_mark: 
Idx | Content | State | Note
:------------ | :-------------| :-------------| :-------------
1 | Split video into frames | :heavy_check_mark: | 
2 | Select valid frames and remove duplicate, occlusion frames | |
3 | Recognize frames and generate board, black point and white point | |
4 | Draw output frame with specific input and output | |
5 | Generate PDF file | |

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
