import random
import time

WATER_CELL = "~"
SHIP_CELL = "H"
MISSED_CELL = "o"
HIT_CELL = "X"
SHIPS_FOR_PLAYER = 8
FIELD_LETTERS = "ABCDEF"


def create_field(letters, water):
    field = dict()
    for l in letters:
        field[l] = []
        for i in range(len(letters)):
            field[l].append(water)
    return field


def fill_field(field, s_cell, s_f_p):
    for i in range(s_f_p):
        while True:
            random_key = random.choice(list(field.keys()))
            random_value = random.randint(0, len(list(field.keys()))-1)
            if field[random_key][random_value] == s_cell:
                continue
            else:
                field[random_key][random_value] = s_cell
                break
    return field


def ship_counter(field, s_cell):
    counter = 0
    for lst in list(field.values()):
        for value in lst:
            if value == s_cell:
                counter += 1
    return counter


def game_continue(p_field, c_field, s_cell):
    p_counter = ship_counter(p_field, s_cell)
    c_counter = ship_counter(c_field, s_cell)
    if p_counter and c_counter:
        return True
    else:
        return False


def print_one_field(field, s_cell, is_visible=True):
    num = "  "
    for x in range(len(field)):
        num += str(x) + " "
    print(num)
    for key in list(field.keys()):
        st = f"{key}"
        for value in field[key]:
            if value == s_cell and is_visible is False:
                st += " " + "~"
            else:
                st += " " + value
        print(st)


def display_board(p_field, c_field, p_ships, c_ships, s_cell):
    print("\n--- SEA BATTLE ---\n")
    time.sleep(1)
    print("     PLAYER FIELD")
    print_one_field(p_field, s_cell, is_visible=True)
    time.sleep(1)
    print("\n     COMPUTER FIELD")
    print_one_field(c_field, s_cell, is_visible=False)
    time.sleep(1)
    print(f'''\nSTAT:
    Player ships - {p_ships}
    Computer ships - {c_ships}''')


def player_shoots(letters, m_cell, h_cell, comp_field):
    numbers = ""
    for x in range(len(letters)):
        numbers += str(x)

    while True:
        u_inp = input("where to fire? - ").upper()

        if len(u_inp) == 0:
            print("no data of cell")
            continue
        elif len(u_inp) != 2:
            print("not enough data")
            continue
        elif u_inp[0] not in letters or u_inp[1] not in numbers:
            print("wrong cell data")
            continue
            
        if comp_field[u_inp[0]][int(u_inp[1])] == m_cell or comp_field[u_inp[0]][int(u_inp[1])] == h_cell:
            print("don't repeat your fails")
        else:
            return u_inp


def comp_shoots(letters, m_cell, h_cell, player_field):
    while True:
        random_l = random.choice(letters)
        random_n = random.randint(0, len(letters)-1)
        if player_field[random_l][random_n] == m_cell or \
                player_field[random_l][random_n] == h_cell:
            continue
        else:
            return random_l + str(random_n)


def analis(field, shot, ship, mis, hit):
    let = shot[0]
    num = int(shot[1])
    if field[let][num] == ship:
        print("ship damaged")
        field[let][num] = hit
    else:
        print("shot missed")
        field[let][num] = mis
    return field


def game(w_cell, s_cell, mis_cell, hit_cell, s_f_p, letters):
    player_field = create_field(letters, w_cell)
    comp_field = create_field(letters, w_cell)
    player_field = fill_field(player_field, s_cell, s_f_p)
    comp_field = fill_field(comp_field, s_cell, s_f_p)
    while game_continue(player_field, comp_field, s_cell):
        display_board(
            player_field,
            comp_field,
            ship_counter(player_field, s_cell),
            ship_counter(comp_field, s_cell),
            s_cell
        )
        p_shot = player_shoots(letters, mis_cell, hit_cell, comp_field)
        print(f"\nYou are shooting at {p_shot}")
        comp_field = analis(comp_field, p_shot, s_cell, mis_cell, hit_cell)
        time.sleep(2)

        comp_shot = comp_shoots(letters, mis_cell, hit_cell, player_field)
        print(f"\nAI is shooting at {comp_shot}")
        player_field = analis(player_field, comp_shot, s_cell, mis_cell, hit_cell)
        time.sleep(2)

    winner = ""
    if ship_counter(player_field) > ship_counter(comp_field):
        winner = "PLAYER"
    elif ship_counter(player_field) < ship_counter(comp_field):
        winner = "AI"
    else:
        winner = "DRAW"
    print(f'''
~~~~~~~~~~~~~~~~
{winner} wins!!
~~~~~~~~~~~~~~~~
''')


print("SEA BATTLE")
game(WATER_CELL, SHIP_CELL, MISSED_CELL, HIT_CELL, SHIPS_FOR_PLAYER, FIELD_LETTERS)
print("THANKS FOR PLAYING")
