print(20+(7*10-3)*52)
coin_found=20
copy_per_day=10
crow_steal=3
weeks=52
print(coin_found+(7*copy_per_day-crow_steal)*weeks)
print("---------")

#data tipes

#int - solid number
a=10
print(type(a))
b=10/2
print(type(b))
print("---------")
a=0.1
b=0.2
print(a+b)
print("---------")

#остача від ділення

a=7
b=2
print(a/b)
print(a//b)#solid only
print(a%b)#find left over
print("---------")

#округлення

a=5.6565132145314

print(round(a,5))
#-,x — кылькысть чисел після точки

#сумісність int, float

print("---------")

x=5.3
y=0.7

z=x+y
print(z)
print(type(z))

#BOOLEAN - TRUE?

print("---------")


a=100

print(a>100)
print(a<100)
print(a>=100)
print(a<=100)
print(a==100)
print(a!=100)

#none

#string

    #\n- пернос на нову строку
    #'''vvv''' - копіювання запрограмованого
    #"сказав:\"відстань"" - \для ігнорування усіх лапок окрім тих, що зкраю

#пошук по рядку
print("---------")
print("a" in "kgfahfdh")
letters= "gf"
text="kgfahfdh"
print(letters in text)

#приведення даних

a = "12"

print(type(a))
a = int(a)
a = float(a)
print(type(a))

#false-0 true-1
print("----------"*10)

a=100
a=bool(a)
print(a)
a=0
a=bool(a)
print(a)
a="ahf"
a=bool(a)
print(a)
a=""
a=bool(a)
print(a)

#оєднання інформації для виводу на екран
print("----------"*10)

a=1
b=2
print("1+2=",a+b)

s="Anya"+"Khrystyna"
print(s)
print("Anya","Khrystyna")

v=12
print("sus",v,"fof")

print("shot %s tanks" %10)
print("shot %s tanks" %"10")
print("----------"*10)
sus="shot %s tanks"
sun="shot %s tanks and %s planes"
puf=10
fup=5
print(sus %puf)
print(sun %(puf,fup))
print("----------"*10)
a=0
b=8
sul="{} sayed to {}: cool belt" 
print(sul.format(a,b))
print("----------"*10)
a=0
b=8
sul=f"{a} sayed to {b}: cool belt"
print(sul)
print("----------"*10)
print("----------"*10)
адреса="вул.Шляховецького"
номер_дому="буд.25"
місто="Велика Малишівка"
адресат="Олександр Волудько"
адресант="Дмитрій Садиба"
посада="головний бухгалтер"
пропуск=" "*25
борг="2500"
текст=f'''{пропуск}{адреса}
{пропуск}{номер_дому}
{пропуск}{місто}

Шановний пане {адресат}

Маю вас повідомити, що вам нараховано борг за несплату комунальних рахунків у розмірі {борг} ГРН.
Сплатити свій борг ви можете у найближчому відділенні ЖКХ

{адресант}
{посада}'''
print(текст)
print("----------"*10)
print("----------"*10)
адреса = input("напиши адресу: ")
номер_дому=input("напиши номер дому: ")
місто=input("напиши назву міста/села: ")
адресат=input("напиши ім'я адресата: ")
адресант=input("напиши ім'я адресанта: ")
посада=input("напиши посаду: ")
борг=input("напиши заборгованність: ")
пропуск=" "*25
текст=f'''{пропуск}{адреса}
{пропуск}{номер_дому}
{пропуск}{місто}

Шановний пане {адресат}

Маю вас повідомити, що вам нараховано борг за несплату комунальних рахунків у розмірі {борг} ГРН.
Сплатити свій борг ви можете у найближчому відділенні ЖКХ

{адресант}
{посада}'''
print(текст)












