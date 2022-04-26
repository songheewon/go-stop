import Turn
import TurnMiddle
import CardAction


class TurnStart(Turn):  # 턴 시작 상태 (1단계)
    def matchCards(self):  # player의 손에 있는 패와 바닥 패 짝을 맞춰주는 함수
        can_match_cards = []  # 내면 바닥패와 맞출 수 있는 카드 리스트
        for card in self.player_hand[self.current_player]:  # player 손에 있는 카드를 하나씩 검사
            pairs = self.cards_on_table.CardsOnTable.getPair(card)  # 테이블 위에서 현재 맞출 수 있는 카드들
            if pairs:  # 맞출 수 있는 카드가 1장 이상이라면
                for pair in pairs:
                    can_match_cards.append(CardAction(card, pair))  # [낼 카드, 맞출 수 있는 카드] 형식으로 저장
            else:  # 맞출 수 있는 카드가 없다면
                can_match_cards.append(CardAction(card, None))  # [낼 카드, None] 형식으로 저장
        return can_match_cards

    def afterMatching(self, card_action):
        current = TurnMiddle(prev_turn=self)
        if card_action is not None: # 낼 카드가 있다면
            current.player_hand[current.current_player].remove(card_action.card) # 손에 있던 카드 제거
            if card_action.pair is not None: # 짝 카드가 있다면
                current.cards_on_table.remove(card_action.pair) # 그 카드를 바닥 패에서 제거
            else: # 짝 카드가 없다면
                current.cards_on_table += card_action.card # player가 내려놓은 카드 바닥 패에 추가
        current.top_deck_card = current.deck.pop()
        return current
