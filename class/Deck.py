import random
import Card


class Deck(list):
    # prev_card를 추가한 이유는 한 턴이 종료되더라도 덱은 그대로 유지되어야 하기 때문에!!!
    # 덱이 변경되는 시점은 새 게임을 시작했을 때뿐임
    def __init__(self, prev_card=Card.cards):
        super(Deck, self).__init__(prev_card)

    # 카드를 섞는 함수
    def cardShuffle(self):
        random.shuffle(self)

    def __hash__(self):
        return hash(self)