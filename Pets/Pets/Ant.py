import IPet


class Ant(IPet):
    def __init__(self):
        self.stats = [2, 1]

    # operator is going to contain the shop, team and board.

    def modify_stats(self, dmg_ant, hlth_amnt, is_perm):
        if is_perm:
            self.stats[0] += dmg_ant
            self.stats[1] += hlth_amnt
        else:
            pass
            # need to figure out some routine for temporary stats

    def do_ability(self, key, operator):
        pass

    def get_stats(self):
        pass

    def get_level(self):
        pass

    def on_eat(self):
        pass

    def on_faint(self):
        pass

    def on_level_up(self):
        pass

    def on_buy(self):
        pass

    def on_sell(self):
        pass
