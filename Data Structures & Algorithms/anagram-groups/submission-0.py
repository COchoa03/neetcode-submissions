class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        save = {}
        for pal in strs:
            key = "".join(sorted(pal))
            if key in save:
                save[key].append(pal)
            else:
                save[key] = [pal]
        return list(save.values())
        