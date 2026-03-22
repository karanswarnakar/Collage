board = [" "] * 9


def show(p):
    for i in range(0,9,3):
        print(p[i], p[i + 1], p[i + 2])
    print()
    
player = "X"
for i in range(9):
    show(board)
    pos = int(input("Enter postinon (1-9): ")) -1
    board[pos] = player 
    if player == 'X':
        player = 'O'
    else:
        player = "X"
print("Game Over!")