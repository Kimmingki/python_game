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

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("/Users/kimminki/Documents/python_game/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = ((screen_width / 2) - (character_width / 2))  # 화면 가로의 절반에 위치
character_y_pos = screen_height - character_height # 화면 세로의 가장 밑에 위치

# 이벤트 루프
running = True

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # close button
            running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # 화면 다시 그리기

# 게임 종료
pygame.quit()