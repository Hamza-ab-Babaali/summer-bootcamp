def self():
    nums1 = [2,2]
    nums2 = [2,1,2]
    result=[]

    hashset=set()
    for i in range(len(nums2)):
        hashset.add(nums2[i])

    print(hashset)
    
    for j in range(len(nums1)):
        if nums1[j] in hashset:
            result.append(nums1[j])
            hashset.remove(nums1[j])



    return result

















print(self())