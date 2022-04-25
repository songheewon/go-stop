import Cards


class CardsOnTable(Cards):
    def getPair(self, card): # 짝 맞는 것들 찾아주는 함수
        pair = []
        for match_card in self.cards:
            if match_card.month == card.month:
                pair.append(match_card)
        return pair