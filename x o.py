import random
import time

def inp_letter():
    u_inp = ""
    while u_inp not in ["Х", "О"]:
        u_inp = input("введіть Х або О - ").upper()
    if u_inp == "Х":
        return "Х", "О"
    else:
        return "О", "Х"


def first_turn():
    if random.randint(0,1) == 0:
        return "Player"
    else:
        return "Computer"


def display_board(board):
    print(f'''
        {board[1]}|{board[2]}|{board[3]}
        -+-+-
        {board[4]}|{board[5]}|{board[6]}
        -+-+-
        {board[7]}|{board[8]}|{board[9]}
''')

def is_cell_free(board, move):
    return board[int(move)] == " "



def get_player_move(board):
    p_move = " "
    while p_move not in "1 2 3 4 5 6 7 8 9".split() or not is_cell_free(board, p_move):
        p_move = input("Куди ставимо? (1-9) - ")

    return int(p_move)


def make_move(board, p_move, letter):
    board[p_move] = letter
    return board


def is_winner(bo, le):
    if (bo[1] == le and bo[2] == le and bo[3] == le) or \
       (bo[4] == le and bo[5] == le and bo[6] == le) or \
       (bo[7] == le and bo[8] == le and bo[6] == le) or \
       (bo[1] == le and bo[4] == le and bo[7] == le) or \
       (bo[2] == le and bo[5] == le and bo[8] == le) or \
       (bo[3] == le and bo[6] == le and bo[9] == le) or \
       (bo[1] == le and bo[5] == le and bo[9] == le) or \
       (bo[3] == le and bo[5] == le and bo[7] == le):
        return True
    else:
        return False


def get_comp_move(boa, c_let, p_let):
    for i in range(1, 10):
        if boa[i] == " ":
            boa_cop = boa[:]
            boa_cop[i] = c_let
            if is_winner(boa_cop, c_let):
                return i
    for i in range(1, 10):
        if boa[i] == " ":
            boa_cop = boa[:]
            boa_cop[i] = p_let
            if is_winner(boa_cop, p_let):
                return i
    if boa[5] == " ":
        return 5
    lst = []
    for x in [1, 3, 7, 9]:
        if boa[x] == " ":
            lst.append(x)
    if len(lst) > 0:
        return random.choice(lst)
    lst = []
    for x in [2, 4, 6, 8]:
        if boa[x] == " ":
            lst.append(x)
    if len(lst) > 0:
        return random.choice(lst)


def is_board_full(boa):
    for i in range(1, 10):
        if boa[i] == " ":
            return False
    return True


def game():
    board = [" "] * 10
    player_letter, comp_letter = inp_letter()
    print(player_letter)
    print(comp_letter)
    turn = first_turn()
    print(f"\n{turn} робить перший хід")
    game_is_running = True
    while game_is_running:
        if turn == "Player":
            display_board(board)
            p_move = get_player_move(board)
            make_move(board, p_move, player_letter)
            if is_winner(board, player_letter):
                display_board(board)
                print("ТИ ВИГРАВ!!!")
                game_is_running = False
            elif is_board_full(board):
                display_board(board)
                print("НІЧИЯ!!!")
                game_is_running = False
            turn = "Computer"
        else:
            comp_move = get_comp_move(board, comp_letter, player_letter)
            make_move(board, comp_move, comp_letter)
            if is_winner(board, comp_letter):
                display_board(board)
                print("ТИ ПРОГРАВ!!!")
                game_is_running = False
            elif is_board_full(board):
                display_board(board)
                print("НІЧИЯ!!!")
                game_is_running = False
            turn = "Player"


print("--- ХРЕСТИКИ-НОЛИКИ ---")
game()
print("Дякую за гру!")
