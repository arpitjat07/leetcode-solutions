from bisect import bisect_left, bisect_right

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        s = 0
        for num in nums:
            s += num
            prefix.append(s)

        def sort(lo, hi):
            if hi - lo <= 1:
                return 0

            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)

            j = k = mid
            for left in prefix[lo:mid]:
                while k < hi and prefix[k] - left < lower:
                    k += 1
                while j < hi and prefix[j] - left <= upper:
                    j += 1
                count += j - k

            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        return sort(0, len(prefix))