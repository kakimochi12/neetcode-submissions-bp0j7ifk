class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {i:set() for w in words for i in w}
        indegree = {c:0 for c in adj}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        indegree[w2[j]] += 1
                        adj[w1[j]].add(w2[j])
                    break
        
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(indegree) != len(res):
            return ""
        return "".join(res)            
                        
