class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        w = t + 1
        buckets = {}

        for i, num in enumerate(nums):
            b = num // w

            if b in buckets:
                return True
            if b - 1 in buckets and abs(num - buckets[b - 1]) < w:
                return True
            if b + 1 in buckets and abs(num - buckets[b + 1]) < w:
                return True

            buckets[b] = num

            if i >= k:
                del buckets[nums[i - k] // w]

        return False