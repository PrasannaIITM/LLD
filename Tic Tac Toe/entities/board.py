BOARD_DEFAULT_SIZE = 3

class Board():
    def __init__(self, size = BOARD_DEFAULT_SIZE) -> None:
        self.size = size
        self.grid = [["_" for i in range(self.size)] for i in range(self.size)]
        
    def printBoard(self):
        for row in range(len(self.grid)):
            print(" ".join(self.grid[row]))
        print()

    def markBoard(self, box, character):
        if len(box) != 2:
            raise Exception("Invalid box-id, Try Again!")

        row = ord(box[0]) - ord("A")
        col = ord(box[1]) - ord("0")

        if row >= len(self.grid) or col >= len(self.grid):
            raise Exception("Invalid box-id, Try Again!")

        if self.grid[row][col] != "_":
            raise Exception("Box filled, Try Again!")

        self.grid[row][col] = character
        return True

    def getRowAsString(self, row):
        rowIdx = ord(row) - ord("A")

        if rowIdx < 0 or rowIdx >= len(self.grid):
            raise Exception("Not a valid row")

        return "".join(self.grid[rowIdx])

    def getColAsString(self, col):
        colIdx = col

        if colIdx < 0 or colIdx >= len(self.grid[0]):
            raise Exception("Not a valid col")

        colString = ""
        for i in range(len(self.grid)):
            colString += self.grid[i][colIdx]
        return colString

    def getDiagAsString(self, diag):
        if diag == 0:
            diagString = ""
            for i in range(len(self.grid)):
                diagString += self.grid[i][i] 
            return diagString
        elif diag == 1:
            diagString = ""
            for i in range(len(self.grid)):
                diagString += self.grid[i][len(self.grid) - 1 - i]
            return diagString
        else:
            raise Exception("Not a valid diag")