class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r = 0
        c = 0
        for row in board:
            if row.count("R") > 0:
                c = row.index("R")
                break
            r += 1

        pawns = 0

        row = board[r]
        #look left
        for i in range(c-1, -1, -1):
            print(row[i])
            if row[i] == "B" or row[i] == "R":
                break
            if row[i] == "p":
                pawns += 1
                break

        #look right
        print("looking right")
        for i in range(c+1, 8):
            print(row[i])
            if row[i] == "B" or row[i] == "R":
                break
            if row[i] == "p":
                pawns += 1
                break
    
        #look up the board
        print("looking up the board")
        for i in range(r-1, -1, -1):
            if board[i][c] == "p":
                pawns += 1
                break
            if board[i][c] == ".":
                continue
            if board[i][c] == "B" or row[i] == "R":
                break
            
        #look down the board
        print("looking down the board")
        for i in range(r+1, 8):
            if board[i][c] == "p":
                pawns += 1
                break
            if board[i][c] == ".":
                continue
            if board[i][c] == "B" or row[i] == "R":
                break
            
        return pawns