from collections import Counter, defaultdict
from .Card import CardType
from .Card import sep_gukjin


class Cards(object):
    # prev_cards를 추가한 이유는 이 카드가 게임 중간 턴의 경우 이전 턴의 정보를 전달받아야하는데
    # 그러기 위해서 매개변수로 이전 턴의 정보를 전달해준 후에 새로운 객체를 만들면 된다고 생각해서!
    def __init__(self, *cards):  # 가변 인수 설정
        self.cards = list(cards)

    def __str__(self):
        ret = ""
        for card in self.cards:
            ret += str(card) + ", "
        ret = ret[:-2]
        return ret

    def __iadd__(self, card):
        self.cards.append(card)
        return self

    def __add__(self, other):
        if isinstance(other, list):
            return self.__class__(self.cards + other)
        else:
            return self.__class__(self.cards + other.cards)

    def __iter__(self):
        return iter(self.cards)

    def pop(self):
        return self.cards.pop()

    def remove(self, card):
        self.cards.remove(card)

    def month_arrange(self):  # 총통, 폭탄, 흔들기 등의 처리를 위함
        month_cards = defaultdict(list)
        for card in self.cards:
            month_cards[card.month].append(card)
        return month_cards

    def card_type_arrange(self):
        type_cards = defaultdict(list)
        for card in self.cards:
            # 국진 패의 경우 list형의 card_type을 가짐
            if isinstance(card.card_type, list):  # 만약 card_type이 list형이라면
                for t in card.card_type:
                    type_cards[t].append(card)  # 두 card_type 모두에 추가
            else:
                type_cards[card.card_type].append(card)
        return type_cards


class CardsOnHand(Cards):
    # 여기서 폭탄이랑 흔들기 처리를 해주면 좋을텐데!!!!
    # @property
    def calc_score(self):
         score = 0
    #     month_cards = self.month_arrange()
    #     month_count = Counter(len(cards) for cards in month_cards.values())
    #     print(month_count)
    #     if month_count[3]>0:
    #         print(month_count[3])
    #
         return score


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
        gwang_cards = self.type_cards[CardType.GWANG] + self.type_cards[CardType.BIGWANG]
        if len(gwang_cards) == 5:  # 광 패가 5장이면
            self.score += 15  # 15점 증가
        if len(gwang_cards) == 4:  # 광 패가 4장이면
            self.score += 4  # 4점 증가
        if len(gwang_cards) == 3:  # 광 패가 3장인데
            if self.type_cards[CardType.BIGWANG]:  # 비광이 존재한다면
                self.score += 2  # 2점 증가
            else:  # 그렇지 않다면
                self.score += 3  # 3점 증가

    def meong_score(self):  # 멍 계산
        meong_cards = self.type_cards[CardType.MEONG] + self.type_cards[CardType.GODORI]  # 멍 패 전부 (멍+고도리)
        godori_cards = self.type_cards[CardType.GODORI]
        if len(meong_cards) >= 5:  # 멍 패가 5장 이상이면
            self.score += len(meong_cards) - 4  # 5장부터 1점이니까, (멍 패 개수 - 4)점 증가
        if len(godori_cards) == 3:  # 고도리가 3장 다 모였다면
            self.score += 5  # 5점 증가

    def ttee_score(self):  # 띠 계산
        ttee_cards = self.type_cards[CardType.REDTTEE] + self.type_cards[CardType.BLUETTEE] + self.type_cards[
            CardType.TTEE] + self.type_cards[CardType.BITTEE]  # 띠 패 전부 (홍단+청단+초단+비초단)
        redTtee_cards = self.type_cards[CardType.REDTTEE]  # 홍단
        blueTtee_cards = self.type_cards[CardType.BLUETTEE]  # 청단
        choTtee_cards = self.type_cards[CardType.TTEE]  # 초단
        if len(ttee_cards) >= 5:  # 띠 패가 5장 이상이면
            self.score += len(ttee_cards) - 4  # 5장부터 1점이니까, (띠 패 개수 - 4)점 증가
        if len(redTtee_cards) == 3:  # 홍단이 3장 다 모였다면
            self.score += 3  # 3점 증가
        if len(blueTtee_cards) == 3:  # 청단이 3장 다 모였다면
            self.score += 3  # 3점 증가
        if len(choTtee_cards) == 3:  # 초단이 3장 다 모였다면
            self.score += 3  # 3점 증가

    def pee_score(self):  # 피 계산
        pee_cards = self.type_cards[CardType.PEE]  # 피
        ssangpee_cards = self.type_cards[CardType.SSANGPEE]  # 쌍피
        add_score = len(pee_cards) + 2 * len(ssangpee_cards)
        if add_score >= 10:  # 10장부터 1점이니까
            if sep_gukjin in self.type_cards[CardType.MEONG]:  # 그런데 이때, 국진 패를 가지고 있다면
                self.type_cards[CardType.MEONG].remove(sep_gukjin)  # 국진을 멍 패에서 없애주고
                self.score += add_score + 2 - 9  # (피 패 개수 - 9)점 증가 인데, 2점을 더 더함
            else:  # 국진 패가 없다면
                self.score += add_score - 9  # (피 패 개수 - 9)점 증가


class CardsOnTable(Cards):
    def get_pair(self, card):  # 짝 맞는 것을 찾아주는 함수
        # card는 내가 내고자 하는 카드
        # self.cards는 바닥에 깔린 카드들
        pair = []
        for card_on_table in self.cards:
            if card_on_table.month == card.month:  # 월이 일치한다면
                pair.append(card_on_table)  # 추가
        return pair
