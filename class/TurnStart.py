import Game
import CardsMatched
import CardsOnTable
import CardsOnHand

class TurnStart(Game):
    def matchCards(self): # player의 손에 있는 패와 바닥 패 짝을 맞춰주는 함수
        can_match_cards=[] # 내면 바닥패와 맞출 수 있는 카드 리스트
        for card in self.player_hand[self.current_player]: # player 손에 있는 카드를 하나씩 검사
            pairs=self.cards_on_table.CardsOnTable.getPair(card) # 테이블 위에서 현재 맞출 수 있는 카드들
            if pairs: # 맞출 수 있는 카드가 1장 이상이라면
                for pair in pairs:
                    can_match_cards.append([card, pair]) # [낼 카드, 맞출 수 있는 카드] 형식으로 저장
            else: # 맞출 수 있는 카드가 없다면
                can_match_cards.append([card, None]) # [낼 카드, None] 형식으로 저장
        return can_match_cards

