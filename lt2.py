"""
a=[1,2,3]
print(a)
for i in a:
    print(i)
for j in range(len(a)):
    print(a[j])

for k,i in enumerate(a):
    print(a[k])
    

#a.append(4)
#a.append(5)
#print(a)

#a.pop(1)
#print(a)

a.insert(3,2)
print(a)

p=len(a)
print(p)

print()



def foon(a):
    print("hello1")
    print("hello2")
    print("hello2")
    print("hello2")
    print("hello2")
    print("hello2")
    print("hello2")
    print("hello2")
    print("hello2")
    return a*a




print(foon(2))
foon(4)
foon()
foon()
foon()


"""

def anagram(s,t):


    return sorted(t)==sorted(s)



t="nagaram"
s="anagram"

print(anagram(s,t))



def foon(a):
    print("hello1")
    print("hello2")
    return a*a
    return a*2
    return a*2
    return a*2
    return a*2
    return a*2
    return a*2
    return a*2
    return a*a
    return a*a
    return a*a




print(foon(2))