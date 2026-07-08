class Solution:
    def divisibleGame(self, nums):
        MOD = 10**9 + 7

        candidates = {2}

        for x in nums:
            d = 2
            while d * d <= x:
                if x % d == 0:
                    candidates.add(d)
                    candidates.add(x // d)
                d += 1
            if x > 1:
                candidates.add(x)

        bestDiff = -10**18
        bestK = 2

        for k in sorted(candidates):
            cur = -10**18
            best = -10**18

            for x in nums:
                val = x if x % k == 0 else -x

                if cur < 0:
                    cur = val
                else:
                    cur += val

                if cur > best:
                    best = cur

            if best > bestDiff:
                bestDiff = best
                bestK = k
            elif best == bestDiff and k < bestK:
                bestK = k

        return (bestDiff * bestK) % MOD