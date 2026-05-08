class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        wordSet.add(beginWord)
        indegree = defaultdict(set)

        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                indegree[pattern].add(word)

        q = deque([beginWord])
        visited = set([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for w in indegree[pattern]:
                        if w not in visited:
                            visited.add(w)
                            q.append(w)
            res += 1
        return 0
                