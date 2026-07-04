class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        frequency = {}
        max_freq = 0
        ans = 0

        for i in range(len(s)):

            # update frequency map to account for new character
            if not s[i] in frequency:
                frequency[s[i]] = 1
            else:
                frequency[s[i]] += 1

            # check what the maximum amount of letter is
            max_freq = max(max_freq, frequency[s[i]]) 

            # check if we have enough characters to cover the entire window
            if not (i - l + 1) - max_freq <= k:
                # decrease frequency of current left letter and increase left pointer
                frequency[s[l]] -= 1
                l += 1

            ans = max(ans, i - l + 1)

                

        return ans
        