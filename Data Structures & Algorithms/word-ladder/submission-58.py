class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        wordSet.add(beginWord)
        nei = defaultdict(set)
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].add(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        LIS = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return LIS
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for w in nei[pattern]:
                        if w not in visited:
                            visited.add(w)
                            q.append(w)
            LIS += 1
        return 0
                
        


