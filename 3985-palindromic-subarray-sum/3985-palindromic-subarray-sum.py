class Solution:
    def getSum(self, nums):
        n = len(nums)

        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x

        def range_sum(l, r):
            return pref[r + 1] - pref[l]

        d1 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and nums[i - k] == nums[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1

        d2 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < n and nums[i - k - 1] == nums[i + k]:
                k += 1
            d2[i] = k
            if i + k - 1 > r:
                l = i - k
                r = i + k - 1

        ans = 0

        for i in range(n):
            rad = d1[i]
            l = i - rad + 1
            r = i + rad - 1
            ans = max(ans, range_sum(l, r))

        for i in range(n):
            rad = d2[i]
            if rad > 0:
                l = i - rad
                r = i + rad - 1
                ans = max(ans, range_sum(l, r))

        return ans