from random import randint

'''
Combat
- Fighting abilities (magic, etc.)
Treasure
Dungeon Walls
- randomly gen
- doors: locked, etc
Boss Monsters
Levels
'''


class Game:
  def __init__(self):
    self.boardWidth = 20
    self.boardHeight = 20
    self.board = []
    self.monsters = []
    self.player = Entity(self.boardWidth//2, self.boardHeight//2, 25, 5, True)
    self.inCombat = False
    
  def drawBoard(self):
    for i in range(len(self.board)):
      print "-"+"-".join(self.board[i])+"-"
    
  def genBoard(self):
    for i in range(self.boardHeight):
      self.board.append([" " for j in range(self.boardWidth)])
      
  def genMonsters(self, amount):
    for i in range(amount):
      x, y = randint(1, len(self.board)-1), randint(1, len(self.board)-1)
      self.monsters.append(Entity(x, y, randint(10, 50), randint(1, 10)))
      self.board[y][x] = "M"
      
  def setUp(self):
    self.genBoard()
    self.genMonsters(5)
    self.board[self.player.y][self.player.x] = "P"
    
  def playerMove(self):
    action = input("\nMove: ")
    if action.lower() == "right":
      if self.player.x < len(self.board[0]):
        self.player.x+=1
      else:
        print "ERROR: Space Non-existent"
        return self.playerMove()
    elif action.lower() == "left":
      if self.player.x > 0: 
        self.player.x-=1
      else:
        print "ERROR: Space Non-existent"
        return self.playerMove()
    elif action.lower() == "up":
      if self.player.y > 0:
        self.player.y-=1
      else:
        print "ERROR: Space Non-existent"
        return self.playerMove()
    elif action.lower() == "down":
      if self.player.y < len(self.board):
        self.player.y+=1
      else:
        print "ERROR: Space Non-existent"
        return self.playerMove()
    else:
      print "ERROR: Command Not Found"
      return self.playerMove()
    
  def monsterMove(self):
    for monster in self.monsters:
      if abs(monster.x-self.player.x) > abs(monster.y - self.player.y):
        if self.player.x > monster.x:
          monster.x+=1
        else:
          monster.x-=1
      else:
        if self.player.y > monster.y:
          monster.y+=1
        else:
          monster.y-=1
          
  def updateBoard(self):
    self.board = []
    self.genBoard()
    for monster in self.monsters:
      self.board[monster.y][monster.x] = "M"
    self.board[self.player.y][self.player.x] = "P"
    
  def proximityCheck(self):
    return (self.player.x < len(self.board[0]) and self.board[self.player.y][self.player.x+1] == "M") or (self.player.y < len(self.board) and self.board[self.player.y+1][self.player.x] == "M") or (self.player.x > 0 and self.board[self.player.y][self.player.x-1] == "M") or (self.player.y > 0 and self.board[self.player.y-1][self.player.x] == "M")
    
  def combat(self, monster):
    pass
    
  def update(self):
    self.inCombat = self.proximityCheck()
    if not self.inCombat:
      self.updateBoard()
      self.drawBoard()
      self.player.displayStats()
      self.playerMove()
      self.monsterMove()
    else:
      pass

class Entity:
  def __init__(self, x, y, health, strength, isPlayer = False):
    self.x = x
    self.y = y
    self.health = health
    self.strength = strength
    self.isPlayer = isPlayer
    
  def displayStats(self):
    if self.isPlayer:
      print "{ PLAYER"
    else:
      print "{ MONSTER"
    print "health: "+str(self.health)
    print "strength: "+str(self.strength)
  
game = Game()
game.setUp()
while True:
  game.update()
