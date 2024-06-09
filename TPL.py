letters = "ABCDEFGHIJK"
sea = "~"
field = {}
for letter in letters:
    field[letter] = []
    for x in range(10):
        field[letter].append(sea)
print(field)
