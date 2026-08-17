class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        nonzero = False

        for x in nums:
            xor ^= x
            if x != 0:
                nonzero = True

        if xor != 0:
            return len(nums)

        if not nonzero:
            return 0

        return len(nums) - 1