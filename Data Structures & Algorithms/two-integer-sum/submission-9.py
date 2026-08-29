class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in mappings:
                return [mappings[diff], index]
            else:
                mappings[num] = index