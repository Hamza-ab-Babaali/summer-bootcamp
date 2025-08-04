off=False

# create dictionnaire

mydict={}

# create new user  إنشاء الحساب
def create():
    key=input("entrer your number :")
    value=input("entrer your value :")
    mydict[key]=value


# Check Balance وظيفة التحقق من الرصيد

def getbalance():
    yourvalue=str(input("entrer your account number :"))
    print(mydict[yourvalue])

# Withdraw  وظيفة السحب

def Withdraw():
    yourvalue=input("entrer your account number :")
    money=int(input("entrer amount to Withdraw :"))
    mydict[yourvalue] = int(mydict[yourvalue])
    mydict[yourvalue]-=money
    print("you Withdraw ",money, "dh and you have now in the bank :" ,mydict[yourvalue])

# Deposit  وظيفة الإيداع
 
def deposit():
    yourvalue=input("entrer your account number :")
    money=int(input("entrer amount to deposit :"))
    mydict[yourvalue] = int(mydict[yourvalue])
    mydict[yourvalue]+=money
    print("you deposit your ",money)

while(off==False):
    print("___________________________")
    print(" 0 - exit ")
    print(" 1 - create new user")
    print(" 2 - Check Balance")
    print(" 3 - Withdraw")
    print(" 4 - Deposit")
    print("_________________________")
    bank=int(input("chose a action to do - \n"))


    if bank==1:
        create()
    if bank==2:
        getbalance()
    if bank==3:
        Withdraw()
    if bank==4:
        deposit()
    if bank==0:
        off=True






