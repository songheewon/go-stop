import random
import Card # cards 변수를 사용하기 위함


class Deck(list):
    # 카드를 섞기 전 상태의 디폴트는 cards 상태 1~12월 순
    def __init__(self, before_shuffle=Card.cards):
        super(Deck, self).__init__(before_shuffle)

    # 카드를 섞는 함수
    def cardShuffle(self):
        random.shuffle(self)

    def __hash__(self):
        return hash(self)