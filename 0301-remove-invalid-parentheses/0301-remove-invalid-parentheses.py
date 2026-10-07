class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left:
                    left -= 1
                else:
                    right += 1

        res = set()

        def dfs(i, path, balance, l, r):
            if i == len(s):
                if balance == 0 and l == 0 and r == 0:
                    res.add(''.join(path))
                return

            ch = s[i]

            if ch == '(':
                if l:
                    dfs(i + 1, path, balance, l - 1, r)
                path.append(ch)
                dfs(i + 1, path, balance + 1, l, r)
                path.pop()

            elif ch == ')':
                if r:
                    dfs(i + 1, path, balance, l, r - 1)
                if balance:
                    path.append(ch)
                    dfs(i + 1, path, balance - 1, l, r)
                    path.pop()

            else:
                path.append(ch)
                dfs(i + 1, path, balance, l, r)
                path.pop()

        dfs(0, [], 0, left, right)
        return list(res)