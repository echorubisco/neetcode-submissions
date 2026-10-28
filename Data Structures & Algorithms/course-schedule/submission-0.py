class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        locks = [0]*numCourses
        for a,b in prerequisites:
            # must take course b before taking course a
            graph[b].append(a)
            locks[a] += 1
        ready = deque([c for c in range(numCourses) if locks[c] == 0])
        taken = []
        while ready:
            course = ready.popleft()
            taken.append(course)
            for nxt in graph[course]:
                locks[nxt] -= 1
                if locks[nxt] == 0:
                    ready.append(nxt)
        if len(taken) == numCourses:
            return True
        else:
            return False