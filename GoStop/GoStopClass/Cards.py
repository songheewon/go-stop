class Cards(object):
    # prev_cards를 추가한 이유는 이 카드가 게임 중간 턴의 경우 이전 턴의 정보를 전달받아야하는데
    # 그러기 위해서 매개변수로 이전 턴의 정보를 전달해준 후에 새로운 객체를 만들면 된다고 생각해서!
    def __init__(self, *prev_cards): # 가변 인수 설정
        self.cards = list(prev_cards)

    # def __repr__(self):
    #     return "{__class__.__name__}({})".format(
    #         __class__=self.__class__, **self.__dict__)

    def __str__(self):
        ret=""
        for card in self.cards:
            ret+=card+", "
        ret=ret[:-2]
        return ret

    def __add__(self, other):
        if isinstance(other, list):
            return self.__class__(self.cards + other)
        else:
            return self.__class__(self.cards + other.cards)

    def remove(self, card):
        self.cards.remove(card)

    # def removeAll(self):
    #     while len(self.cards)>0:
    #         self.cards.pop()

    # def monthArrange(self): # 총통, 폭탄, 흔들기 등의 처리를 위함
    #     monthCards={}
    #     for card in self.cards:
    #         monthCards[card.month].append(card)
    #     return monthCards

    def month_count(self): # 총통, 폭탄, 흔들기 등의 처리를 위함
        month_cnt=[0 for _ in range(13)] # 1월부터 12월까지 있으니까 index가 12까지 있도록 처리했음
        for card in self.cards:
            month_cnt[card.month]+=1
        return month_cnt

    def card_type_arrange(self):
        type_cards={}
        for card in self.cards:
            # 국진 패의 경우 list형의 card_type임
            if isinstance(card.card_type, list): # 만약 card_type이 list형이라면
                for t in card.card_type:
                    type_cards[t].append(card) # 두 card_type 모두에 추가
            else:
                type_cards[card.card_type].append(card)
        return type_cards