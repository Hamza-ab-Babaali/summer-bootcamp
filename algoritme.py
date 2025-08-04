"""
def fct (nums):

    for i in range(4) :
        for j in range(i+1,4):
            if nums[i]==nums[j]:
                return(True)
                break
    return(False)



t1 = [1,2,3,8]
#print(fct(t1))
t2 = [1,2,3,8]
#print(fct(t2))
def fct2 (nums):

    for i in range(4) :
        for j in range(i+1,4):
            if nums[i]+nums[j]==9:
                return[i,j]
print (fct2(t2))

"""""

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZqBqKulQRiQ?si=DKZCiYj1-g9Ii7I6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>