from abc import ABCMETA, abstractmethod


class PetI(metaclass=ABCMETA):
    @abstractmethod
    def __init__(self):
        pass

    # operator is going to contain the shop, team and board.
    @abstractmethod
    def do_ability(self, key, operator):
        pass

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def get_level(self):
        pass

    @abstractmethod
    def on_eat(self):
        pass

    @abstractmethod
    def on_faint(self):
        pass

    @abstractmethod
    def on_level_up(self):
        pass

    @abstractmethod
    def on_buy(self):
        pass

    @abstractmethod
    def on_sell(self):
        pass
