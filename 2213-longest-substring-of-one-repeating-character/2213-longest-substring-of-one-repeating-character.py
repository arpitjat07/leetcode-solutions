class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)

        size = 4 * n
        left = [0] * size
        right = [0] * size
        best = [0] * size

        def build(node, l, r):
            if l == r:
                left[node] = right[node] = best[node] = 1
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            pull(node, l, r)

        def pull(node, l, r):
            mid = (l + r) // 2
            a = node * 2
            b = a + 1

            left[node] = left[a]
            right[node] = right[b]
            best[node] = max(best[a], best[b])

            if s[mid] == s[mid + 1]:
                best[node] = max(best[node], right[a] + left[b])

                if left[a] == mid - l + 1:
                    left[node] += left[b]

                if right[b] == r - mid:
                    right[node] += right[a]

        def update(node, l, r, idx):
            if l == r:
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx)
            else:
                update(node * 2 + 1, mid + 1, r, idx)

            pull(node, l, r)

        build(1, 0, n - 1)

        ans = []

        for idx, ch in zip(queryIndices, queryCharacters):
            s[idx] = ch
            update(1, 0, n - 1, idx)
            ans.append(best[1])

        return ans