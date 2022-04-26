class Pair(object):
    def __init__(self, card, pair): # 낸 카드, 짝 카드
        self.card = card
        self.pair = pair

    def __str__(self):
        if self.pair:
            ret = "내가 가진 " + str(self.card) + "와 바닥패인 "+str(self.pair)
        else:
            ret = "짝이 없는" + str(self.card)
        return ret