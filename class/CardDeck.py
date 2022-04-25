import Card # cards 변수를 사용하기 위함
import random

class CardDeck(list):
    def __init__(self, before_shuffle=Card.cards):
        super(CardDeck, self).__init__(before_shuffle)

    # 카드를 섞는 함수
    def cardShuffle(self):
        random.shuffle(self)

    def __hash__(self):
        return hash(self)