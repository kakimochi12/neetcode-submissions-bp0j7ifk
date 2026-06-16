class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        wordSet.add(beginWord)
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
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
                    for nei in adj[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res += 1
        return 0