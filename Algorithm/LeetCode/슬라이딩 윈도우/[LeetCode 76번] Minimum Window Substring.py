class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        
        m, n = len(s), len(t)
        
        target = defaultdict(int)
        for char in t:
            target[char] += 1
        
        while n <= m:
            for i in range(m-n+1):
                dummy = target.copy()
                for j in range(n):
                    if s[i+j] in dummy:
                        dummy[s[i+j]] -= 1
                        if not dummy[s[i+j]]:
                            del dummy[s[i+j]]
                    if not dummy:
                        return s[i:i+n]
            n += 1
        else:
            return ""