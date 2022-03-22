import IPet

class Ant(IPet):
  def __init__(self):
    self.stats = [2,1]
  
  #operator is going to contain the shop, team and board. 

  def modifyStats(self, dmgAmt, hlthAmt, isPerm):
    if isPerm:
      self.stats[0] += dmgAmt
      self.stats[1] += hlthAmt
    else:
      pass
      #need to figure out some routine for temporary stats

  def doAbility(self, key, operator):
    pass

  
  def getStats(self):
    pass

   
  def getLevel(self):
    pass
  
   
  def onEat(self):
    pass
   
  def onFaint(self):
    pass

   
  def onLevelUp(self):
    pass

   
  def onBuy(self):
    pass

   
  def onSell(self):
    pass
