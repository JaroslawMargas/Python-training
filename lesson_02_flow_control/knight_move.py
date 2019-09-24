# Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells
# vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can
# go from the first cell to the second in one move.
#
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two -
# for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go
# from the first cell to the second in one move, or NO otherwise.

while True:
    x_src = int(input("x source"))
    y_src = int(input("y source"))
    x_dst = int(input("x destination "))
    y_dst = int(input("y destination "))

    # x -+2  and y -+ 1
    # x -+1 and y -+2

    if abs(x_src - x_dst) == 2 and abs(y_src - y_dst) == 1 or \
            abs(x_src - x_dst) == 1 and abs(y_src - y_dst) == 2:
        print("correct knight move")
    else:
        print("it is not a knight move")