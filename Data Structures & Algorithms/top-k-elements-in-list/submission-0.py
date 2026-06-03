class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        save = {}
        for num in nums:
            if num in save:
                save[num] += 1
            elif num not in save:
                save[num] = 1
        pairs = list(save.items())
        pairs = sorted(pairs, key=lambda pair: pair[1], reverse=True)
        result = []
        for num, freq in pairs[:k]:
            result.append(num)
        return result

