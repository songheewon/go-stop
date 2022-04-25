class Card(object):
    def __init__(self, name, month, card_type):
        self.name = name
        self.month = month
        self.card_type = card_type

    def __repr__(self):
        return "{__class__name.__name__}(name='{name}', month={month}, card_type={card_type})".format(
            __class__=self.__class__, **self.__dict__)

    def __str__(self):
        return self.name

    # __eq__ 함수가 필요하려나...?
    # def __eq__(self, other):
    #     if other is None:
    #         return False
    #     elif isinstance(other, self.__class__):
    #         return self.month == other.month and self.card_type == other.card_type
    #     return not NotImplemented

    # Card 객체 간의 크기 비교는 할 일이 없으니 __lt__나 __gt__와 같은 함수는 생성 x
    # 혹시 미니게임으로 섯다를 추가하게 될 경우 만들자!

    def __hash__(self):
        return hash(self.month, self.card_type)


class Month(object):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12
    Bonus = 13


class CardType(object):
    Gwang = 1  # 광
    BiGwang = 2  # 비광(12월 광)
    Meong = 3  # 멍
    Godori = 4  # 고도리 패
    Gukjin = 5  # 국진
    RedTtee = 6  # 홍단
    BlueTtee = 7  # 청단
    Ttee = 8  # 초단
    BiTtee = 9  # 비초단
    Pee = 10  # 피
    SsangPee = 11  # 쌍피


JanGwang = Card("JanGwang", Month.Jan, CardType.Gwang)
JanTtee = Card("JanTtee", Month.Jan, CardType.RedTtee)
JanPee1 = Card("JanPee1", Month.Jan, CardType.Pee)
JanPee2 = Card("JanPee2", Month.Jan, CardType.Pee)

FebGodori = Card("FebGodori", Month.Feb, CardType.Godori)
FebTtee = Card("FebTtee", Month.Feb, CardType.RedTtee)
FebPee1 = Card("FebPee1", Month.Feb, CardType.Pee)
FebPee2 = Card("FebPee2", Month.Feb, CardType.Pee)

MarGwang = Card("MarGwang", Month.Mar, CardType.Gwang)
MarTtee = Card("MarTtee", Month.Mar, CardType.RedTtee)
MarPee1 = Card("MarPee1", Month.Mar, CardType.Pee)
MarPee2 = Card("MarPee2", Month.Mar, CardType.Pee)

AprGodori = Card("AprGodori", Month.Apr, CardType.Godori)
AprTtee = Card("AprTtee", Month.Apr, CardType.Ttee)
AprPee1 = Card("AprPee1", Month.Apr, CardType.Pee)
AprPee2 = Card("AprPee2", Month.Apr, CardType.Pee)

MayMeong = Card("MayMeong", Month.May, CardType.Meong)
MayTtee = Card("MayTtee", Month.May, CardType.Ttee)
MayPee1 = Card("MayPee1", Month.May, CardType.Pee)
MayPee2 = Card("MayPee2", Month.May, CardType.Pee)

JunMeong = Card("JunMeong", Month.Jun, CardType.Meong)
JunTtee = Card("JunTtee", Month.Jun, CardType.BlueTtee)
JunPee1 = Card("JunPee1", Month.Jun, CardType.Pee)
JunPee2 = Card("JunPee2", Month.Jun, CardType.Pee)

JulMeong = Card("JulMeong", Month.Jul, CardType.Meong)
JulTtee = Card("JulTtee", Month.Jul, CardType.Ttee)
JulPee1 = Card("JulPee1", Month.Jul, CardType.Pee)
JulPee2 = Card("JulPee2", Month.Jul, CardType.Pee)

AugGwang = Card("AugGwang", Month.Aug, CardType.Gwang)
AugGodori = Card("AugTtee", Month.Aug, CardType.Godori)
AugPee1 = Card("AugPee1", Month.Aug, CardType.Pee)
AugPee2 = Card("AugPee2", Month.Aug, CardType.Pee)

SepGukjin = Card("SepGukjin", Month.Sep, CardType.Gukjin)  # 이 카드의 처리가 힘들지 않을까..?
SepTtee = Card("SepTtee", Month.Sep, CardType.BlueTtee)
SepPee1 = Card("SepPee1", Month.Sep, CardType.Pee)
SepPee2 = Card("SepPee2", Month.Sep, CardType.Pee)

OctMeong = Card("OctMeong", Month.Oct, CardType.Meong)
OctTtee = Card("OctTtee", Month.Oct, CardType.BlueTtee)
OctPee1 = Card("OctPee1", Month.Oct, CardType.Pee)
OctPee2 = Card("OctPee2", Month.Oct, CardType.Pee)

NovGwang = Card("NovGwang", Month.Nov, CardType.Gwang)
NovPee1 = Card("NovPee1", Month.Nov, CardType.Pee)
NovPee2 = Card("NovPee2", Month.Nov, CardType.Pee)
NovSsangPee = Card("NovSsangPee", Month.Nov, CardType.SsangPee)

DecBiGwang = Card("DecBiGwang", Month.Dec, CardType.BiGwang)
DecMeong = Card("DecMeong", Month.Dec, CardType.Meong)
DecBiTtee = Card("DecBiTtee", Month.Dec, CardType.BiTtee)
DecSsangPee = Card("DecSsangPee", Month.Dec, CardType.Pee)

Bonus1 = Card("Bonus1", Month.Bonus, CardType.SsangPee)
Bonus2 = Card("Bonus2", Month.Bonus, CardType.SsangPee)

cards = (JanGwang, JanTtee, JanPee1, JanPee2, FebGodori, FebTtee, FebPee1, FebPee2, MarGwang, MarTtee, MarPee1, MarPee2,
         AprGodori, AprTtee, AprPee1, AprPee2, MayMeong, MayTtee, MayPee1, MayPee2, JunMeong, JunTtee, JunPee1, JunPee2,
         JulMeong, JulTtee, JulPee1, JulPee2, AugGwang, AugGodori, AugPee1, AugPee2, SepGukjin, SepTtee, SepPee1,
         SepPee2, OctMeong, OctTtee, OctPee1, OctPee2, NovGwang, NovPee1, NovPee2, NovSsangPee, DecBiGwang, DecMeong,
         DecBiTtee, DecSsangPee, Bonus1, Bonus2)
