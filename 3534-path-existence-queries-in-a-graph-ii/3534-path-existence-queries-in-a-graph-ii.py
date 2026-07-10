from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:
        pairs = sorted((x, i) for i, x in enumerate(nums))
        pos = [0] * n
        for p, (_, i) in enumerate(pairs):
            pos[i] = p

        nxt = [0] * n
        r = n - 1
        for l in range(n - 1, -1, -1):
            while pairs[r][0] - pairs[l][0] > maxDiff:
                r -= 1
            nxt[l] = r

        LOG = n.bit_length()
        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            if nums[u] == nums[v]:
                ans.append(1)
                continue

            if nums[u] > nums[v]:
                u, v = v, u

            cur = pos[u]
            target = nums[v]
            steps = 0

            for k in range(LOG - 1, -1, -1):
                nxt_pos = up[k][cur]
                if pairs[nxt_pos][0] < target:
                    cur = nxt_pos
                    steps += 1 << k

            if pairs[up[0][cur]][0] < target:
                ans.append(-1)
            else:
                ans.append(steps + 1)

        return ans