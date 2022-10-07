import os
import time
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1
Win=1
Draw=-1
stop=1
Running=0
Game=Running
def drawBoard():       #drawing the board or functions that print's the board
    print("%c | %c | %c" % (board[1],board[2],board[3]))
    print(" _| _ |_")
    print("%c | %c | %c" % (board[4], board[5], board[6]))
    print(" _| _ |_")
    print("%c | %c | %c" % (board[7], board[8], board[9]))
def checkwin():        #checking weather player as win the game or not
    global Game
    # Horizontal winning condition
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
        # Vertical Winning Condition
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
        # Diagonal Winning Condition
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game = Win
        # Match Tie or Draw Condition
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running

def checkpos(x):  #check weather the choice which player made is empty or not
    if(board[x]==" "):
        return  True
    else:
        return False
def display():  #this function just display the loading effects
    print("plzz waite", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")
    time.sleep(2)
print("welcome to tic toe board")
print("player[1]-->X   player[2]---->O")
print()
display() #calling the function of loading effects
print()
while(Game==Running):        #runing till player win or player draw
    # os.system('cls')
    drawBoard()
    if(player % 2 !=0):
        print("player 1 chance")
        Mark="X"
    else:
        print("player 2 chance")
        Mark="O"
    choice=int(input("enter the pos where you want to fill "))      #player input of choice 1 to 9
    if(checkpos(choice)):
        board[choice]=Mark
        player+=1
        checkwin()
# os.system('cls')
drawBoard()
if(Game==Draw):     #display the message when draw
    print("Game is draw")
elif (Game==Win):   #display the message when player win
    player-=1
    if(player%2!=0):
        print("player 1 won!!")
    else:
        print("player 2 won!!")



