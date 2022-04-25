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

    def getChongTongMonth(self):
        if not self.chongTong():
            return
        chongtong_month = 0
        for month in range(13):
            if self.month_cnt[month] == 4:
                chongtong_month.append(month)
        return chongtong_month[-1] # 제일 큰 총통의 달 수 리턴


    # 폭탄 처리 함수 만들기