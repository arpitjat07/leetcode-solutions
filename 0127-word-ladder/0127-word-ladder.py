from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        patternMap = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patternMap[pattern].append(word)

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]

                for nei in patternMap[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, steps + 1))

                patternMap[pattern] = []

        return 0