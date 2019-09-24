# Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the
# chessboard, determine whether a queen can go from the first cell to the second in one move.
#
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two -
# for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go
# from the first cell to the second in one move, or NO otherwise.

while True:
    x_src = int(input("x source"))
    y_src = int(input("y source"))
    x_dst = int(input("x destination "))
    y_dst = int(input("y destination "))

    # move left , right
    # 5,5 -> 5,4 / 5,3 / 5,2 / 5,1 / 5,6 / 5,7
    # move top , bottom
    # 5,5 -> 4,5 / 3,5 / 2 ,5 / 1,5 /6,5 / 7/5
    # move diagonally
    # |x1 - x2| == |y1-y2|

    if abs(x_src - x_dst) == abs(y_src - y_dst) or x_src == x_dst or y_src == y_dst:
        print("correct queen move")
    else:
        print("it is not a queen move")