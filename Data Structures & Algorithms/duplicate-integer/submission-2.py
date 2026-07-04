class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        options = set()

        for num in nums:
            if num in options:
                return True
            else:
                options.add(num)

        return False
        