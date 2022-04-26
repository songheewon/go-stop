import Turn
import TurnStart
import CardAction


class TurnMiddle(Turn):
    def matchCards(self): # 바닥 패와 뒤집은 패의 짝을 맞춰주는 함수
        can_match_cards=[] # 뒤집으면 바닥패와 맞출 수 있는 카드 리스트
        pairs=self.cards_on_table.getPair(self.top_card)
        if pairs:
            for pair in pairs:
                can_match_cards.append(CardAction(self.top_card, pair))
        else:
            can_match_cards.append(CardAction(self.top_card, None))
        return can_match_cards

    def afterMatching(self, card_action):
        current=TurnStart(prev_turn=self)
        if card_action is not None:

