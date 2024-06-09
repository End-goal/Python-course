import random
WORDLIST = 'робота собака машина людина картопля дім ріст кар\'єр аллах літак комфорт тротил самогубство'.split(" ")
ALPHABET = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщьЮюЯя'


def tablo(pic, mills, cor, word):
    print(pic[len(mills)])
    print("не правильні - ", mills)
    print("")
    for letter in word:
        if letter in cor:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


def get_pics():
    a = r'''
    +----+
    |    
    |   
    |   
    ==='''
    b = r'''
    +----+
    |    0
    |   
    |   
    ==='''
    c = r'''
    +----+
    |    0
    |    |
    |
    ==='''
    d = r'''
    +----+
    |    0
    |   /|
    |
    ==='''
    e = r'''
    +----+
    |    0
    |   /|\
    |   
    ==='''
    f = r'''
    +----+
    |    0
    |   /|\
    |   / 
    ==='''
    g = r'''
    +----+
    |    0
    |   /|\
    |   / \
    ==='''
    lst = [a, b, c, d, e, f, g]
    return lst


def user_input(mis, cor, alf):
    while True:
        u_inp = input("введіть літеру укр. алфавіту - ")
        if len(u_inp) == 0:
            print("нічого нема")
            continue
        elif len(u_inp) > 1:
            print("ОДНУ ітеру")
            continue
        elif u_inp not in alf:
            print("БУКВУ")
            continue
        elif u_inp in cor or u_inp in mis:
            print("вже було")
            continue
        else:
            return u_inp


def analisys(guess, word,  cor_l, mis_l, pic):
    game_con = True
    winner = None
    if guess in word:
        cor_l += guess
        for letter in word:
            if letter not in cor_l:
                return cor_l, mis_l, game_con, winner
        game_con = False
        winner = "player"
        return cor_l, mis_l, game_con, winner
    else:
        mis_l += guess
        if len(mis_l) != len(pic):
            return cor_l, mis_l, game_con, winner
        else:
            game_con = False
            winner = "AI"
            return cor_l, mis_l, game_con, winner


def checkAnotherGame():
    print("Чи хочете грати ще раз?")
    u_input = input().lower()
    if u_input.startswith("т"):
        return True
    elif u_input.startswith("н"):
        return False
    else:
        print("и ввели якусь фігню")


def game(wlist, albt):
    correct_letters = ' '
    missed_letters = ' '
    pictures = get_pics()
    game_continue = True
    winner = None

    word = random.choice(wlist)

    while True:

        tablo(pictures, missed_letters, correct_letters, word)

        guess = user_input(missed_letters, correct_letters, albt)

        correct_letters, missed_letters, game_continue, winner = analisys(guess, word, correct_letters, missed_letters, pictures)

        if game_continue is True:
            continue
        else:
            if winner == "player":
                print(f"ви вгадали слово: {word}")
            else:
                print(f"ви не вгадали слово: {word}")
        if checkAnotherGame():
            game(wlist, albt)
        else:
            break


print("ШИБЕНИЦЯ")
game(WORDLIST, ALPHABET)
print("ДЯКУЮ ЗА ГРУ")
