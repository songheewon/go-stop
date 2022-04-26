import Cards


class CardsOnTable(Cards):
    def get_pair(self, card): # 짝 맞는 것을 찾아주는 함수
        # card는 내가 내고자 하는 카드
        # self.cards는 바닥에 깔린 카드들
        pair = []
        for card_on_table in self.cards:
            if card_on_table.month == card.month: # 월이 일치한다면
                pair.append(card_on_table) # 추가
        return pair