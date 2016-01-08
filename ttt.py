from os import system
def clear():
    system('clear')
def print_table(table):
    for row in table:
        for cell in row:
            print(cell, end=' ')
        print()
def game():
    turn = 'X'
    table = [[' ', 1, 2, 3], [1,' ',' ',' '], [2, ' ',' ',' '], [3, ' ', ' ', ' ']]
    print(step(table, turn))
    print_table(table)
def step(table, turn):
    clear()
    print_table(table)
    turn_list = ['X', 'O']
    choise = input("{0}sess is turning now.\nEnter coordinates to put the {0}\nPut you choise bellow:\n".format(turn))
    if choise == None or not choise[0].isdigit() or not choise[2].isdigit() or len(choise) != 3 or 0 > int(choise[0]) > 3 or 0 > int(choise[2]) > 3:
        print('Ipunt incorrect!\nTry again')
        step(table, turn)
    if table[int(choise[0])][int(choise[2])] != ' ':
        print('This cell already exist.\nPlease choise another cell.')
        step(table, turn)
    table[int(choise[2])][int(choise[0])] = turn
    if winner(table, turn):
        clear()
        print('{0} is winner!'.format(turn))
        response = input('You want to play again?(type Y or N)')
        if response.down() == 'y':
            game()
        elif response.down() == 'n':
            exit()
    step(table, turn_list[turn_list.index(turn)-1])
def winner(table, turn):
    if row_win(table, turn):
        return 1
    if column_win(table, turn):
        return 1
    if diagonal_win(table, turn):
        return 1
    return 0
def row_win(table, turn):
    for row in table:
        if row[1] == row[2] == row[3] == turn:
            return 1
    return 0
def column_win(table, turn):
    for t in range(1, 4):
        if table[1][t] == table[2][t] == table[3][t] == turn:
            return 1
    return 0
def diagonal_win(table, turn):
    if table[1][1] == table[2][2] == table[3][3] == turn or table[3][1] == table[2][2] == table[1][3] == turn:
        return 1
    return 0
if __name__ == "__main__":
    game()
