class Pair(object):
    def __init__(self, card, pair): # 낸 카드, 짝 카드
        self.card = card
        self.pair = pair

    def __str__(self):
        if self.pair:
            ret = str(self.card) + "패와 바닥패인 "+ str(self.pair) + "패를 맞춥니다."
        else:
            ret = "짝이 없는 " + str(self.card) + "패를 내려놓습니다."
        return ret