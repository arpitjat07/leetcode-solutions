from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()

        for i, num in enumerate(nums):
            pos = window.bisect_left(num - valueDiff)

            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True

            window.add(num)

            if len(window) > indexDiff:
                window.remove(nums[i - indexDiff])

        return False