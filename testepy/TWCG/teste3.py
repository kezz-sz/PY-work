import pygame
import sys

pygame.init()

largura_tela = 1200
altura_tela = 650
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("(Un)Dating Simulator")

branco = (255, 255, 255)

background_image = pygame.image.load("menu.png")  
background_image = pygame.transform.scale(background_image, (largura_tela, 780))

character_image = pygame.image.load("luigi1.png")  
novo_tamanho_personagem = (320, 500)  
character_image = pygame.transform.scale(character_image, novo_tamanho_personagem)

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        tela.fill(branco)
        tela.blit(background_image, (0, -70))
        tela.blit(character_image, (450, 100))  

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
