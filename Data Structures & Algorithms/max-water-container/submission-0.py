class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0

        i = 0
        j = len(heights) - 1

        while i < j:
            curr_area = (j - i) * min(heights[i], heights[j])
            
            if curr_area > curr_max:
                curr_max = curr_area

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return curr_max
    