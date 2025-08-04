
def hm():

    ransomnote = "rat" 
    magazine = "car"

    hashmap={}
    for c in magazine:
        if c in hashmap:
            hashmap[c]+=1
        else :
            hashmap[c]=1


    print(hashmap)

    hashmapD={}
    for c in ransomnote:
        if c in hashmapD:
            hashmapD[c]+=1
        else :
            hashmapD[c]=1


    print(hashmapD)
    if hashmapD==hashmap:
        return True
    else : 
        return False 
print(hm())