def valid_solution(board):
    # check 1: horizontal check
    for row in board:
        if not sorted(row) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    
    # check 2: vertical check
    for col in range(len(board)):
        entire_col = [x[col] for x in board]
        if not sorted(entire_col) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    
    # check 3: inside square
    for x in range(1, 10):
        start_col = ((x % 3) - 1) * 3
        if x <= 3:
            start_row = 0
        elif x > 3 and x <= 6:
            start_row = 3
        else:
            start_row = 6
        
        square = list()
        for a in range(3):
            for b in range(3):
                square.append(board[start_row + a][start_col + b])
        if not sorted(square) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]))