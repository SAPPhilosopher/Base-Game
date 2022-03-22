from abc import ABCMETA, abstractmethod

class PetI(metaclass= ABCMETA):

  @abstractmethod
  def __init__(self):
    pass

  #operator is going to contain the shop, team and board. 
  @abstractmethod
  def doAbility(self, key, operator):
    pass

  @abstractmethod
  def getStats(self):
    pass

  @abstractmethod
  def getLevel(self):
    pass
  
  @abstractmethod
  def onEat(self):
    pass
  @abstractmethod
  def onFaint(self):
    pass

  @abstractmethod
  def onLevelUp(self):
    pass

  @abstractmethod
  def onBuy(self):
    pass

  @abstractmethod
  def onSell(self):
    pass
