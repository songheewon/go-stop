import Cards


class CardsOnHand(Cards):
    def calcScore(self):
        self.score = 0
        self.month_cards = self.monthArrange()
        self.month_cnt = self.monthCount()

    def chongTong(self):  # 총통 여부
        for cnt in self.month_cnt:
            if cnt == 4:
                return True
        return False

    # 폭탄 처리 함수 만들기