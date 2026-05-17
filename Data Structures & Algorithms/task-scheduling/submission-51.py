class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        count = [-c for c in count.values()]
        heapq.heapify(count)
        time = 0

        q = deque()
        while count or q:
            time += 1
            if count:
                curr = heapq.heappop(count)
                curr += 1
                if curr != 0:
                    q.append([time + n, curr])
            if q and q[0][0] == time:
                cooled = q.popleft()
                heapq.heappush(count, cooled[1])
        return time