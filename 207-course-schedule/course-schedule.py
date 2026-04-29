from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Step 1: graph + indegree
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # Step 2: queue for 0 indegree
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # Step 3: process
        count = 0
        while q:
            course = q.popleft()
            count += 1
            
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        # Step 4: check
        return count == numCourses