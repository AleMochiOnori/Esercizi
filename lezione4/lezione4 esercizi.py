def move_zeros(nums : list[int]):
    for a in range(len(nums)):
        if nums[a] == 0 :
            nums.append(nums.pop(a))
    return nums

print(move_zeros([0,4,3,0,2,0,4]))    




def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    newList = []
    for a in nums1 :
        if a in nums2 and a not in newList:
            newList.append(a)
    return newList



print(intersection([1,2,4,65,4],[5,2,5,2,1,9,8]))    

d = [10 , 3 , 4]
