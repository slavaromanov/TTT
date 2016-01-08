from os import system

def new_game():
    step([[' ', 1, 2, 3], [1,' ',' ',' '], [2, ' ',' ',' '], [3, ' ', ' ', ' ']], 'X')

def step(table, turn, msg=''):
    clear(table, msg)
    turn_list = ['X', 'O']
    try:
        x, y = map(int, input("{0} is turning now.\nWrite 2 digits from 1 to 3 via space.\n".format(turn)).split(' '))
    except ValueError or IndexError:
        step(table, turn, msg='Incorrect input, try again')
    if table[x][y] != ' ':
        step(table, turn, msg='This cell already exits, choise another cell.')
    table[x][y] = turn
    if winner(table, turn):
        clear(table, '{0} is winner!'.format(turn))
        end()
    if draw(table):
        clear(table, 'Draw!')
        end()
    step(table, turn_list[turn_list.index(turn)-1])

def clear(table, msg):
    system('clear')
    print(msg)
    print_table(table)

def end():
    response = input('You want to play again?(type Y or N and press enter)\n')
    if response.lower() == 'y': new_game()
    elif response.lower() == 'n': exit()
    else:
        print('Error, try again.')
        end()

def print_table(table):
    for row in table:
        for cell in row:
            print(cell, end=' ')
        print()

def winner(table, turn):
    if row_win(table, turn) or column_win(table, turn) or diagonal_win(table, turn): return 1

def row_win(table, turn):
    for row in table[1:]:
        if row[1] == row[2] == row[3] == turn: return 1

def column_win(table, turn):
    for t in range(1, 4):
        if table[1][t] == table[2][t] == table[3][t] == turn: return 1

def diagonal_win(table, turn):
    if table[1][1] == table[2][2] == table[3][3] == turn or table[3][1] == table[2][2] == table[1][3] == turn: return 1

def draw(table):
    return all(map(lambda x: all(map(str.isalpha, x[1:])), table[1:]))

if __name__ == "__main__":
    new_game()
