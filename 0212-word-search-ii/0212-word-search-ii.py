class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] not in node.children
            ):
                return

            ch = board[r][c]
            nxt = node.children[ch]

            if nxt.word:
                res.append(nxt.word)
                nxt.word = None

            board[r][c] = "#"

            dfs(r + 1, c, nxt)
            dfs(r - 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)

            board[r][c] = ch

            if not nxt.children:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res