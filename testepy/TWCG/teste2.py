import pygame
import sys

pygame.init()

# Configurações da tela
largura_tela = 1200
altura_tela = 650
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Visual Novel")

# Cores
branco = (255, 255, 255)

# Carrega imagens
background_image = pygame.image.load("menu.png")  # Substitua com o caminho para sua imagem de fundo
character_image = pygame.image.load("luigi1.png")  # Substitua com o caminho para a imagem do personagem

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Desenha o fundo e o personagem
        tela.fill(branco)
        tela.blit(background_image, (0, 0))
        tela.blit(character_image, (100, 100))  # Ajuste as coordenadas conforme necessário

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
