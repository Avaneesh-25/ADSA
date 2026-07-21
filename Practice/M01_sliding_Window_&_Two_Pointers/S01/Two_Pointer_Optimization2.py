from typing import List
def removeElement(nums: List[int], val: int) -> int:
        i = 0
        for j in range(0,len(nums)):
            if nums[j] != val:
                
                nums[i] = nums[j]
                i += 1
                
        return i   

nums = [0,0,1,1,1,2,2,3,3,4]
val = 1
print(removeElement(nums, val))