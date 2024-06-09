#text =("There is some text")
#print(text[2])
#print(text[-2])
#print(text[0:5])
#print(text[0:-2])
#print(text[2])
#print(text[2::2])
#print(text[1::2])
#print(text[::-1])
#print(text[::2])
#print(len(text))

#lst = text.split(" ")
#print(len(lst))

#txt = input("Write smth - ")
#lst = txt.split(" ")
#res = ""
#for x in lst:
#    res = x + " " + res
#print(res)


#text = "I should run from the house I should run from the house"
#lst = text.split("h")
#res = lst[0] + " " + lst[len(lst)-1]
#print(res)

#text = "I should run from the house I should run from the house"
#i_start = 0
#i_end = 0
#counter = 0
#for index in range(len(text))
#    if text[index] == "h"
#        if counter == 3:
#            i_start = index

print("------------------------------------------------------------------")

while True:
    num = input("Enter number - ")
    if not num.isdigit() or len(num) != 3:
        continue
    break

x = []
x.extend(num)
print(x)

sum = 0
for el in x:
    sum += int(el)
print(sum)