class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i, total):
            if total == target:
                res.append(comb[:])
                return

            if i == len(candidates) or total > target:
                return

            comb.append(candidates[i])
            backtrack(i, total + candidates[i])
            comb.pop()

            backtrack(i + 1, total)

        backtrack(0, 0)
        return res