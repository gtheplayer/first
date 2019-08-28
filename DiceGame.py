class Die :
    def __init__ (self):
        self.sides = 6
        import random
        self.num = random.randint(1,self.sides)
    def __str__(self) :
        return " number of sides is: " + str(self.sides) + " and the current number is: " + str(self.num) 
    def getnum(self) :
        return self.num
    def roll(self) :
       import random
       self.num = random.randint(1,self.sides)
class Board :
    def __init__ (self) :
        self.boardList = [1,2,3,4,5,6,7,8,9,10,11,12,12,11,10,9,8,7,6,5,4,3,2,1]
        self.pos =0
    def __str__(self):
        return "Board Position is: " + str(self.pos)
    def getpos(self):
        return self.pos
    def didmove(self, num1, num2, num3):
        
        moving = True
        while moving == True:
            tracker = self.pos
            if num1 == self.boardList[self.pos] or num2 == self.boardList[self.pos] or num3 == self.boardList[self.pos] or num1+num2 == self.boardList[self.pos] or num2+num3 ==self.boardList[self.pos] or num1+num3 == self.boardList[self.pos] or num1+num2+num3 == self.boardList[self.pos]:
                self.pos += 1 
            if tracker ==self.pos or self.pos == 11 or self.pos == 23:
                moving = False
        return self.getpos()
class Player:
    def __init__ (self, playerName):
        self.name = playerName
        self.board = Board()
    def __str__ (self) :
        return self.name
    def hasWon (self):
        if self.board.getpos() ==23:
            return True
        return False
        
class Game :
    def __init__ (self, numPlayers):
        self.players = numPlayers
        i =0
        self.playerList = []
        while i < self.players:
            self.playerList.append(Player(input ("Player Name")))
            i+= 1
    def playGame (self):
        die1 = Die()
        die2 = Die()
        die3 = Die()

        gameOver = False
        while gameOver == False:
            i =0
            while i < self.players :
                die1.roll()
                die2.roll()
                die3.roll()
                print (self.playerList[i].__str__() + " rolled " + str(die1.getnum()) + " " + str(die2.getnum()) + " "+ str(die3.getnum()))
                tracker = self.playerList[i].board.getpos()
                if self.playerList[i].board.didmove(die1.getnum(), die2.getnum(), die3.getnum()) != tracker:
                    print (self.playerList[i].__str__() + " is on " + str(self.playerList[i].board.boardList[self.playerList[i].board.getpos()-1]))
                if self.playerList[i].hasWon() == True:
                    print (self.playerList[i].__str__() + " is on " + str(self.playerList[i].board.boardList[self.playerList[i].board.getpos()]))
                    print (self.playerList[i].__str__() + " is Victorious!!!")
                    gameOver = True
                    break
                if self.playerList[i].board.getpos() ==  11 or self.playerList[i].board.getpos() == tracker:
                    print (self.playerList[i].__str__() + " is on " + str(self.playerList[i].board.boardList[self.playerList[i].board.getpos()]))
                    i +=1
                    print ("Next Player's turn")
                
                
                

game1 = Game(2)
game1.playGame()

 
