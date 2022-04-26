import pygame
import sys

from GoStopClass import Turn
from GoStopClass import Player

# 초기화
pygame.init()
pygame.display.set_caption("맞고 게임")
big_font = pygame.font.SysFont("notosanscjkkr", 80)  # 큰 글씨
small_font = pygame.font.SysFont("notosanscjkkr", 40)  # 작은 글씨
smallest_font = pygame.font.SysFont("notosanscjkkr", 30)  # 더 작은 글씨
screen = pygame.display.set_mode([1200, 800])  # 창 크기 설정
FPSCLOCK = pygame.time.Clock()

push_key_msg = small_font.render("Press SPACE BAR to Start", True, (255, 255, 255))
start_screen = pygame.image.load("맞고.png")


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # 키가 눌렸다면
                if event.key == pygame.K_SPACE:  # 그 키가 스페이스바인지 확인하고
                    game_screen()  # 게임화면으로 넘어가도록 설정
        screen.blit(start_screen, (0, 0))
        screen.blit(push_key_msg, (427, 600))
        pygame.display.update()
        FPSCLOCK.tick(30)


board = pygame.image.load("판.png")
left_deck = pygame.image.load("뒷장.jpg")
hand_msg1 = smallest_font.render("Cards On", True, (255, 255, 255))
hand_msg2 = smallest_font.render("Your Hand", True, (255, 255, 255))
temp1 = pygame.image.load("FebGodori.jpg")
temp2 = pygame.image.load("JanGwang.jpg")
temp3 = pygame.image.load("JanPee1.jpg")
temp4 = pygame.image.load("OctTtee.jpg")
temp5 = pygame.image.load("NovSsangPee.jpg")
temp6 = pygame.image.load("SepGukjin.jpg")
temp7 = pygame.image.load("AprGodori.jpg")
temp8 = pygame.image.load("DecBiTtee.jpg")
temp9 = pygame.image.load("DecMeong.jpg")
temp10 = pygame.image.load("MayPee1.jpg")

temp_pee1 = pygame.image.load("AprPee1.jpg")
temp_pee2 = pygame.image.load("AprPee2.jpg")
temp_pee3 = pygame.image.load("JanPee1.jpg")
temp_pee4 = pygame.image.load("MayPee1.jpg")
temp_pee5 = pygame.image.load("JulPee1.jpg")
temp_pee6 = pygame.image.load("AugPee1.jpg")
temp_pee7 = pygame.image.load("DecSsangPee.jpg")
temp_pee8 = pygame.image.load("NovSsangPee.jpg")
temp_pee9 = pygame.image.load("FebPee2.jpg")
temp_pee10 = pygame.image.load("SepPee1.jpg")
temp_pee11 = pygame.image.load("JunPee1.jpg")
temp_pee12 = pygame.image.load("AugPee2.jpg")

temp_meong1 = pygame.image.load("AprGodori.jpg")
temp_meong2 = pygame.image.load("FebGodori.jpg")
temp_meong3 = pygame.image.load("DecMeong.jpg")
temp_meong4 = pygame.image.load("OctMeong.jpg")
temp_meong5 = pygame.image.load("AugGodori.jpg")
temp_meong6 = pygame.image.load("JulMeong.jpg")

temp_ttee1 = pygame.image.load("OctTtee.jpg")
temp_ttee2 = pygame.image.load("MayTtee.jpg")
temp_ttee3 = pygame.image.load("JunTtee.jpg")
temp_ttee4 = pygame.image.load("FebTtee.jpg")
temp_ttee5 = pygame.image.load("DecBiTtee.jpg")

temp_gwang1 = pygame.image.load("AugGwang.jpg")
temp_gwang2 = pygame.image.load("JanGwang.jpg")
temp_gwang3 = pygame.image.load("DecBiGwang.jpg")
temp_gwang4 = pygame.image.load("MarGwang.jpg")

temp_table1 = pygame.image.load("SepPee1.jpg")
temp_table2 = pygame.image.load("SepPee1.jpg")
temp_table3 = pygame.image.load("SepPee1.jpg")
temp_table4 = pygame.image.load("SepPee1.jpg")
temp_table5 = pygame.image.load("SepPee1.jpg")
temp_table6 = pygame.image.load("SepPee1.jpg")
temp_table7 = pygame.image.load("SepPee1.jpg")
temp_table8 = pygame.image.load("SepPee1.jpg")

players = [Player.HumanPlayer("ME"), Player.ComputerPlayer("COM")] # 항상 컴퓨터와 1대1로...

def game_screen():
    current = Turn.Turn.first_turn()  # 게임 시작
    while True:
        current_player = players[current.current_player]
        print("ME: " + str(current.player_hand[0]))
        print("COM: " + str(current.player_hand[1]))
        print("floor: " + str(current.cards_on_table))
        print("MY SCORE: " + str(current.player_matched[0].calc_score()))
        print("COM SCORE: " + str(current.player_matched[1].calc_score()))
        can_do = current.step_1()
        if len(can_do) == 0:
            raise Exception("Cannot Do Anything!!!!")
        action = current_player.get_action(current, can_do)
        print('*** {0} takes action {1}'.format(current_player, str(action)))
        last_player = current.current_player  # 기억해두기 (승자 출력을 위함)
        current = current.step_2(action)
        if current.get_result(last_player) == 0:
            print('*** {0} wins!'.format(players[last_player]))
            break

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(board, (0, 0))
        screen.blit(left_deck, (500, 365))
        screen.blit(hand_msg1, (1090, 280))
        screen.blit(hand_msg2, (1088, 310))
        # 손에 있는 패 한 번 놔둬보기 (자리 괜찮은지 확인하기 위함)
        screen.blit(temp1, (1090, 360))
        screen.blit(temp2, (1145, 360))
        screen.blit(temp3, (1090, 440))
        screen.blit(temp4, (1145, 440))
        screen.blit(temp5, (1090, 520))
        screen.blit(temp6, (1145, 520))
        screen.blit(temp7, (1090, 600))
        screen.blit(temp8, (1145, 600))
        screen.blit(temp9, (1090, 680))
        screen.blit(temp10, (1145, 680))
        # 내가 딴 피 한 번 놔둬보기 (자리 괜찮은지 확인하기 위함)
        screen.blit(temp_pee1, (845, 720))
        screen.blit(temp_pee2, (865, 720))
        screen.blit(temp_pee3, (885, 720))
        screen.blit(temp_pee4, (905, 720))
        screen.blit(temp_pee5, (925, 720))
        screen.blit(temp_pee6, (845, 640))
        screen.blit(temp_pee7, (865, 640))
        screen.blit(temp_pee8, (885, 640))
        screen.blit(temp_pee9, (905, 640))
        screen.blit(temp_pee10, (925, 640))
        # 내가 딴 멍 한 번 놔둬보기 (자리 괜찮은지 확인하기 위함)
        screen.blit(temp_meong1, (437.5, 535))
        screen.blit(temp_meong2, (457.5, 535))
        screen.blit(temp_meong3, (477.5, 535))
        screen.blit(temp_meong4, (497.5, 535))
        screen.blit(temp_meong5, (517.5, 535))
        screen.blit(temp_meong6, (537.5, 535))
        # 내가 딴 띠 한번 놔둬보기 (자리 괜찮은지 확인하기 위함)
        screen.blit(temp_ttee1, (437.5, 720))
        screen.blit(temp_ttee2, (457.5, 720))
        screen.blit(temp_ttee3, (477.5, 720))
        screen.blit(temp_ttee4, (497.5, 720))
        screen.blit(temp_ttee5, (517.5, 720))
        # 내가 딴 광 한번 놔둬보기 (자리 괜찮은지 확인하기 위함)
        screen.blit(temp_gwang1, (50, 640))
        screen.blit(temp_gwang2, (70, 640))
        screen.blit(temp_gwang3, (90, 640))
        screen.blit(temp_gwang4, (110, 640))
        # 바닥 패 한번 놔둬보기 (자리 괜찮은지 확인하기 위함)
        screen.blit(temp_table1, (50, 365))
        screen.blit(temp_table2, (120, 365))
        screen.blit(temp_table3, (190, 365))
        screen.blit(temp_table4, (260, 365))
        screen.blit(temp_table1, (330, 365))
        screen.blit(temp_table1, (400, 365))
        screen.blit(temp_table5, (600, 365))
        screen.blit(temp_table6, (670, 365))
        screen.blit(temp_table7, (740, 365))
        screen.blit(temp_table8, (810, 365))
        screen.blit(temp_table1, (880, 365))
        screen.blit(temp_table1, (950, 365))
        # 상대 패는 뒤집어서 동일하게 깔자!!!!
        # 이제 연동만 하면 되겠당...!
        # 연동까지 다 하면 카드 움직이는 액션..? 애니메이션..? 넣어서 퀄리티를 올리자

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()
