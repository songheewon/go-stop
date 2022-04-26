import Turn
import TurnStart
import TurnMiddle
import TurnEnd


class GoStop(object):
    GO = 1
    STOP = 2


class TurnDecision(Turn):  # 턴 마지막 상태 (3단계)
    def get_left_cards(self): # 덱에 남은 카드 수를 리턴
        if len(self.deck) > 0:
            return len(self.deck)
        return 0

    def after_decision(self, action):
        if action == GoStop.GO: # GO를 선택했다면
            current = TurnStart(prev_turn=self) # 다시 턴 변경
            # 흠,,,, 점수 처리를 어떻게 해주지?
        elif action == GoStop.STOP: # STOP을 선택했다면
            current = TurnEnd(prev_turn=self) # 게임 끝을 알리고
            current.winner = self.current_player # 승자 선언
        return current
