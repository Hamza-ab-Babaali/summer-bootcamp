import random
user_reponse=[]

def repenses(user_reponse):
    je=input("je ")
    user_reponse.append(je)
    tu=input("tu ")
    user_reponse.append(tu)
    il=input("il ")
    user_reponse.append(il)
    nous=input("nous ")
    user_reponse.append(nous)
    vous=input("vous ")
    user_reponse.append(vous)
    ils=input("ils ")
    user_reponse.append(ils)
    
verbes_choices=["manger","courir","parler","écouter","écrire","lire","chanter","dormir","travailler","jouer"]
verbes=random.choice(verbes_choices)
print("conjuguer le verbe ",verbes,":")

repenses(user_reponse)


corect=['mange', 'manges','mange','mangeons', 'mangez', 'mangent']
user_incorects=[]


if user_reponse[0]!=corect[0]:
    user_incorects.append("je")
if user_reponse[1]!=corect[1]:
    user_incorects.append("tu")
if user_reponse[2]!=corect[2]:
    user_incorects.append("il")
if user_reponse[3]!=corect[3]:
    user_incorects.append("nous")
if user_reponse[4]!=corect[4]:
    user_incorects.append("vous")
if user_reponse[5]!=corect[5]:
    user_incorects.append("ils")

while user_incorects.count!=0:
    user_reponse=[]
    print("vous aver des fautes dans : ")

    print(user_incorects)
    user_incorects=[]

    je=input("je ")
    user_reponse.append(je)
    tu=input("tu ")
    user_reponse.append(tu)
    il=input("il ")
    user_reponse.append(il)
    nous=input("nous ")
    user_reponse.append(nous)
    vous=input("vous ")
    user_reponse.append(vous)
    ils=input("ils ")
    user_reponse.append(ils)
    if user_reponse[0]!=corect[0]:
        user_incorects.append("je")
    if user_reponse[1]!=corect[1]:
        user_incorects.append("tu")
    if user_reponse[2]!=corect[2]:
        user_incorects.append("il")
    if user_reponse[3]!=corect[3]:
        user_incorects.append("nous")
    if user_reponse[4]!=corect[4]:
        user_incorects.append("vous")
    if user_reponse[5]!=corect[5]:
        user_incorects.append("ils")