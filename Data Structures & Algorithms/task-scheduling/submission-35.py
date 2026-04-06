class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        counter = [-c for c in counter.values()]
        heapq.heapify(counter)
        time = 0

        q = deque()
        while q or counter:
            time += 1
            if counter:
                curr = heapq.heappop(counter)
                curr += 1
                if curr != 0:
                    q.append([curr, time + n])
            if q and q[0][1] == time:
                cooled = q.popleft()
                heapq.heappush(counter, cooled[0])
        return time