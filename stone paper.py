import random

score_player = 0
score_comp = 0
round = 1

variants = ["r", "p", "s"]

while round < 4:
    print(f"ROUND NUMBER {round}")
    while True:
        player_choice = input("Enter your choice (r)rock, (p)paper, (s)scissors - ").lower()
        if len(player_choice) == 0:
            continue
        if player_choice[0] not in variants:
            continue
        player_choice = player_choice[0]
        break
    comp_choice = random.choice(variants)

    print(f"computer choise is {comp_choice}, Player choise is {player_choice}")
    if comp_choice == player_choice:
        print("Draw. Try one more time.")
        continue
    elif (player_choice == "r" and comp_choice == "s") or \
        (player_choice == "p" and comp_choice == "r") or \
        (player_choice == "s" and comp_choice == "p"):
        print("Player wins")
        score_player += 1
    else:
        print("Computer wins")
        score_comp +=1

    print(f"SCORE: Player ({score_player}) , Computer ({score_comp})")
    round += 1
    print("-"*100)


if score_comp > score_player:
    print("COMPUTER WINS!")
else:
    print("PLAYER WINS!")
print(f"SCORE: Player ({score_player}) , Computer ({score_comp})")
