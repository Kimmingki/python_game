import pygame
import random
###################################################### 기본적인 부분
pygame.init()

# 화면 크기 조정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("Avoiding poo")

# FPS
clock = pygame.time.Clock()

######################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load("/Users/kimminki/Documents/python_game/background.png")

character = pygame.image.load("/Users/kimminki/Documents/python_game/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
character_speed = 10


ddong = pygame.image.load("/Users/kimminki/Documents/python_game/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10

ddong2 = pygame.image.load("/Users/kimminki/Documents/python_game/enemy.png")
ddong2_size = ddong2.get_rect().size
ddong2_width = ddong2_size[0]
ddong2_height = ddong2_size[1]
ddong2_x_pos = random.randint(0, screen_width - ddong2_width)
ddong2_y_pos = 0
ddong2_speed = 7


running = True

while(running):
    dt = clock.tick(60) # FPS

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # close button
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed
    ddong2_y_pos += ddong2_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
    if ddong2_y_pos > screen_height:
        ddong2_y_pos = 0
        ddong2_x_pos = random.randint(0, screen_width - ddong_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    ddong2_rect = ddong2.get_rect()
    ddong2_rect.left = ddong2_x_pos
    ddong2_rect.top = ddong2_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했습니다.")
        running = False
    elif character_rect.colliderect(ddong2_rect):
        print("충돌했습니다.")
        running = False


    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
    screen.blit(ddong2, (ddong2_x_pos, ddong2_y_pos))
    pygame.display.update() # 화면 다시 그리기

# 잠시 대기
pygame.time.delay(1000) # 2초 정도 대기 (ms)

# 게임 종료
pygame.quit()