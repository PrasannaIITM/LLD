from entities.board import Board
from entities.player import Player
BOARD_DEFAULT_SIZE = 3

GAME_STATES = ["LIVE", "END", "DRAW"]

class Game():
    turn = 0
    gameState = "LIVE"

    def __init__(self, p1, p2, board) -> None:
        self.p1 = p1
        self.p2 = p2
        self.board = board

    def printBoard(self):
        self.board.printBoard()
          
    def __checkWinner(self, player):
        char = player.character

        winningString = char*self.board.size

        for row in [chr(ord("A") + i) for i in range(self.board.size)]:
            if self.board.getRowAsString(row) == winningString:
                return True

        for col in range(self.board.size):
            if self.board.getColAsString(col) == winningString:
                return True

        for diag in range(2):
            if self.board.getDiagAsString(diag) == winningString:
                return True

        return False

    def nextTurnPrompt(self):
        if self.turn % 2 == 0:
            player = self.p1
        else:
            player = self.p2

        return f"Turn {self.turn + 1} | Player : {player.name} Character : {player.character}"

    def play(self, box):
        if self.turn % 2 == 0:
            player = self.p1
        else:
            player = self.p2

        try:
            success = self.board.markBoard(box, player.character)
        except Exception as e:
            print(e)
            return
        
        if success:
            if self.__checkWinner(player):
                self.gameState = "END"
                print(f"Game Over! {player.name} is the winner")
                return

            self.turn += 1

        if self.turn == self.board.size*self.board.size:
            self.gameState = "DRAW"
            print("Game ended in DRAW")

    @staticmethod
    def builder():
        return GameBuilder()

class GameBuilder():
    __p1 = None
    __p2 = None
    __size = None

    def addPlayer1(self, name, character = "X"):
        self.__p1 =  Player.builder().setName(name).setCharacter(character).build()
        return self

    def addPlayer2(self, name, character = "O"):
        self.__p2 =  Player.builder().setName(name).setCharacter(character).build()
        return self
    
    def setSize(self, size = BOARD_DEFAULT_SIZE):
        self.__size = size
        return self

    def build(self):
        if not self.__p1:
            raise Exception("Player 1 not created")

        if not self.__p2:
            raise Exception("Player 2 not created")
        
        return Game(self.__p1, self.__p2, Board(self.__size))

