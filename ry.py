#try

text = input("Int please - ")
try:
    int(text)
    print("Int")
except:
    print("Not int")