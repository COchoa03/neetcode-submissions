class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = 0
        result = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in result:
                return [result[complement], i]
            else:
                result[num] = i
        