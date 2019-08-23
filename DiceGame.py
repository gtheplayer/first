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
        if(num1 == self.boardList[pos] or num2 == self.boardList[pos] or num3 == self.boardList[pos] or num1+num2 == self.boardList[pos] or num2+num3 ==self.boardList[pos] or num1+num3 ==self.boardList[pos])
        self.pos += 1
        return True
class Game :
    def __init__ (self, numPlayers)
            

    
    
