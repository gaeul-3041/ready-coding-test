def solution(info, edges):
    answer = 0
    visited = [0] * len(info)
    
    def dfs(sheep, wolf):
        nonlocal answer
        if sheep <= wolf:
            return
        else:
            answer = max(answer, sheep)
            
        for parent, child in edges:
            if visited[parent] == 1 and visited[child] == 0:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[child] = 0
                
    visited[0] = 1
    dfs(1, 0)
    
    return answer