from .Cards import CardsOnHand, CardsMatched
from .util import _
from .Turn import TurnStart, TurnMiddle, TurnDecision, TurnEnd
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
            if isinstance(current, TurnStart):
                response = input(_(u"=================================== 현재 손에서 내려놓을 패를 고릅니다 ===================================\n{0}").format(
                    '\n'.join(u'{0}번째 선택지: {1}'.format(
                        idx, str(action))
                              for idx, action in enumerate(can_do))))
                print("=======================================================================================================")
                if response in (str(n) for n in range(0, len(can_do))):
                    return can_do[int(response)]

            elif isinstance(current, TurnMiddle):
                response = input(_(u"======================================== 뒤집은 패를 내려놓습니다 ========================================\n{0}").format(
                    '\n'.join(u'{0}번째 선택지: {1}'.format(
                        idx, str(action))
                              for idx, action in enumerate(can_do))))
                print("=======================================================================================================")
                if response in (str(n) for n in range(0, len(can_do))):
                    return can_do[int(response)]

            elif isinstance(current, TurnDecision):
                response = input(_(u"================================= GO 또는 STOP을 외칩니다 =================================\n{0}").format(
                    '\n'.join(u'{0}번째 선택지: {1}'.format(
                        idx, str(action))
                              for idx, action in enumerate(can_do))))
                print("=======================================================================================================")
                if response in (str(n) for n in range(0, len(can_do))):
                    return can_do[int(response)]
            elif isinstance(current, TurnEnd):
                print(current.winner)
                break


class ComputerPlayer(Player):
    def get_action(self, current, can_do):
        ret = random.choice(can_do)
        if isinstance(current, TurnStart):
            print("=================================== 현재 손에서 내려놓을 패를 고릅니다 ===================================")
        return ret
