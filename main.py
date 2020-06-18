import pygame
from game import Game

pygame.init()

# creer la fenetre principale
window = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("assassin")

# charger le jeu
game = Game()

continuer = 1

# boucle principale du jeu
while continuer:
    pygame.time.delay(5)

    # actualiser la fenetre
    pygame.display.flip()

    # afficher les images (joueur, backgroud etc...)
    window.blit(game.agent_secret.image, game.agent_secret.rect)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        # detecter fermeture de la fenetre
        if event.type == pygame.QUIT:
            continuer = 0
            pygame.quit()

    # déplacement du personnage
    if keys[pygame.K_RIGHT]:
        game.agent_secret.move_right()
    if keys[pygame.K_LEFT]:
        game.agent_secret.move_left()
    if keys[pygame.K_DOWN]:
        game.agent_secret.move_down()
    if keys[pygame.K_UP]:
        game.agent_secret.move_up()
