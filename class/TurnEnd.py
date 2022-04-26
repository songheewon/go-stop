import Turn
import TurnStart
import TurnMiddle
import TurnDecision

class TurnEnd(Turn):
    def do_nothing(self):
        return []