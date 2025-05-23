
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
def removeDuplicates(nums):
        left = 0
        right = left+1
        while right<len(nums):
            if nums[right]!=nums[left]:
                left+=1
                nums[left]=nums[right] 
            right+=1
        return left+1


print(removeDuplicates([1,1,2])) # 2 is the length of the this array
print(removeDuplicates([1,3,6,7,7])) # 4 is the length of the this array