from read_pic import *
from draw_test import *

isOver = 0 #not over

print('Enter your x_coordinate: ')
x = int(input())

print('Enter your y_coordinate: ')
y = int(input())

print('Enter the type: (2 white / 1 black)')
Type = int(input())

array[y-1][x-1] = Type #1
counter = output(array,counter)

print("Over? (1) ")
isOver = int(input())

while(isOver != 1):
    print('Enter your x_coordinate: ')
    x = int(input())

    print('Enter your y_coordinate: ')
    y = int(input())

    print('Enter the type: (2 white / 1 black)')
    Type = int(input())

    array[y-1][x-1] = Type #1
    counter = output(array,counter)

    print("(15,4)", global_array[15][4][:])
    
    create_pdf(filename, player_name1, player_name2, result, img, img2)

    print("Over? (1) ")
    isOver = int(input())





