class Solution:
    def solveSudoku(self, board):
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

       
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r//3)*3 + c//3].add(num)

        def backtrack(r, c):
            if r == 9:
                return True
            
            if c == 9:
                return backtrack(r + 1, 0)
            
            if board[r][c] != ".":
                return backtrack(r, c + 1)
            
            for num in "123456789":
                box_id = (r//3)*3 + c//3
                
                if num in rows[r] or num in cols[c] or num in boxes[box_id]:
                    continue
                
                
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_id].add(num)

                if backtrack(r, c + 1):
                    return True
                
                
                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_id].remove(num)
            
            return False

        backtrack(0, 0)