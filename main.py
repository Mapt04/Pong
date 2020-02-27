import pygame

pygame.init()

width = 800
height = 495
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    for i in range(20):
        pygame.draw.rect(win, (255, 255, 255), (width/2-1, i*25, 2, 20))

    pygame.display.update()

pygame.quit