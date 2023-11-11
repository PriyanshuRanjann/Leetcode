from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0 
        i = 0
        
        
        for num in nums:
            if num != val:
                nums[i] = num  
                count += 1
                i += 1  

        return count  

