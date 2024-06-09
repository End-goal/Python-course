def foo(x):
    if type(x) is not list:
        return "This is not list"
    res = []
    for i in x:
        if type(i) is not str:
            res.append(i)
    return res

lst = [1, 2, "text", 3, 4, True, "text2", None, "text3"]
lst2 = foo(lst)
print(lst2)

print("-"*25)

def si(x):
    try:
        x = float(x)
    except:
        return "This is not a number"
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0

user_inp = input("Введи якесь число для функції si(x) - ")
res = si(user_inp)
print(res)

print("-"*25)


lst_st = []
lst_dsk = []
total_st = 0
total_dsk = 0
def user_inp():
    while True:
        us_inp = input("Скільки студентів?")

        try:
            st = int(us_inp)
        except:
            print("Введи нормальне число!")
            continue

        return st

def desks_count(st):
    if st%2 == 0:
        return st//2
    else:
        return st//2 + 1
def summ(lst):
    summ = 0
    for i in lst:
        summ += i
        return summ


for x in range(3):
    students = user_inp()
    desks = desks_count(students)

    lst_st.append(students)
    lst_dsk.append(desks)

total_st = summ(lst_st)
total_dsk = summ(lst_dsk)

print(f"Для {total_st} студентів треба купити {total_dsk} парт")