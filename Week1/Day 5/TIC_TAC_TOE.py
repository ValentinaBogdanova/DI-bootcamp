# display_board()

board=[[" "," "," "],
       [" "," "," "],
       [" "," "," "],
       ]
def consol(board):
    print('*************')
    for i, row in enumerate(board):
        print("|"," | ".join(row), "|")
        if i <len(board)-1:
            print("---- --- ----")
    print("*************")
consol(board)


def making_move(board, symbol):
    while True:
        input_column=input("Choose a column  ")
        input_row=input("Choose a row  ")
        if not input_column.isdigit() or not input_row.isdigit():
            print("Invalid input. Please enter numbers only.")
            continue
        column=int(input_column)-1
        row =int(input_row)-1
        if row not in [0, 1, 2] or column not in [0, 1, 2]:
            print("Invalid input. Try again")
            continue
        if board[row][column] != " ":
            print("Sorry, this cell is already taken, choose another one")
            continue
        else:
            board[row][column]=symbol
            break

win_combination = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
    ]

def cheking_winner(board, symbol):
    for combination in win_combination:
        if all(board[row][column] == symbol for row, column in combination):
            return True
    return False

def chek_tie(board):
    for i in board:
        if " " in i:
            return False
    return True


        
def main():
    symbol= "X"
    while True:
        making_move(board, symbol)
        if cheking_winner(board, symbol):
            print(f'Player {symbol} wins!')
            break
        if chek_tie(board):
            print("It is a tie!")
            break
        if symbol == "X":
            symbol = "O"
        else:
            symbol = "X"
        consol(board)
main()

