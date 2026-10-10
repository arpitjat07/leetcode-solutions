class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        from collections import Counter

        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        freq = Counter(diff)
        max_d = max(diff)

        for d in range(max_d, 0, -1):
            count = freq[d]
            if count == 0:
                continue

            if k >= count:
                k -= count
                freq[d - 1] += count
                freq[d] = 0
            else:
                q, r = divmod(k, count)
                freq[d] -= count
                freq[d - q] += count - r
                if r:
                    freq[d - q - 1] += r
                k = 0
                break

        return sum(d * d * count for d, count in freq.items())