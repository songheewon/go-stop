class CardAction(object):
    def __init__(self, card, pair): # 낸 카드, 짝 카드
        super(CardAction, self).__init__()
        self.card = card
        self.pair = pair
