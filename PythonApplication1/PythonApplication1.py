#from datetime import *
#from random import *

#k=0
#while True:
#    k+=1
#    a=randint(1,50)
#    b=randint(1,50)
#    p=0
#    while p!=3:
#        p+=1
#        v=int(input("Millega võrdub {0}+{1}= ".format(a,b)))
#        if v==a+b:
#            print("Tubli!")
#            break
#        else:
#            print("Mõtle veel!")
#    print("{0}+{1}={2}".format(a,b,a+b))
    
#    if k==5:break





##2 summa 10 arvud
#summa=0
#for i in range(10):
#    arv=float(input("Sisesta arv: "))
#    summa+=arv
#print(summa)

#summa=0
#i=0
#while True:
#    i+=1
#    arv=float(input("Sisesta arv: "))
#    summa+=arv
#    if i==10: break
#print(summa)



##1 Siim
#nimi=input("Mis on sinu nimi?")
#mitu=int(input("Mitu korda tervitada?"))
#for i in range(1,mitu+1):
#    print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")


##Komm
#print("1. variant -while True-")
#while True:
#    v=input("Tahan komme!").lower()
#    if v=="komm": break

#print("2. variant -while tingimusega-")
#v=""
#while v!="komm":
#    v=input("Tahan komme!").lower()

##Nädala päevad
#paevad=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede","Laupäev","Pühapäev"]
#tunnid=["8 tundi","9 tundi","5 tundi","8 tundi","6 tundi","tunde pole","tunde pole"]
#for i in range(7):
#    print(paevad[i]+"-"+tunnid[i])

##8 Poes korduslausega
#arve_nr=datetime.now() # date.today()
#print(arve_nr)
#tsekk="Arve: "+str(arve_nr)+"\nToode  Hind  Kogus  Summa\n"
#summa=0
#tooded=["Piim","Leib","Komm"] #index 0-1-2
#for i in range(3): #i=0,i=1,i=2
#    toode=tooded[i]
#    hind=randint(50,150)/100
#    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
#    if v=="jah":
#        mitu=int(input("Mitu?"))
#        tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#        summa+=mitu*hind

#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)

#list = [1,2,3,4,5,6,7,8,9,10,11]
#for i in range(11):

#    print("text", i)

##7
#from random import *

#for i in range(5):
#    number = randint(0, 9)
#    print(number, end=".")


#for test in range(1,101):
#    if test % 5 == 0:
#        print(test, end = " ")

#p1 = 0
#p2 = 0
#for i in range(2, 101):
#    if i % 2 == 0:
#        print(f"(i)-paaris")
#        p1+=1
#    else:
#        print(f"(i)-paaritu")
#        p2+=1


#for test in range(1,11):
#    q = input("Угадай число 1-10")
#    if q == test:
#        print("угадал!")
#    else:
#        print("не угадал!")

#11
#import random

#def arva_arv():
#    arvuti_arv = random.randint(1, 10)  
#    katsete_arv = 0

#    while katsete_arv < 3:
#        kasutaja_arvamus = int(input("Угадайте число от 1 до 10: "))

#        if kasutaja_arvamus == arvuti_arv:
#            print("Правильно! Поздравляю вас!")
#            break
#        else:
#            katsete_arv += 1
#            if katsete_arv < 3:
#                print("Неправильно. Попробуйте еще раз!")
#            else:
#                print(f"К сожалению, вы не угадали. Правильное число было {arvuti_arv}.")

#                jätkamise_küsimus = input("Хотите попробовать еще раз? (да/нет): ")
#                if jätkamise_küsimus.lower() == "да":
#                    arvuti_arv = random.randint(1, 10)
#                    katsete_arv = 0
#                else:
#                    print("Спасибо за игру! Хорошего вам дня!")
#                    break
 
#if __name__ == "__main__":
#    arva_arv()

#print("Arv ruut kuup")
#print()
#print()
#print()

#for i in range(1,11):
#    ruut = i ** 2
#    kuup = i ** 2
#    print(f"{i:2} {ruut:2} {kuup:3}")


from random import *
from datetime import *

summa = float(input("Напишите какую сумму вы хотите положить"))
test_summa = summa
procent = randint(1,10)
print("Ты сделал взнос", summa, "Твой процент равен", procent)

howmanyear = int(input("На сколько лет"))
for i in range(1, howmanyear+1):
    intsumma = (summa + procent) 
    test_summa = summa + intsumma
    print(f"{i} {summa} {intsumma} {test_summa}" )
    summa + test_summa
print(f"Сумма итог: {test_summa} eur")
print(f"Выгода: {test_summa - summa} eur" )