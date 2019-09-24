# In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard,
# determine whether a bishop can go from the first to the second in one move.
#
# The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting
# square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from
# the first square to the second in one move, or NO otherwise.

while True:
    x_src = int(input("x source"))
    y_src = int(input("y source"))
    x_dst = int(input("x destination "))
    y_dst = int(input("y destination "))

    # example source
    # (x = 3, y = 2)
    #
    # and possibilities move: 1 field
    # (2,1) and (2,3) and (4,1) and (4,3)
    #
    # 3->2 2->1
    # 3->2 2->3
    # 3->4 2->1
    # 3->4 2->1
    # solution: delta_x =1 and delta_y =1
    # solution N field = delta x = y = N

    if abs(x_src - x_dst) == abs(y_src - y_dst):
        print("correct bishop move")
    else:
        print("it is not a bishop move")