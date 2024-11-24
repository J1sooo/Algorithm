def solution(keyinput, board):
    answer = [0,0]
    xlimit = board[0] // 2
    ylimit = board[1] // 2
    
    for i in keyinput:
        if i=='up' and answer[1]<ylimit:
            answer[1]+=1
        elif i=='down' and answer[1]>-ylimit:
            answer[1]-=1
        elif i=='left' and answer[0]>-xlimit:
            answer[0]-=1
        elif i=='right' and answer[0]<xlimit:
            answer[0]+=1
    return answer