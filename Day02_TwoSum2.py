def twoSum(numbers, target):
            left,right=0,len(numbers)-1
            while left<right:
                current_sum = numbers[left]+numbers[right]
                if current_sum==target:
                    return [left+1,right+1]
                elif numbers[left]+numbers[right]>target:
                    right-=1
                else:
                    left+=1

print(twoSum([1,2,3,4,5],5))
print(twoSum([2,3,4,5,4],7))