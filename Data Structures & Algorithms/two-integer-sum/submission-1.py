class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        options = {}

        i = 0
        for num in nums:
            options[num] = i
            i += 1

        i = 0
        for num in nums:
            difference = target - num
            if difference in options and options[difference] != i:
                return [min(options[difference], i), max(options[difference], i)]
            i += 1

        



        