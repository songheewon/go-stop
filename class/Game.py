import Deck
import CardsMatched
import CardsOnTable
import CardsOnHand

class Game(object):
    def __init__(self):
        self.winner = None
        self.deck = Deck.Deck()
        self.cards_on_table = CardsOnTable.CardsOnTable() # 바닥패, player1과 player2에게 공통적인 패
        self.current_player = 0  # 현재 턴인 player의 idx
        self.player_hand = [CardsOnHand.CardsOnHand() for _ in range(2)]  # idx=0 -> player1 hand, idx=1 -> player2 hand
        self.player_matched = [CardsMatched.CardsMatched() for _ in
                               range(2)]  # idx=0 -> player1 matched cards, idx=1 -> player2 matched cards
        self.player_shake_cnt = [0 for _ in range(2)] # idx=0 -> player1이 흔든 횟수, idx=1 -> player2가 흔든 횟수
        self.player_go_cnt = [0 for _ in range(2)] # idx=0 -> player1이 GO를 외친 횟수, idx=1 -> player2가 GO를 외친 횟수
        self.player_go_score = [0 for _ in range(2)]  # idx=0 -> player1이 GO를 외쳤을 때의 점수, idx=1 -> player2가 GO를 외쳤을 때의 점수

    def startGame(self):
        self.deck.cardShuffle()  # 패 섞기
        for _ in range(2):  # 2번 반복
            for _ in range(5):  # player1에게 5장
                self.player1_hand += self.deck.pop()
            for _ in range(5):  # player2에게 5장
                self.player2_hand += self.deck.pop()
            for _ in range(4):  # 바닥에 4장
                self.cards_on_table += self.deck.pop()
        return self

    # def getWinner(self):
    #     # 총통은 바로 승리 처리
    #     if self.player1_hand.chongTong() and self.player2_hand.chongTong():
    #         player1_chongtong_month = self.player1_hand.getChongTongMonth()
    #         player2_chongtong_month = self.player2_hand.getChongTongMonth()
    #         if player1_chongtong_month > player2_chongtong_month:
    #             self.winner = "player 1"
    #         else:
    #             self.winner = "player 2"
    #     elif self.player1_hand.chongTong():
    #         self.winner = "player 1"
    #     elif self.player2_hand.chongTong():
    #         self.winner = "player 2"
    #     else:  # 여기부터 다시 처리해주기
    #         self.winner = None
