import random

def get_pics():
    a = r'''
    +---+
    |   
    |  
    |  
    ===
    '''
    b =r'''
    +---+
    |   0
    |  
    |  
    ===
    '''
    c = r'''
    +---+
    |   0
    |  /
    |  
    ===
    '''
    d = r'''
    +---+
    |   0
    |  /|
    |  
    ===
    '''
    e = r'''
    +---+
    |   0
    |  /|\
    |  
    ===
    '''
    f = r'''
    +---+
    |   0
    |  /|\
    |  / 
    ===
    '''
    g = r'''
    +---+
    |   0
    |  /|\
    |  / \
    ===
    '''
    list = [a, b, c, d, e, f, g]
    return list

def displayBoard(pics, secret_word, correct_letters, missed_letters):
    print(pics[len(missed_letters)])
    print("Помилкові літери: ", missed_letters)
    for letter in secret_word:
        if letter in correct_letters:
            print(letter, end = " ")
        else:
            print("_", end=" ")
    print()

def getGuess(correct_letters, missed_letters, alphabet):
    while True:
        letter = input("Введіть літеру - ")

        if len(letter) != 1:
            print("Введи одну букву!")
            continue
        elif letter not in alphabet:
            print("Введи букву!")
            continue
        elif letter in correct_letters or \
            letter in missed_letters:
            print("Таку літеру ви вже називали")
            continue
        else:
            return letter

def analis(guess, secret_word, correct_letters, missed_letters, pics):
    if guess in secret_word:
        correct_letters += guess
        for letter in secret_word:
            if not letter in correct_letters:
                return None, correct_letters, missed_letters
        return f"Ви вгадали слово {secret_word}!", correct_letters, missed_letters

    else:
        missed_letters += guess
        if len(missed_letters) != len(pics):
            return None, correct_letters, missed_letters

        return f"закінчились спроби! Ви не вгадали слово {secret_word}!", correct_letters, missed_letters


def endGameCheck():
    while True:
        u_inp = input("ЧИ ХОЧЕТЕ ВИ ЗІГРАТИ ЩЕ РАЗ???  (так/ні) - ").lower()
        if u_inp not in ["т", "так", "н", "ні"]:
            print("Будьте уважні з відповідями.")
            continue
        elif u_inp in ["т", "так"]:
            return True
        elif u_inp in ["т", "так"]:
            return False
def game(wordlist, alphabet, pics):
    secret_word = random.choice(wordlist.split())
    correct_letters = ''
    missed_letters = ''
    gameIsDone = False

    while True:
        displayBoard(pics, secret_word, correct_letters, missed_letters)

        guess = getGuess(correct_letters, missed_letters, alphabet)

        res, correct_letters, missed_letters = analis(guess, secret_word, correct_letters, missed_letters, pics)
        if res == None:
            continue
        else:
            print(res)

        ContinueGame = endGameCheck()
        if ContinueGame == True:
            game(wordlist, alphabet, pics)
        else:
            break

wordlist = "аіст акула бабуїн баран барсук бобер бик верблюд"
alphabet = "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщьЮюЯя"

print('Ш И Б Е Н И Ц Я')
pics = get_pics()
game(wordlist, alphabet, pics)
print("ДЯКУЄМО ЗА ГРУ!")