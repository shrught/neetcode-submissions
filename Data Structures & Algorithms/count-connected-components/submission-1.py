class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        def dfs(node):

            visited[node] = True

            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)


        res = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                res += 1

        return res

                