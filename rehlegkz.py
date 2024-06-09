import random
# txt = input("text, please ")
# lit = txt.split()
# soul = ""
# for z in lit:
#     soul = z + " " + soul
# print(soul)

# txt = "i should run from this horrible house i should run from this horrible house"
# con_staruto = 0
# con_enudo = 0
# counter = 0
# for index in range(len(txt)):
#     if txt[index] == "h":
#         counter += 1
#     if counter == 3:
#         con_staruto = index+2
#     if counter == 5:
#         con_enudo = index
# print(txt[con_staruto:con_enudo])

# txt = input("3 simbol number ")
# lst = []
# lst.extend(txt)
# x = len(lst)
# if x > 3:
#     print("3 simboled number required")
# if x < 3:
#     print("3 simboled number required")
# summ = lst[0]+lst[1]+lst[2]
# print(summ)

round = 1
scr_p = 0
scr_AI = 0
variants= ["r", "p", 's']
while round < 4:
    print(f"round {round}\n")
    AI_choice = random.choice(variants)
    while True:
        p_choice = input('''pick: (r)ock (p)paper (s)cissors \n''').lower()
        if (p_choice[0] not in variants) or (len(p_choice) == 0):
            continue
        p_choice = p_choice[0]
        break
    print(f"Player chosed ({p_choice}) AI chosed ({AI_choice})")
    if p_choice == AI_choice:
        print("DRAW. Let`s try again\n")
    elif (p_choice == "r" and AI_choice == "s") or \
         (p_choice == "s" and AI_choice == "p") or \
         (p_choice == "p" and AI_choice == "r"):
        print("player wins round\n")
        scr_p += 1
    else:
        print("AI wis round\n")
        scr_AI += 1
    round += 1
    print("--"*25)


print("GAME")
print(f"AI score is {scr_AI} Player score is {scr_p}")
if scr_p > scr_AI:
    print("Player won")
elif scr_p == scr_AI:
    print("ended in draw")
else:
    print("AI won")
