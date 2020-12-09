import random

def random_value(m,n):
    value = random.randint(m,n)
    return value

def get_odd_random_position():
    counter = 0
    q = 0
    figure = ''
    random_string_position = ""
    numbers = [0,1,2,2,2,8,0,1,2,2,2,8]
    names = ['k','q','r','n','b','p','K','Q','R','N','B','P']
    board = [['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','','']]
    value = random_value(1,31)
    while(value == 31): value = random_value(1,31)
    i = random_value(0,7)
    j = random_value(0,7)
    board[i][j] = 'K'
    while(board[i][j] == 'K'):
        i = random_value(0,7)
        j = random_value(0,7)
    board[i][j] = 'k'
    for i in range(value):
        value = random_value(0,11)
        while(numbers[value] == 0):
            value = random_value(0,11)
        if (value == 0): figure = "k"
        if (value == 1): figure = "q"
        if (value == 2): figure = "r"
        if (value == 3): figure = "n"
        if (value == 4): figure = "b"
        if (value == 5): figure = "p"
        if (value == 6): figure = "K"
        if (value == 7): figure = "Q"
        if (value == 8): figure = "R"
        if (value == 9): figure = "N"
        if (value == 10): figure = "B"
        if (value == 11): figure = "P"
        numbers[value] -=1
        i = random_value(0,7)
        j = random_value(0,7)
        while (board[i][j] != ''):
            i = random_value(0,7)
            j = random_value(0,7)
        board[i][j] += figure
    for i in range(8):
        q = 0
        for j in range(8):
            if (board[i][j] == ''):
                counter += 1
            if (board[i][j] != '') and (counter != 0):
                random_string_position += str(counter)
                random_string_position += board[i][j]
                counter = 0
            elif (board[i][j] != '') and (counter == 0):
                random_string_position += board[i][j]
                counter = 0
            if (j==7) and (counter !=0):
                random_string_position += str(counter)
                random_string_position += "/"
                q = 1
                counter = 0
            if (j==7) and (counter == 0) and (q!=1) : random_string_position += "/"
    random_string_position = random_string_position[:-1]
    random_string_position += " w "


    if (board[0][4] == 'k'):
        if (board[0][0] == 'r'): random_string_position += 'q'
        if (board[0][7] == 'r'): random_string_position += 'Q'
    if (board[7][4] == 'K'):
        if (board[7][0] == 'R'): random_string_position += 'k'
        if (board[7][7] == 'R'): random_string_position += 'K'
    else:
        random_string_position += '-'
    random_string_position += ' - 0 1'
    return (random_string_position)
