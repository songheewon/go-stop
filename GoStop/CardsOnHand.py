import Cards


class CardsOnHand(Cards):
    def calc_score(self):
        self.score = 0
        self.month_cards = self.month_arrange()
        self.month_cnt = self.month_count()

    def chongtong(self):  # 총통 여부
        for cnt in self.month_cnt:
            if cnt == 4:
                return True
        return False

    def get_chongTong_month(self):
        if not self.chongtong():
            return
        chongtong_month = 0
        for month in range(13):
            if self.month_cnt[month] == 4:
                chongtong_month.append(month)
        return chongtong_month[-1] # 제일 큰 총통의 달 수 리턴


    # 폭탄 처리 함수 만들기