import math as m
"""
def identité_remarquable(a,b):
    x=pow(a,2)+2*a*b+pow(b,2)
    return x
print(identité_remarquable(3,5))


def suface_circonférence(r,d):
    e=m.pi*pow(r,2)
    s=m.pi*d
    return "suface:",e,"circonférence:",s
print(suface_circonférence(2,2))


def polinome(x,x3,x2,x1,x0):
    p=x3*pow(x,3)+x2*pow(x,2)+x1*pow(x,1)+x0*pow(x,0)
    return p


def calc(x,x3,x2,x1,x0,y,y3,y2,y1,y0):
    cl=polinome(x,x3,x2,x1,x0)/polinome(y,y3,y2,y1,y0)
    return cl

print(calc(1,5,7,0,8,1,0,0,8,-6))

print("entrer a :   ")
a=int(input())

b=int(input("entrer b :   "))

k=a+b

print("la somme de a et b est :",k)
"""

print("لعبة السباق الثلاثي")
m=str(input("ادخل اسم الرياضي"))
n=int(input("ادخل رقم الرياضي"))
s1=int(input("نتيجة رياضة السباحة"))
s2=int(input("تنيجة رياضة ركوب الدراجات"))
s3=int(input("نتيجة رياضة الجري"))
c=(s1+s2+s3)/3
print("متوسط نقاط في لعبة السباق الثلاثي",c)