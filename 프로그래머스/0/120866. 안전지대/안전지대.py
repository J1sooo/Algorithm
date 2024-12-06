def solution(board):
    answer = 0
    l1=[]
    M = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    for i in range(M):
        for j in range(M):
            if board[i][j]==1:
                l1.append((i,j))
                
    for x,y in l1:
        for j in range(8):
            ax = x+dx[j]
            ay = y+dy[j]
            if 0<=ax<M and 0<=ay<M:
                board[ax][ay]=1
                
    for i in range(M):
        answer+=board[i].count(0)
            
    return answer