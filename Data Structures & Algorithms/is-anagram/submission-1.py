class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_m = {}
        t_m = {}
        for ls,lt in zip(s,t):
            s_m[ls] = s_m.get(ls,0) + 1
            t_m[lt] = t_m.get(lt,0) + 1
        
        return s_m == t_m