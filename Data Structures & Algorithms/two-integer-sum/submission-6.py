class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = {}

        for i, n in enumerate(nums):
            mappings[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mappings and mappings[diff] != i:
                return [i, mappings[diff]]

        return []
        