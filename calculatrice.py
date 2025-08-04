import time
a,b=float(input("ecrire a: \n")),float(input("ecrire b: \n"))

c=str(input("ecrire c: \n"))
while c != "-" and c != "+" and c != "*" and c != "/":
    print("_____________error - + / * _____________")
    c=str(input("ecrire c: \n"))

if c=="-":
    d=a-b
    print(a,"-",b,"=",d)
if c=="+":
    d=a+b
    print(a,"+",b,"=",d)
if c=="*":
    d=a*b
    print(a,"*",b,"=",d)
if c=="/":
    if b==0:
        print("impossible")
    if b!=0:
        d=a/b
        print(a,"/",b,"=",d)


time.sleep(12)