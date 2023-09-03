
import warnings
from read_pic import *
from fpdf import FPDF
warnings.simplefilter('default', DeprecationWarning)

def create_pdf(filename, player_name1, player_name2, result, img, img2):
    #variables
    circle_x_coor = 18
    circle_y_coor = 214

    text_x_coor = 21.5
    text_y_coor = 221


    isLessThanTen = False
    # Create a new PDF object with A4 size (210x297 mm)
    pdf = FPDF(format='A4')

    # Add a page
    pdf.add_page()

    # Set font and font size
    pdf.set_font("Arial", size=18)

    # Write text on the header line
    pdf.set_y(15)  # Set the y-coordinate for writing text
    pdf.cell(0, -5, txt="GO Report",align="C")

    # Draw a line for the header
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    # Write player names and result text
    pdf.set_font("Arial", size=14)
    pdf.text(10, pdf.get_y() + 10, "black: " + player_name1)
    pdf.text(80, pdf.get_y() + 10, "White: " + player_name2)
    pdf.text(150, pdf.get_y() + 10, result)

    # Set the width and height of the image
    desired_width = 150
    desired_height = 150

    # Set the x and y coordinates for placing the image
    x = (pdf.w - desired_width) / 2
    y = (pdf.h - desired_height) / 2

    # Add the image to the PDF
    pdf.image(img, x=x, y=y-30, w=desired_width, h=desired_height)
    pdf.rect(15,205,180,80,round_corners=True,style="D")

    # pdf.set_fill_color(0)
    # pdf.circle(20,215,6.8,style=None)
    # pdf.set_font("Helvetica", size=18)
    # pdf.text(21.5,220.7,"1")

    # pdf.text(28, 221, " = ")


    # pdf.set_fill_color(r=0, g=0, b=0)
    # pdf.circle(x=36, y=215, r=7, style="FD")

    # pdf.set_text_color(255,255,255)
    # pdf.text(37.5,220.7, "3")

    print("test")
    #find number 

    pdf.set_font_size(16) 
    sequence = 1
    while sequence < 25: #Condition of total
        for row in range(19):
            for col in range(19):
                #print("test")
                if len(global_array[row][col]) > 2: #eaten peice
                    print("eaten pieces")

                    if global_array[row][col][2][1] == sequence:
                        #print(global_array[row][col][:])
                        #print("Black")
                        for i in range(2,len(global_array[row][col])):

                            #===========================================
                            if global_array[row][col][i][1] > 9:
                                pdf.set_font_size(14)
                                small_x_move = 0.6
                                small_y_move = 4.98
                            else:
                                pdf.set_font_size(16)

                                small_x_move = 1.5
                                small_y_move = 5.2
                            #===========================================

                            if global_array[row][col][i][0] == 1: #black

                                print("black")
                                pdf.set_fill_color(r=0,g=0,b=0)
                                pdf.circle(circle_x_coor,circle_y_coor,7,style="FD")

                                pdf.set_text_color(255,255,255)
                                #pdf.set_font_size(14)
                                pdf.text(circle_x_coor + small_x_move ,circle_y_coor + small_y_move, str(global_array[row][col][i][1]))

                                circle_x_coor += 10
                            else:
                                print("white")
                                pdf.set_fill_color(0)
                                pdf.circle(circle_x_coor,circle_y_coor,6.8,style=None)

                                pdf.set_text_color(0)
                                pdf.text(circle_x_coor + small_x_move ,circle_y_coor + small_y_move, str(global_array[row][col][i][1]))

                                circle_x_coor += 10
                        
                        #print("hellow")
                        pdf.set_text_color(0)
                        pdf.text(circle_x_coor, circle_y_coor + 5, " = ")
                        circle_x_coor += 10

                        if global_array[row][col][1][1] < 10: #setting font 
                            pdf.set_font_size(16)
                            isLessThanTen = True

                        if global_array[row][col][1][0] == 1: #black   
                            pdf.set_fill_color(r=0,g=0,b=0)
                            pdf.circle(circle_x_coor,circle_y_coor,7,style="FD")

                            pdf.set_text_color(255,255,255)
                            #pdf.set_font_size(14)
                            if (isLessThanTen):
                                pdf.text(circle_x_coor + 1.8 ,circle_y_coor + 5.2, str(global_array[row][col][1][1]))
                            else:
                                pdf.text(circle_x_coor + 0.75 ,circle_y_coor + 4.98, str(global_array[row][col][1][1]))                      

                        else: #white
                            pdf.set_fill_color(0)
                            pdf.circle(circle_x_coor,circle_y_coor,6.8,style=None)
                            pdf.set_text_color(0)

                            if (isLessThanTen):
                                pdf.text(circle_x_coor + 1.8 ,circle_y_coor + 5.2, str(global_array[row][col][1][1])) 
                            else:
                                pdf.text(circle_x_coor + 0.75 ,circle_y_coor + 4.98, str(global_array[row][col][1][1]))            

                            circle_y_coor += 3
                        
                        print("rounded!!!")
                        circle_x_coor = 18
                        circle_y_coor += 10 

        sequence += 1


    # pdf.set_fill_color(0) #black
    # pdf.circle(50, 50, 30,style='F')

    # pdf.set_fill_color(255) #white
    # pdf.circle(100, 50, 30, style = 'F')
    # Save the PDF to the specified file location
    pdf.output("circle.pdf")

 

filename = "GO_6_3.pdf"
player_name1 = "Zackery"
player_name2 = "Bob"
result = "Winner: Zackery"
img = "E:\python_test\GO\go_game_extension-main (2)\go_game_extension-main\output.png"
img2 = "E:\python_test\GO\go_game_extension-main (2)\go_game_extension-main\white_PIC.jpg"

create_pdf(filename, player_name1, player_name2, result, img, img2)
