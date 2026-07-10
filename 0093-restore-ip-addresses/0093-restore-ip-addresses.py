class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]

                if (part[0] == "0" and len(part) > 1) or int(part) > 255:
                    continue

                path.append(part)
                backtrack(end, path)
                path.pop()

        backtrack(0, [])
        return res