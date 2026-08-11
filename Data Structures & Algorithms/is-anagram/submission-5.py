class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for char in s:
            if not char in s_to_t:
                s_to_t[char] = 1
            else:
                s_to_t[char] += 1

        for char in t:
            if not char in t_to_s:
                t_to_s[char] = 1
            else:
                t_to_s[char] += 1

        return s_to_t == t_to_s