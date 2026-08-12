class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        suffix = {}
        results = []

        for index, num in enumerate(nums):
            if not index - 1 in prefix:
                prefix[index] = 1
            else:
                prefix[index] = nums[index - 1] * prefix[index - 1]

        for index in range(len(nums) - 1, -1, -1):
            num = nums[index]
            if not index + 1 in suffix:
                suffix[index] = 1
            else:
                suffix[index] = nums[index + 1] * suffix[index + 1]
        
        for i in range(len(nums)):
            results.append(prefix[i] * suffix[i])
        
        return results