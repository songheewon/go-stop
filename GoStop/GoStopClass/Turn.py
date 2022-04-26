from .Deck import Deck
from .Cards import CardsOnHand, CardsMatched, CardsOnTable
from .Pair import Pair


class Turn(object):
    # prev_turn을 추가한 이유는 현재 시점에서 정보를 초기화해야하는지 저장해뒀던 정보를 불러와야하는지 알아야하기 때문에!!!
    def __init__(self, prev_turn=None):
        if prev_turn is None:
            self.winner = None
            self.deck = Deck()
            self.cards_on_table = CardsOnTable()  # 바닥패, player1과 player2에게 공통적인 패
            self.current_player = 0  # 현재 턴인 player의 idx
            self.player_hand = [CardsOnHand() for _ in range(2)]  # idx=0 -> player1 hand, idx=1 -> player2 hand
            self.player_matched = [CardsMatched() for _ in
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

    @staticmethod
    def first_turn():  # 맨 처음 턴은 무조건 패 섞고 패 나누기를 진행
        current = TurnStart()  # 지금 상태는 턴 시작 상태
        current.deck.card_shuffle()  # 패 섞기
        for _ in range(2):  # 2번 반복
            for _ in range(5):  # player1에게 5장
                current.player_hand[0] += current.deck.pop()
            for _ in range(5):  # player2에게 5장
                current.player_hand[1] += current.deck.pop()
            for _ in range(4):  # 바닥에 4장
                current.cards_on_table += current.deck.pop()

        # 총통은 첫 턴에서 바로 승리 처리
        # if current.player_hand[0].chongtong() and current.player_hand[1].chongtong():
        #     if current.player_hand[0].get_chongtong_month() > current.player2_hand[1].get_chongtong_month():
        #         current.winner = 0
        #         current = TurnEnd()
        #     else:
        #         current.winner = 1
        #         current = TurnEnd()
        # elif current.player_hand[0].chongtong():
        #     current.winner = 0
        #     current = TurnEnd()
        # elif current.player_hand[1].chongtong():
        #     current.winner = 1
        #     current = TurnEnd()
        return current

    def step_1(self):  # 자식 클래스들은 이 클래스를 가짐, 하지만 이 클래스에선 사용 x
        raise NotImplementedError()

    def step_2(self, card_pairs_or_action):  # 자식 클래스들은 이 클래스를 가짐, 하지만 이 클래스에선 사용 x
        raise NotImplementedError()


class TurnStart(Turn):  # 턴 시작 상태 (1단계)
    def step_1(self):  # player의 손에 있는 패와 바닥 패 짝을 맞춰주는 함수
        can_match_cards = []  # 내면 바닥패와 맞출 수 있는 카드 리스트
        for card in self.player_hand[self.current_player]:  # player 손에 있는 카드를 하나씩 검사
            pairs = self.cards_on_table.get_pair(card)  # 테이블 위에서 현재 맞출 수 있는 카드들
            if pairs:  # 맞출 수 있는 카드가 1장 이상이라면
                for pair in pairs:
                    can_match_cards.append(Pair(card, pair))  # [낼 카드, 맞출 수 있는 카드] 형식으로 저장
            else:  # 맞출 수 있는 카드가 없다면
                can_match_cards.append(Pair(card, None))  # [낼 카드, None] 형식으로 저장
        return can_match_cards

    def step_2(self, card_pairs):
        current = TurnMiddle(prev_turn=self)
        if card_pairs is not None:
            current.player_hand[current.current_player].remove(card_pairs.card)  # 손에 있던 카드 제거
            ### 똥 싸는 거 처리를 어디서 해주지?? ###
            if card_pairs.pair is not None:  # 짝 카드가 있다면
                current.cards_on_table.remove(card_pairs.pair)  # 그 카드를 바닥 패에서 제거
            else:  # 짝 카드가 없다면
                current.cards_on_table += card_pairs.card  # player가 내려놓은 카드 바닥 패에 추가
        current.last_paired_card = card_pairs
        current.top_deck_card = current.deck.pop()
        return current


class TurnMiddle(Turn):  # 턴 중간 상태 (2단계)
    def step_1(self):  # 바닥 패와 뒤집은 패의 짝을 맞춰주는 함수
        can_match_cards = []  # 뒤집으면 바닥패와 맞출 수 있는 카드 리스트
        pairs = self.cards_on_table.get_pair(self.top_card)  # top_card는 player가 deck에서 뒤집는 카드
        if pairs:  # 맞출 수 있는 카드가 1장 이상이라면
            for pair in pairs:
                can_match_cards.append(Pair(self.top_card, pair))  # [뒤집은 카드, 짝 카드] 형식으로 저장
        else:  # 맞출 수 있는 카드가 없다면
            can_match_cards.append(Pair(self.top_card, None))  # [뒤집은 카드, None] 형식으로 저장
        return can_match_cards

    def step_2(self, card_pairs):
        current = TurnStart(prev_turn=self)  # 다시 처음으로 돌아간다고 가정 (만약 점수가 났다면 current를 변경해줄 것임)
        if self.last_paired_card.pair is not None:
            current.player_matched[current.current_player] += self.last_paired_card.card
            current.player_matched[current.current_player] += self.last_paired_card.pair

        if card_pairs is not None:
            if card_pairs.pair is not None:  # 짝 카드가 있다면
                current.cards_on_table.remove(card_pairs.pair)  # 짝 카드를 바닥 패에서 제거하고
                # 현재 player의 matched card로 뒤집은 카드와 짝 맞춰진 카드 모두 가져온다.
                current.player_matched[current.current_player] += card_pairs.card
                current.player_matched[current.current_player] += card_pairs.pair
            else:  # 짝 카드가 없다면
                current.cards_on_table += card_pairs.card  # 뒤집은 카드를 바닥에 둔다.

        if current.player_matched[current.current_player].score >= 7:  # 현재 턴인 player의 점수가 7점 이상 났다면
            current = TurnDecision(prev_turn=self)  # GO 또는 STOP을 외칠 수 있다.
        else:  # 점수가 나지 않았다면
            current.current_player = (current.current_player + 1) % 2  # 다음 턴으로 이동
        return current


class TurnDecision(Turn):  # 턴 마지막 상태 (3단계)
    def step_1(self):
        if len(self.deck) > 0:  # GO할 수도 STOP할 수도 있음
            return [GoStop.GO, GoStop.STOP]
        return [GoStop.STOP]  # 무조건 STOP해야함

    def step_2(self, action):
        if action == GoStop.GO:  # GO를 선택했다면
            current = TurnStart(prev_turn=self)  # 다시 턴 변경
            # 흠,,,, 점수 처리를 어떻게 해주지?
        elif action == GoStop.STOP:  # STOP을 선택했다면
            current = TurnEnd(prev_turn=self)  # 게임 끝을 알리고
            current.winner = self.current_player  # 승자 선언
        return current


class TurnEnd(Turn):
    def step_1(self):
        return []

    def step_2(self, action):
        return None


class GoStop(object):
    GO = 1
    STOP = 2
