import pygame
import random

#############################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")  # 게임 이름

# FPS
clock = pygame.time.Clock()
#############################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load("C:\\study\\Python\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\study\\Python\\pygame_basic\\character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
# 이동 속도
character_speed = 0.4

# 이동할 좌표
to_x = 0

# 하늘에서 떨어지는 똥 불러오기
ddong = pygame.image.load("C:\\study\\Python\\pygame_basic\\enemy.png")
ddong_size = ddong.get_rect().size  # 이미지의 크기를 구해옴
ddong_width = ddong_size[0]  # 캐릭터의 가로 크기
ddong_height = ddong_size[1]  # 캐릭터의 세로 크기
ddong_x_pos = random.randrange(0, screen_width - ddong_width)  # 랜덤 위치 (가로)
ddong_y_pos = 0  # 화면의 가장 위 (세로)

fall_speed = 0.2  # 하늘에서 똥이 떨어지는 속도

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    # 똥의 위치 정의
    ddong_y_pos += fall_speed * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 캐릭터가 똥과 충돌하지 않고 똥이 바닥까지 떨어졌다면 다시 똥이 하늘에서 떨어진다
    if ddong_y_pos > screen_height - ddong_height:
        ddong_x_pos = random.randrange(0, screen_width - ddong_width)  # 랜덤 위치 (가로)
        ddong_y_pos = 0  # 화면의 가장 위 (세로)

    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))  # 적 그리기

    pygame.display.update()  # 게임화면을 다시 그리기!

pygame.quit()
