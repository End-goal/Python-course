dct = {
    1 : "one",
    2.3 : "float",
    "text" : 123,
    True : "awjh",
    None : "flafdoat"
}
print(dct.keys())
print(dct.values())
print(dct.items())

for key in dct.keys():
    print(f"key - {key}, value - {dct[key]}")

print("-"*25)

for item in dct.items():
    print(f"key - {item[0]}, value - {item[1]}")


print("-"*25)

dct = {
    "key1":1234
}
print(dct)

dct["key2"] = "es,gjh"

print(dct)

dct = {
    1 : "one",
    2.3 : "float",
    "text" : 123,
    True : "awjh",
    None : "flafdoat"
}
print(dct.get("text"))
print(dct.get("upuhnipu"))

#setdefault
dct = {
    1 : "one",
    2.3 : "float",
    "text" : 123,
    True : "awjh",
    None : "flafdoat"
}


dct.setdefault("text", 777)
print(dct)
dct.setdefault("upuhnipu", 888)
print(dct)