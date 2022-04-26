import Turn
import TurnStart
import TurnDecision
import Pair


class TurnMiddle(Turn):  # 턴 중간 상태 (2단계)
    def match_cards(self):  # 바닥 패와 뒤집은 패의 짝을 맞춰주는 함수
        can_match_cards = []  # 뒤집으면 바닥패와 맞출 수 있는 카드 리스트
        pairs = self.cards_on_table.get_pair(self.top_card)  # top_card는 player가 deck에서 뒤집는 카드
        if pairs:  # 맞출 수 있는 카드가 1장 이상이라면
            for pair in pairs:
                can_match_cards.append(Pair(self.top_card, pair))  # [뒤집은 카드, 짝 카드] 형식으로 저장
        else:  # 맞출 수 있는 카드가 없다면
            can_match_cards.append(Pair(self.top_card, None))  # [뒤집은 카드, None] 형식으로 저장
        return can_match_cards

    def after_matching(self, card_pairs):
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
