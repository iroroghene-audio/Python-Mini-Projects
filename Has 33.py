def has_33(nums):

    for item in nums:
        if nums[item] == 3 and nums[item+1] == 3:
            return True
    return False




checker = has_33([1, 3, 2, 4])

print(checker)