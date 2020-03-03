def duplicate(nums):
    nums.sort()
    duplicates=[]
    for i in range (1, len(nums)):
        if nums[i] == nums[i-1]:
            value=nums[i]
            duplicates.append(value)
    return duplicates
print(duplicate([2,4,6,2,3,1,3]))