import pygame
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

enemy = pygame.image.load("/Users/kimminki/Documents/python_game/enemy.png")

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


    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # 화면 다시 그리기

# 잠시 대기
pygame.time.delay(1000) # 2초 정도 대기 (ms)

# 게임 종료
pygame.quit()