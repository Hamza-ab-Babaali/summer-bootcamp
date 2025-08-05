import random

def double():
    j=input("you won,",n,"! do you want to try doeble or nothing? guess a number between 1 and 100to double your score!")
    i=random.randrange(1, 100, 1)

    if j==i:
        print("you won!")
    else:
        print("oops! it was",i,". you lost your score!")

"""
#score
d=open("score.txt","r")
m=float(d.read())
print(m)
d.close
m-=1
v=open("score.txt","w")

v.writelines(m)"""



#game logic
n=str(input("what s your name :"))
print("hello",n,"let's play! i'm thinking of a number between 1 and 10")
k=random.choice([1,2,3,4,5,6,7,8,9,10])

haert=3
while(haert != 0):
    h=int(input("guess?"))
    print(n,"guesses",h)
    if h>k:
        print("your number is high!")
    if h<k:
        print("your number is lower!")
    if h==k:
        print("you are correcte!")
        double()
        break
    if h!=k:
        haert-=1
if haert==0:
    print("you lose!!")

print(k)



