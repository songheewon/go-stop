import Cards
import Card


class CardsMatched(Cards):
    def calc_score(self):
        self.score = 0
        self.type_cards = self.card_type_arrange()
        self.pee_score()  # 멍보다 피를 먼저 계산해서 국진 패를 처리해주자!
        self.meong_score()
        self.gwang_score()
        self.ttee_score()
        return self.score

    def gwang_score(self):  # 광 계산
        gwang_cards = self.type_cards[Card.CardType.GWANG] + self.type_cards[Card.CardType.BIGWANG]
        if len(gwang_cards) == 5:  # 광 패가 5장이면
            self.score += 15  # 15점 증가
        if len(gwang_cards) == 4:  # 광 패가 4장이면
            self.score += 4  # 4점 증가
        if len(gwang_cards) == 3:  # 광 패가 3장인데
            if self.type_cards[Card.CardType.BIGWANG]:  # 비광이 존재한다면
                self.score += 2  # 2점 증가
            else:  # 그렇지 않다면
                self.score += 3  # 3점 증가

    def meong_score(self):  # 멍 계산
        meong_cards = self.type_cards[Card.CardType.MEONG] + self.type_cards[Card.CardType.GODORI]  # 멍 패 전부 (멍+고도리)
        godori_cards = self.type_cards[Card.CardType.GODORI]
        if len(meong_cards) >= 5:  # 멍 패가 5장 이상이면
            self.score += len(meong_cards) - 4  # 5장부터 1점이니까, (멍 패 개수 - 4)점 증가
        if len(godori_cards) == 3:  # 고도리가 3장 다 모였다면
            self.score += 5  # 5점 증가

    def ttee_score(self): # 띠 계산
        ttee_cards = self.type_cards[Card.CardType.REDTTEE] + self.type_cards[Card.CardType.BLUETTEE] + self.type_cards[
            Card.CardType.TTEE] + self.type_cards[Card.CardType.BITTEE]  # 띠 패 전부 (홍단+청단+초단+비초단)
        redTtee_cards = self.type_cards[Card.CardType.REDTTEE]  # 홍단
        blueTtee_cards = self.type_cards[Card.CardType.BLUETTEE]  # 청단
        choTtee_cards = self.type_cards[Card.CardType.TTEE]  # 초단
        if len(ttee_cards) >= 5:  # 띠 패가 5장 이상이면
            self.score += len(ttee_cards) - 4  # 5장부터 1점이니까, (띠 패 개수 - 4)점 증가
        if len(redTtee_cards) == 3:  # 홍단이 3장 다 모였다면
            self.score += 3  # 3점 증가
        if len(blueTtee_cards) == 3:  # 청단이 3장 다 모였다면
            self.score += 3  # 3점 증가
        if len(choTtee_cards) == 3:  # 초단이 3장 다 모였다면
            self.score += 3  # 3점 증가

    def pee_score(self): # 피 계산
        pee_cards = self.type_cards[Card.CardType.PEE]  # 피
        ssangpee_cards = self.type_cards[Card.CardType.SSANGPEE]  # 쌍피
        add_score = len(pee_cards) + 2 * len(ssangpee_cards)
        if add_score >= 10:  # 10장부터 1점이니까
            if Card.sep_gukjin in self.type_cards[Card.CardType.MEONG]:  # 그런데 이때, 국진 패를 가지고 있다면
                self.type_cards[Card.CardType.MEONG].remove(Card.sep_gukjin)  # 국진을 멍 패에서 없애주고
                self.score += add_score + 2 - 9  # (피 패 개수 - 9)점 증가 인데, 2점을 더 더함
            else:  # 국진 패가 없다면
                self.score += add_score - 9  # (피 패 개수 - 9)점 증가