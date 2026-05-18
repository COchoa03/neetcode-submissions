class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        save = {}
        for num in nums:
            if num in save:
                return True
            else:
                save[num] = num
        return False
        
        