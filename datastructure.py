a=[1,3,5,7,9,3,4,2,8,3]
for i in range (5):
    print(a[i])


a.append(11)
print("append a new item ")
print(a)

a.reverse()
print("reverse the order")
print(a)
print("le nembre du tableau:")
y=1
z=0
while a[z]!=a[-1]:
   y+=1
   z+=1
print(y)

print(" get the number of occurrences of3")
k=0
n=0
while a[k]!=a[-1]:
       n+=1
print(n)