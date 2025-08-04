nuns=[1,2,3,5]
result=0
for i in range(4):
    for j in range(i+1,4):
        if nuns[i]==nuns[j]:
            result=1

if result==0:
    print(False)
if result==1:
    print(True)