import Cards
import Card


class CardsMatched(Cards):
    def calcScore(self):
        self.score = 0
        self.type_cards = self.cardTypeArrange()
        self.peeScore()  # 멍보다 피를 먼저 계산해서 국진 패를 처리해주자!
        self.meongScore()
        self.gwangScore()
        self.tteeScore()
        return self.score

    def gwangScore(self):  # 광 계산
        gwang_cards = self.type_cards[Card.CardType.Gwang] + self.type_cards[Card.CardType.BiGwang]
        if len(gwang_cards) == 5:  # 광 패가 5장이면
            self.score += 15  # 15점 증가
        if len(gwang_cards) == 4:  # 광 패가 4장이면
            self.score += 4  # 4점 증가
        if len(gwang_cards) == 3:  # 광 패가 3장인데
            if self.type_cards[Card.CardType.BiGwang]:  # 비광이 존재한다면
                self.score += 2  # 2점 증가
            else:  # 그렇지 않다면
                self.score += 3  # 3점 증가

    def meongScore(self):  # 멍 계산
        meong_cards = self.type_cards[Card.CardType.Meong] + self.type_cards[Card.CardType.Godori]  # 멍 패 전부 (멍+고도리)
        godori_cards = self.type_cards[Card.CardType.Godori]
        if len(meong_cards) >= 5:  # 멍 패가 5장 이상이면
            self.score += len(meong_cards) - 4  # 5장부터 1점이니까, (멍 패 개수 - 4)점 증가
        if len(godori_cards) == 3:  # 고도리가 3장 다 모였다면
            self.score += 5  # 5점 증가

    def tteeScore(self): # 띠 계산
        ttee_cards = self.type_cards[Card.CardType.RedTtee] + self.type_cards[Card.CardType.BlueTtee] + self.type_cards[
            Card.CardType.Ttee] + self.type_cards[Card.CardType.BiTtee]  # 띠 패 전부 (홍단+청단+초단+비초단)
        redTtee_cards = self.type_cards[Card.CardType.RedTtee]  # 홍단
        blueTtee_cards = self.type_cards[Card.CardType.BlueTtee]  # 청단
        choTtee_cards = self.type_cards[Card.CardType.Ttee]  # 초단
        if len(ttee_cards) >= 5:  # 띠 패가 5장 이상이면
            self.score += len(ttee_cards) - 4  # 5장부터 1점이니까, (띠 패 개수 - 4)점 증가
        if len(redTtee_cards) == 3:  # 홍단이 3장 다 모였다면
            self.score += 3  # 3점 증가
        if len(blueTtee_cards) == 3:  # 청단이 3장 다 모였다면
            self.score += 3  # 3점 증가
        if len(choTtee_cards) == 3:  # 초단이 3장 다 모였다면
            self.score += 3  # 3점 증가

    def peeScore(self): # 피 계산
        pee_cards = self.type_cards[Card.CardType.Pee]  # 피
        ssangpee_cards = self.type_cards[Card.CardType.SsangPee]  # 쌍피
        add_score = len(pee_cards) + 2 * len(ssangpee_cards)
        if add_score >= 10:  # 10장부터 1점이니까
            if Card.SepGukjin in self.type_cards[Card.CardType.Meong]:  # 그런데 이때, 국진 패를 가지고 있다면
                self.type_cards[Card.CardType.Meong].remove(Card.SepGukjin)  # 국진을 멍 패에서 없애주고
                self.score += add_score + 2 - 9  # (피 패 개수 - 9)점 증가 인데, 2점을 더 더함
            else:  # 국진 패가 없다면
                self.score += add_score - 9  # (피 패 개수 - 9)점 증가