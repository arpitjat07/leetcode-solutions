class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        last = [-1] * m
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        ans = []
        j = 0
        mismatch = True

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif mismatch and (j == m - 1 or i < last[j + 1]):
                ans.append(i)
                j += 1
                mismatch = False

        return ans if j == m else []