from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            wordSet -= level
            nextLevel = set()

            for word in level:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i + 1:]

                        if newWord in wordSet:
                            nextLevel.add(newWord)
                            parents[newWord].append(word)

                            if newWord == endWord:
                                found = True

            level = nextLevel

        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        if found:
            dfs(endWord, [endWord])

        return res