class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(t):
            bal = 0
            for ch in t:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        level = {s}

        while level:
            valid = [t for t in level if is_valid(t)]
            if valid:
                return valid

            nxt = set()
            for t in level:
                for i, ch in enumerate(t):
                    if ch not in '()':
                        continue
                    if i > 0 and t[i] == t[i - 1]:
                        continue
                    nxt.add(t[:i] + t[i + 1:])

            level = nxt

        return [""]