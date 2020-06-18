import pygame
pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((1080, 720), 0, 32)
pygame.display.set_caption("assassin")


continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
            pygame.quit()

    pygame.display.update()
    clock.tick(60)
    
