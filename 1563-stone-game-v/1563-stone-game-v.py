class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        left_best = [[0] * n for _ in range(n)]
        right_best = [[0] * n for _ in range(n)]

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        def get_sum(l, r):
            return prefix[r + 1] - prefix[l]

        for i in range(n - 1, -1, -1):
            k = i - 1

            for j in range(i + 1, n):
                while (
                    k + 1 < j
                    and get_sum(i, k + 1) <= get_sum(k + 2, j)
                ):
                    k += 1

                best = 0

                if k >= i:
                    best = left_best[i][k]

                if k < i:
                    best = max(best, right_best[i + 1][j])
                else:
                    if get_sum(i, k) == get_sum(k + 1, j):
                        start = k + 1
                    else:
                        start = k + 2

                    if start <= j:
                        best = max(best, right_best[start][j])

                dp[i][j] = best

                total = get_sum(i, j)

                left_best[i][j] = max(
                    left_best[i][j - 1],
                    total + dp[i][j]
                )

                right_best[i][j] = max(
                    right_best[i + 1][j],
                    total + dp[i][j]
                )

        return dp[0][n - 1]