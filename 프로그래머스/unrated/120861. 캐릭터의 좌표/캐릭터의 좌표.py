def solution(keyinput, board):
    f_result = 0
    n_result = 0
    
    for i in range(len(keyinput)):
        if keyinput[i] == 'left' and (f_result) > -(board[0] // 2):
            f_result -= 1
        elif keyinput[i] == 'right' and (f_result) < (board[0] // 2):
            f_result += 1
        elif keyinput[i] == 'up' and (n_result) < (board[1] // 2):
            n_result += 1
        elif keyinput[i] == 'down' and (n_result) > -(board[1] // 2):
            n_result -= 1
    
    result = [f_result, n_result]
    return result
