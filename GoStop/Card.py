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
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12
    BONUS = 13


class CardType(object):
    GWANG = 1  # 광
    BIGWANG = 2  # 비광(12월 광)
    MEONG = 3  # 멍
    GODORI = 4  # 고도리 패
    REDTTEE = 5  # 홍단
    BLUETTEE = 6  # 청단
    TTEE = 7  # 초단
    BITTEE = 8  # 비초단
    PEE = 9  # 피
    SSANGPEE = 10  # 쌍피

#class ImgName(object):



jan_gwang = Card("JanGwang", Month.JAN, CardType.GWANG)
jan_ttee = Card("JanTtee", Month.JAN, CardType.REDTTEE)
jan_pee1 = Card("JanPee1", Month.JAN, CardType.PEE)
jan_pee2 = Card("JanPee2", Month.JAN, CardType.PEE)

feb_godori = Card("FebGodori", Month.FEB, CardType.GODORI)
feb_ttee = Card("FebTtee", Month.FEB, CardType.REDTTEE)
feb_pee1 = Card("FebPee1", Month.FEB, CardType.PEE)
feb_pee2 = Card("FebPee2", Month.FEB, CardType.PEE)

mar_gwang = Card("MarGwang", Month.MAR, CardType.GWANG)
mar_ttee = Card("MarTtee", Month.MAR, CardType.REDTTEE)
mar_pee1 = Card("MarPee1", Month.MAR, CardType.PEE)
mar_pee2 = Card("MarPee2", Month.MAR, CardType.PEE)

apr_godori = Card("AprGodori", Month.APR, CardType.GODORI)
apr_ttee = Card("AprTtee", Month.APR, CardType.TTEE)
apr_pee1 = Card("AprPee1", Month.APR, CardType.PEE)
apr_pee2 = Card("AprPee2", Month.APR, CardType.PEE)

may_meong = Card("MayMeong", Month.MAY, CardType.MEONG)
may_ttee = Card("MayTtee", Month.MAY, CardType.TTEE)
may_pee1 = Card("MayPee1", Month.MAY, CardType.PEE)
may_pee2 = Card("MayPee2", Month.MAY, CardType.PEE)

jun_meong = Card("JunMeong", Month.JUN, CardType.MEONG)
jun_ttee = Card("JunTtee", Month.JUN, CardType.BLUETTEE)
jun_pee1 = Card("JunPee1", Month.JUN, CardType.PEE)
jun_pee2 = Card("JunPee2", Month.JUN, CardType.PEE)

jul_meong = Card("JulMeong", Month.JUL, CardType.MEONG)
jul_ttee = Card("JulTtee", Month.JUL, CardType.TTEE)
jul_pee1 = Card("JulPee1", Month.JUL, CardType.PEE)
jul_pee2 = Card("JulPee2", Month.JUL, CardType.PEE)

aug_gwang = Card("AugGwang", Month.AUG, CardType.GWANG)
aug_godori = Card("AugTtee", Month.AUG, CardType.GODORI)
aug_pee1 = Card("AugPee1", Month.AUG, CardType.PEE)
aug_pee2 = Card("AugPee2", Month.AUG, CardType.PEE)

sep_gukjin = Card("SepGukjin", Month.SEP, [CardType.MEONG, CardType.SSANGPEE])  # 이 카드의 처리가 힘들지 않을까..?
sep_ttee = Card("SepTtee", Month.SEP, CardType.BLUETTEE)
sep_pee1 = Card("SepPee1", Month.SEP, CardType.PEE)
sep_pee2 = Card("SepPee2", Month.SEP, CardType.PEE)

oct_meong = Card("OctMeong", Month.OCT, CardType.MEONG)
oct_ttee = Card("OctTtee", Month.OCT, CardType.BLUETTEE)
oct_pee1 = Card("OctPee1", Month.OCT, CardType.PEE)
oct_pee2 = Card("OctPee2", Month.OCT, CardType.PEE)

nov_gwang = Card("NovGwang", Month.NOV, CardType.GWANG)
nov_pee1 = Card("NovPee1", Month.NOV, CardType.PEE)
nov_pee2 = Card("NovPee2", Month.NOV, CardType.PEE)
nov_ssangpee = Card("NovSsangPee", Month.NOV, CardType.SSANGPEE)

dec_bigwang = Card("DecBiGwang", Month.DEC, CardType.BIGWANG)
dec_meong = Card("DecMeong", Month.DEC, CardType.MEONG)
dec_bittee = Card("DecBiTtee", Month.DEC, CardType.BITTEE)
dec_ssangpee = Card("DecSsangPee", Month.DEC, CardType.PEE)

bonus1 = Card("Bonus1", Month.BONUS, CardType.SSANGPEE)
bonus2 = Card("Bonus2", Month.BONUS, CardType.SSANGPEE)

cards = [jan_gwang, jan_ttee, jan_pee1, jan_pee2, feb_godori, feb_ttee, feb_pee1, feb_pee2, mar_gwang, mar_ttee, mar_pee1, mar_pee2,
         apr_godori, apr_ttee, apr_pee1, apr_pee2, may_meong, may_ttee, may_pee1, may_pee2, jun_meong, jun_ttee, jun_pee1, jun_pee2,
         jul_meong, jul_ttee, jul_pee1, jul_pee2, aug_gwang, aug_godori, aug_pee1, aug_pee2, sep_gukjin, sep_ttee, sep_pee1,
         sep_pee2, oct_meong, oct_ttee, oct_pee1, oct_pee2, nov_gwang, nov_pee1, nov_pee2, nov_ssangpee, dec_bigwang, dec_meong,
         dec_bittee, dec_ssangpee, bonus1, bonus2]