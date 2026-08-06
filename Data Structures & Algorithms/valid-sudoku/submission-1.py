class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols,rows,boxes=defaultdict(set),defaultdict(set),defaultdict(set)
        for c in range(len(board)):
            for r in range(len(board)):
                if board[r][c]=='.':
                    continue
                if (board[r][c] in cols[c]) or (board[r][c] in rows[r]) or (board[r][c] in boxes[(r//3,c//3)]):
                    return False
                else:
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    boxes[(r//3,c//3)].add(board[r][c])
        return True

