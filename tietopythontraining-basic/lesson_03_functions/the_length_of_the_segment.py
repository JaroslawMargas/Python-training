# Given four real numbers representing cartesian coordinates: (x1,y1),(x2,y2). Write a function distance(x1, y1, x2,
# y2) to compute the distance between the points (x1,y1) and (x2,y2). Read four real numbers and print the resulting
# distance calculated by the function.

import math

dic_value = {
    1: "x1",
    2: "y1",
    3: "x2",
    4: "y2"
}


def distance(val_list):
    dis = math.sqrt((val_list[3] - val_list[1]) ** 2 + (val_list[2] - val_list[0]) ** 2)
    return dis


if __name__ == "__main__":
    list_cor = []
    x = 1
    while len(list_cor) != 4:
        try:
            val = float(input("provide coordinate " + str(dic_value[x])))
            list_cor.append(val)
            x += 1
        except (SyntaxError, EOFError, ValueError, NameError, TypeError):
            print("wrong value try again !")

    print("distance: " + str(distance(list_cor)))
