def fonctionmax(a,b):
            if a<b :
               print(a,"<",b)
            if a>b :
               print(a,">",b)
            if a==b :
               print(a,"=",b)
#fonctionmax(5,8)
#fonctionmax(6,3)
#fonctionmax(15,15)
#fonctionmax(7,34)
#fonctionmax(4,67)
#fonctionmax(45,67)





def hamza(d):
    print(1)
    return d*d
    print(2)
#c=hamza(6)
#print(c)




#Fonction
def bultane(y):
    note=(y[0]+y[1]+y[2]+y[3])/4
    if note>=12:
        print(True)
    else : print(False)
    return note





#Programe initial
y=[]
print(y)
for i in range(4):
    x=int(input("donne la note :"))
    while x<0 or x>21 :
        print("error : donne la note")
        x=int(input())
    y.append(x)
print(y)
print("___ La fonction de la note ___")
print(bultane(y))