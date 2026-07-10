class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev2 = prev1 = 0

            for num in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + num)

            return prev1

        return max(helper(nums[:-1]), helper(nums[1:]))