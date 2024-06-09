lst = []
crt = ()

lst = list()
crt = tuple()
print(crt)
print(type(crt))

print("-"*25)

lst = [1, 3.3, True, None, ["one", "two"]]
crt = (1, 3.3, True, None, ["one", "two"])
print(lst)
print(crt)

lst[0] = "заміна"
print(lst)
#crt[0] = "заміна"
print(lst)

print("-"*25)

for i in crt:
    print(i)

print("-"*25)

crt[4][0] = "заміна"
print(crt)

print("-"*25)

#ser - куча

st = set()
st = {}

#st = {1, 3.3, True, None, ["one", "two"]}
#print(st)

#print(st[0])

st = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
print(st)
#lst = list(st)
#print(lst)

for x in st:
    print(x)

print(1 in st)

st.add("додати")
print(st)
st.remove(1)
print(st)

#frozenSet
fst = frozenset()

print("-"*25)

#dictionary
dct = dict()
dct = {}

dct = {
    "first" : 1,
    "second" : 2,
    3 : "third",
    True: [1,2,3],
    None: 0
}
print(dct)
#print(dct[0])
print(dct["first"])

print(dct.keys())
print(dct.values())

for key in dct.keys():
    print(f"{key} - {dct[key]}")

print("-"*25)

print(3 in dct.keys())
print(4 in dct.keys())

print(3 in dct)

print("-"*25)

#gor i in dct.items():
#print(f"Ключ {i[0]},значення {i[1]}")

calendar = {
    "january" : 31,
    "february" : 28,
    "March" : 31,
    "april" : 30
}

for key in calendar.keys():
    print(f"{key} - {calendar[key]}")

print("-"*25)


students = {
    "Alice": (85, 90, 92),
    "Bob": (78, 85, 88),
    "Charlie": (90, 92, 95)

}
for student in students:
    sum = 0
    for x in students[student]:
        sum += x

    ln = len(students[student])
    av = sum / ln

    print(f"{student} - {av}")




print("-"*25)

orders = {
    "apple": (1, 10),
    "banana": (2, 20),
    "orange": (3, 15)
}
total = 0
for fruit in orders:
    sum = orders[fruit][0]*orders[fruit][1]
    print(f"{fruit} - {sum}")
    total += sum
print(f"Total = {total}")

print("-"*25)

letters = "ABCDEFGHIK"
sea = "~"
field = {}


for letter in letters:
    field[letter] = []
    for x in range(10):
        field[letter].append("~")

print(field)

for key in field.keys():
    str = key

    for i in field[key]:
        str = str + " " + i

    print(str)
