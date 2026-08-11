class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = {}

        index = 0
        for num in nums:
            curr_target = target - num
            if curr_target in mappings:
                return [mappings[curr_target], index]

            else:
                mappings[num] = index

            index += 1

