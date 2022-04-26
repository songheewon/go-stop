import Deck
import CardsMatched
import CardsOnTable
import CardsOnHand
import TurnStart
import Pair


class Turn(object):
    # prev_turn을 추가한 이유는 현재 시점에서 정보를 초기화해야하는지 저장해뒀던 정보를 불러와야하는지 알아야하기 때문에!!!
    def __init__(self, prev_turn=None):
        if prev_turn is None:
            self.winner = None
            self.deck = Deck.Deck()
            self.cards_on_table = CardsOnTable.CardsOnTable()  # 바닥패, player1과 player2에게 공통적인 패
            self.current_player = 0  # 현재 턴인 player의 idx
            self.player_hand = [CardsOnHand.CardsOnHand() for _ in
                                range(2)]  # idx=0 -> player1 hand, idx=1 -> player2 hand
            self.player_matched = [CardsMatched.CardsMatched() for _ in
                                   range(2)]  # idx=0 -> player1 matched cards, idx=1 -> player2 matched cards
            # self.player_shake_cnt = [0 for _ in range(2)] # idx=0 -> player1이 흔든 횟수, idx=1 -> player2가 흔든 횟수
            # self.player_go_cnt = [0 for _ in range(2)] # idx=0 -> player1이 GO를 외친 횟수, idx=1 -> player2가 GO를 외친 횟수
            # self.player_go_score = [0 for _ in range(2)]  # idx=0 -> player1이 GO를 외쳤을 때의 점수, idx=1 -> player2가 GO를 외쳤을 때의 점수

        else:
            self.winner = None
            self.deck = Deck.Deck(prev_card=prev_turn.deck)
            self.cards_on_table = CardsOnTable.CardsOnTable(*prev_turn.cards_on_table)  # 바닥패, player1과 player2에게 공통적인 패
            self.current_player = prev_turn.current_player  # 지금이 아니라 턴 마지막에 current_player의 idx를 바꿔주면 됨
            self.player_hand = [CardsOnHand.CardsOnHand(*card) for card in
                                prev_turn.player_hand]  # idx=0 -> player1 hand, idx=1 -> player2 hand
            self.player_matched = [CardsMatched.CardsMatched(*card) for card in
                                   prev_turn.player_matched]  # idx=0 -> player1 matched cards, idx=1 -> player2 matched cards


    def first_turn(self): # 맨 처음 턴은 무조건 패 섞고 패 나누기를 진행
        current=TurnStart() # 지금 상태는 턴 시작 상태
        current.deck.cardShuffle()  # 패 섞기
        for _ in range(2):  # 2번 반복
            for _ in range(5):  # player1에게 5장
                current.player_hand[0] += current.deck.pop()
            for _ in range(5):  # player2에게 5장
                current.player_hand[1] += current.deck.pop()
            for _ in range(4):  # 바닥에 4장
                current.cards_on_table += current.deck.pop()

        # 총통은 첫 턴에서 바로 승리 처리
        if current.player_hand[0].chongtong() and current.player_hand[1].chongtong():
            if current.player_hand[0].get_chongtong_month() > current.player2_hand[1].get_chongtong_month():
                current.winner = 0
            else:
                current.winner = 1
        elif current.player_hand[0].chongtong():
            current.winner = 0
        elif current.player_hand[1].chongtong():
            current.winner = 1

        return current