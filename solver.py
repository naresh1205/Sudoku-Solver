import math
board = [
    [0,9,1,3,8,0,0,0,2],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,6,9,0,0,0,3],
    [6,2,0,5,0,0,0,0,0],
    [0,0,0,0,2,0,0,0,0],
    [0,0,7,0,0,0,0,1,0],
    [0,0,0,0,4,9,0,0,8],
    [5,0,0,0,0,7,0,0,0],
    [2,6,0,0,0,0,0,4,0]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, len(bo) + 1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    #check rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check columns
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check square
    dim = int(math.sqrt(len(bo)))
    box_x = pos[0] // dim
    box_y = pos[1] // dim
    for i in range(dim * box_x, dim * box_x + dim):
        for j in range(dim * box_y, dim * box_y + dim):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


#Printing the board
def print_board(bo):
    dim = int(math.sqrt(len(bo)))
    for i in range(len(bo)):
        if i % dim == 0 and i != 0:
            print("------------------------")

        for j in range(len(bo[0])):
            if j % dim == 0 and j != 0:
                print(" | ", end="")
            if j ==  len(bo) - 1:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#finding empty element
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if(bo[i][j] == 0):
                return (i, j) # row, column

    return None

#printing board before solving
print_board(board)

print("~~~~~~~~~~~~~~~~~~~~~~~")
solve(board)

#printing solved board
print_board(board)
