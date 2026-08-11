class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = {}

        for index, num in enumerate(nums):
            curr_target = target - num
            if curr_target in mappings:
                return [mappings[curr_target], index]

            mappings[num] = index

        