from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return max(nums)

        freq = Counter(nums)

        if k == 1:
            return max((x for x in nums if freq[x] == 1), default=-1)

        ans = -1

        if freq[nums[0]] == 1:
            ans = nums[0]

        if freq[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans