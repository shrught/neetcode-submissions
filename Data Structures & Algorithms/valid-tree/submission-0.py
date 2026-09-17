class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #if edges are more than the number of nodes, there will cycles
        if len(edges) - 1 > n:
            return False

        adj = [[] for _ in range(n)]
        #create the adjacency matrix
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        #dfs detect cycle
        visit = set()
        
        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        #a tree should traverse all the nodes once and only once
        return dfs(0, -1) and len(visit) == n

        