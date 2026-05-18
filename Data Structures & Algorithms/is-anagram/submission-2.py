class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        save = {}
        if len(s) == len(t):
            for l in s:
                if l in save:
                    save[l] += 1
                else:
                    save[l] = 1
            for c in t:
                if c in save:
                    save[c] -= 1
                else:
                    return False
        for i in save.values():
            if i != 0:
                return False
        else:
            return True
