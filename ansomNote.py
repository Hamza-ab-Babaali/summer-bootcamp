
def hm():

    ransomnote = "nagaram" 
    magazine = "anagram"

    hashmap={}
    for c in magazine:
        if c in hashmap:
            hashmap[c]+=1
        else :
            hashmap[c]=1


    print(hashmap)

    for k in ransomnote:
        if k not in hashmap or hashmap[k]==0:
            return False
        elif hashmap[k]==0:
            del hashmap[k]
        else :
            hashmap[k]=hashmap[k]-1
    print(hashmap)

    return True
print(hm())