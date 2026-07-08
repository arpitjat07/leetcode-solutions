class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        pre = [-1] * n
        j = 0
        for i in range(n):
            while j < m and t[j] != s[i]:
                j += 1
            if j == m:
                break
            pre[i] = j
            j += 1

        if n > 0 and pre[n - 1] != -1:
            return True

        suf = [-1] * n
        j = m - 1
        for i in range(n - 1, -1, -1):
            while j >= 0 and t[j] != s[i]:
                j -= 1
            if j < 0:
                break
            suf[i] = j
            j -= 1

        for i in range(n):
            left = -1 if i == 0 else pre[i - 1]
            right = m if i == n - 1 else suf[i + 1]

            if left != -1 or i == 0:
                if right != -1 or i == n - 1:
                    if left < right:
                        if right - left >= 2:
                            return True

        return False