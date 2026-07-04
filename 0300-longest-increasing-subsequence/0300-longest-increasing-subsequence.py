from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for num in nums:
            idx = bisect_left(lis, num)

            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num

        return len(lis)