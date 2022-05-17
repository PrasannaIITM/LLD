from entities.game import Game

gameBuilder = Game.builder()

print("Enter player 1 name :", end = " ")
player1Name = input().strip()
print()

print("Enter player 1 character(default = X) :", end = " ")
player1Char = input().strip()
if len(player1Char) == 0:
    player1Char = "X"
print()
gameBuilder.addPlayer1(player1Name, player1Char)


print("Enter player 2 name :", end = " ")
player2Name = input().strip()
print()

print("Enter player 2 character(default = O) :", end = " ")
player2Char = input().strip()
if len(player2Char) == 0:
    player2Char = "O"
print()
gameBuilder.addPlayer2(player2Name, player2Char)

print("Enter size of the board", end = " ")
size = int(input())
gameBuilder.setSize(size)

game = gameBuilder.build()

while game.gameState == "LIVE":
    game.printBoard()
    print(game.nextTurnPrompt())
    print("Enter Box :", end = " ")
    box = input().strip()
    game.play(box)

print("Final Board")
game.printBoard()

