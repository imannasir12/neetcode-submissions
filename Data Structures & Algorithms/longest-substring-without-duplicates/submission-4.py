class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        mappings = {}

        max_length = 0
        curr_length = 0

        while r < len(s):
            if s[r] not in mappings or mappings[s[r]] == 0: 
                mappings[s[r]] = 1
                curr_length = r - l + 1
                max_length = max(max_length, curr_length)
            else: 
                mappings[s[r]] += 1
                
                while s[l] != s[r]:
                    mappings[s[l]] -= 1
                    l += 1
                mappings[s[l]] -= 1
                l += 1
                curr_length = r - l + 1
                max_length = max(max_length, curr_length)   
            r += 1
        return max_length