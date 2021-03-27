import pygame

pygame.init()

# 화면 크기 조정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load("/Users/kimminki/Documents/python_game/background.png")

# 이벤트 루프
running = True

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # close button
            running = False

    screen.blit(background, (0, 0))
    pygame.display.update() # 화면 다시 그리기

# 게임 종료
pygame.quit()