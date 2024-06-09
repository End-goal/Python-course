from random import randint


name = input("привіт... а як тебе звати? ")
print(f"добре, {name}, спробуй вгадати число від 1 до 20, даю тобі 6 спроб")
counter = 0

num = randint(1, 20)
for counter in range(6):
    while True:
        guess = input(f"спробуй вгадати моє число, в тебе ще є {6-counter} спроб ")
        if not guess.isdigit():
            print("ІДІОТ, НАПИШИ ЧИСЛО!!!")
        else:
            guess = int(guess)
            break
        break
    if guess < num:
        print("ні, число більше")
    elif guess > num:
        print("ні, число меньше")
    elif guess == num:
        break

if guess == num:
    print(f"молодець вгадав моє число за {counter+1} спроб")
else:
    print(f"дундук це було {num}")