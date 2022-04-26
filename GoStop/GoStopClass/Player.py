from .Cards import CardsOnHand, CardsMatched
from .util import _
import random


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = CardsOnHand()
        self.matched = CardsMatched()
        self.score = 0

    def get_action(self, current, can_do):
        raise NotImplementedError()


class HumanPlayer(Player):
    def get_action(self, current, can_do):
        while True:
            response = input(_(u"== Choose action for {0} {1}? ").format(
                self.name,
                '/'.join(u'({0}){1}'.format(
                    idx, str(action))
                         for idx, action in enumerate(can_do))))
            if response in (str(n) for n in range(0, len(can_do))):
                print(can_do[int(response)])
                return can_do[int(response)]


class ComputerPlayer(Player):
    def get_action(self, current, can_do):
        ret = random.choice(can_do)
        return ret