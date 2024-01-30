from random import *
from datetime import *
#1
try:
    n = int(input("Kirjutage 1-9")) 
    if n == "1, 2, 3, 4, 5, 6, 7, 8, 9": 
        for i in range(n):
            print(" -----\n|  O  |\n!  -  !\n -----")
    else:
        print("Ma ütlesin 1 kuni 9")
except :
    print("kasutage ainult numbreid")

#2

n = int(input("n: "))
for i in range(n**3 + 1):
    result = n ** i
    if result <= n ** 3:
        print(f"{n} в степени {i} равно {result}")
    else:
        break

#3

from random import *

o = randint(10, 31)  #õpetused
s = 0 

for i in range(o):
    g = randint(1, 5) #hinnangud
    s+=g  #siin võtan hinnangud kokku
a = s / o 
g1 = round(a, 2)
print("Õpilaste keskmine hinne =", g1)

#4
esimine = 5 #первая сумма
aeg = 0 #возвраст 
rand = randint(1,8)

for t in range(rand):
    esimine = esimine * 2 + aeg   
    aeg += 1
    t += esimine  
    print(f"Aeg: {aeg}, Kingitus: {esimine}, Kogusumma: {t}") #ответ
print(f" {aeg} lõplik vanus.")
