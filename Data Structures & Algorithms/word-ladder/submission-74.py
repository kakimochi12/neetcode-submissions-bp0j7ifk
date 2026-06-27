class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        wordSet.add(beginWord)
        indegree = defaultdict(list)

        for w in wordSet:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                indegree[pattern].append(w)
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in indegree[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        return 0