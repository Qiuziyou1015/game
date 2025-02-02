import pygame

#初始化
pygame.init()

#設定視窗名稱
pygame.display.set_caption("frist_game")

#長寬
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h

#建立視窗
screen = pygame.display.set_mode((W,H),pygame.FULLSCREEN)

#建立時間物件
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    
    pygame.display.update()