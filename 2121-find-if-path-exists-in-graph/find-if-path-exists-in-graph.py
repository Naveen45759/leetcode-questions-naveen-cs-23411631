class Solution:
    def validPath(self, n, edges, source, destination):

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            if node == destination:
                return True

            visited[node] = True

            for neighbour in graph[node]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True

            return False

        return dfs(source)

