class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        locks = [0] * numCourses
        prereq = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            prereq[b].append(a)
            locks[a] += 1
        taken = [i for i in range(numCourses) if locks[i] == 0]
        i = 0
        while i < len(taken):
            cur = taken[i]
            i += 1
            for course in prereq[cur]:
                locks[course] -= 1
                if locks[course] == 0:
                    taken.append(course)
        return taken if len(taken) == numCourses else []


