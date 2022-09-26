class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict 
        adjList = defaultdict(list)
        for s, e in edges:
            adjList[s].append(e)
            adjList[e].append(s)
        maxDepth = {i:0 for i in range(n)}
        visited = [False for _ in range(n)]
        
        def dfs(s, idx, cnt=0):
            flag = 0
            for w in adjList[idx]:
                if not visited[w]:
                    visited[w] = True
                    dfs(s, w, cnt+1)
                    visited[w] = False
                else:
                    flag += 1
                    
            if flag == len(adjList[idx]):
                if maxDepth[s] < cnt:
                    maxDepth[s] = cnt
                return
                
        for i in range(n):
            visited[i] = True
            dfs(i, i)
            visited[i] = False
        
        minV = min(maxDepth.values())
        result = []
        for key, value in maxDepth.items():
            if minV == value:
                result.append(key)
            
        return result