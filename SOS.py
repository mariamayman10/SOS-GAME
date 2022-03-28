# Done By Mariam Ayman Taha
# ID 20210380

# board made as an array of five arrays
board = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-"]]


# function to display the board every turn
def display_board():
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "|" + board[0][3] + "|" + board[0][4])
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|" + board[1][3] + "|" + board[1][4])
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|" + board[2][3] + "|" + board[2][4])
    print(board[3][0] + "|" + board[3][1] + "|" + board[3][2] + "|" + board[3][3] + "|" + board[3][4])
    print(board[4][0] + "|" + board[4][1] + "|" + board[4][2] + "|" + board[4][3] + "|" + board[4][4])


# function to check every turn if there is any 'SOS' shape formed or not
# try, except are used to check if the given indices are valid or not
def check(r, c):
    if board[r][c] == 'S':
        try:
            # check if there is a diagonal formed up at left
            dul = board[r - 1][c - 1] == 'O' and board[r - 2][c - 2] == 'S'
        except:
            # if there is an error detected in the indices it is assigned False
            dul = False
        try:
            # check if there is a diagonal formed up at right
            dur = board[r - 1][c + 1] == 'O' and board[r - 2][c + 2] == 'S'
        except:
            # if there is an error detected in the indices it is assigned False
            dur = False
        try:
            # check if there is a diagonal formed down 'bottom' at left
            dbl = board[r + 1][c - 1] == 'O' and board[r + 2][c - 2] == 'S'
        except:
            # if there is an error detected in the indices it is assigned False
            dbl = False
        try:
            # check if there is a diagonal formed down 'bottom' at right
            dbr = board[r + 1][c + 1] == 'O' and board[r + 2][c + 2] == 'S'
        except:
            # if there is an error detected in the indices it is assigned False
            dbr = False
        try:
            # check if there is a row formed at the left
            rl = board[r][c - 1] == 'O' and board[r][c - 2] == 'S'
        except:
            # if there is an error detected in the indices it is assigned False
            rl = False
        try:
            # check if there is a row formed at the right
            rr = board[r][c + 1] == 'O' and board[r][c + 2] == 'S'
        except:
            # if there is an error detected in the indices it is assigned False
            rr = False
        try:
            # check if there is a column formed up
            cu = board[r - 1][c] == 'O' and board[r - 2][c] == 'S'
        except:
            # if there is an error detected in the indices it is assigned False
            cu = False
        try:
            # check if there is a column formed down 'bottom'
            cb = board[r + 1][c] == 'O' and board[r + 2][c] == 'S'
        except:
            # if there is an error detected in the indices it is assigned False
            cb = False
        return dul + dur + dbl + dbr + rl + rr + cu + cb
    try:
        # check if there is any cross diagonal
        d1 = board[r - 1][c - 1] == 'S' and board[r + 1][c + 1] == 'S'
    except:
        # if there is an error detected in the indices it is assigned False
        d1 = False
    try:
        # check if there is any cross diagonal
        d2 = board[r + 1][c - 1] == 'S' and board[r - 1][c + 1] == 'S'
    except:
        # if there is an error detected in the indices it is assigned False
        d2 = False
    try:
        # check if there is a row formed
        r1 = board[r][c - 1] == 'S' and board[r][c + 1] == 'S'
    except:
        # if there is an error detected in the indices it is assigned False
        r1 = False
    try:
        # check if there is a column formed
        c1 = board[r - 1][c] == 'S' and board[r + 1][c] == 'S'
    except:
        # if there is an error detected in the indices it is assigned False
        c1 = False
    return d1 + d2 + r1 + c1


remaining = 25
player = -1
p1 = 0
p2 = 0
while remaining != 0:
    # if player = 0 means it is player 1's turn else if the player = 1 then it is player 2's turn
    # initialize the player to be player 1

    print("Player {}'s turn".format(player + 1))
    print('#####################\nPlayer 1 = {}\nPlayer 2 = {}\n#####################'.format(p1, p2))
    # display th board to be easier to detect the position
    display_board()
    # let the player input the index of the row and column
    row, col = input("Please Choose Position of row: "), input("Please Choose Position of column: ")
    # check if the input is integer and if not loop until valid input
    while not row.isdigit() or not col.isdigit() or int(row) < 1 or int(row) > 5 or int(col) < 1 or int(col) > 5:
        print("CHECK THAT THE row AND col INPUTS ARE INTEGERS AND IN RANGE 1-5")
        row, col = input("Please Choose Position of row: "), input("Please Choose Position of column: ")
        if row.isdigit() and col.isdigit() and 1 <= int(row) <= 5 and 1 <= int(col) <= 5:
            break
    # let the player choose S or O
    ch = input("Please Choose S or O: ")
    # check if the input is S or O and if not loop until valid input
    while ch != "S" and ch != "O":
        print("CHECK THAT THE INPUT ch IS A CHARACTER AND IS AN 'S' OR 'O'")
        ch = input("Please Choose S or O: ")
        if ch == "S" or ch == "O":
            break
    row = int(row)
    col = int(col)
    # check if the chosen place is not full
    if board[row - 1][col - 1] != '-':
        print("Please Choose Empty Cell")
        player = (player + 1) % 2
        continue
    # modify the board
    board[row - 1][col - 1] = ch
    # check the return of the check function
    score = check(row - 1, col - 1)
    if score > 0:
        if player == 0:
            p1 += score
        else:
            p2 += score
            # flip the player
        player = (player + 1) % 2
    remaining -= 1

if p1 > p2:
    print('Player 1 won')
elif p1 < p2:
    print('Player 2 won')
else:
    print('Game Over')
