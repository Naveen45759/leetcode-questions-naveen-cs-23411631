
class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        visited = [0] * n

        def dfs(node):
            if visited[node] == 1:
                return False

            if visited[node] == 2:
                return True

            visited[node] = 1

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            visited[node] = 2
            return True

        ans = []

        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans
