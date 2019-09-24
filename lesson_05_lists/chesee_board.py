# Given two numbers n and m. Create a two-dimensional array of size (n×m) and populate it with the characters "." and
# "*" in a checkerboard pattern. The top left corner should have the character "."

while True:
    try:
        row = int(input("row number"))
        col = int(input("col number"))
        break
    except ValueError:
        print("This value is incorrect")

black_field = "*"
white_field = "."

# make white field
board = [[white_field] * row for i in range(col)]


for i in range(row):
    for j in range(col):
        if i % 2 == 1:
            if j % 2 == 0:
                board[i][j] = black_field
        else:
            if j % 2 == 1:
                board[i][j] = black_field

print(board)
