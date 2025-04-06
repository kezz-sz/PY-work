import pygame
import sys

pygame.init()

largura_tela = 1200
altura_tela = 650
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("(Un)Dating Simulator")

branco = (255, 255, 255)
preto = (0, 0, 0, 128)

background_image = pygame.image.load("menu.png")  
background_image = pygame.transform.scale(background_image, (largura_tela, 780))

character_image = pygame.image.load("luigi1.png")  
novo_tamanho_personagem = (320, 500)  
character_image = pygame.transform.scale(character_image, novo_tamanho_personagem)

fonte = pygame.font.Font(None, 36)

def desenhar_interface():
    tela.fill(branco)
    tela.blit(background_image, (0, -70))
    tela.blit(character_image, (450, 100))  

    pygame.draw.rect(tela, preto, (0, 450, largura_tela, 200))

    texto = fonte.render("Goza em mim bolsonaro!", True, branco)
    tela.blit(texto, (20, 470))

    for i in range(4):
        pygame.draw.rect(tela, preto, (i * largura_tela // 4, 550, largura_tela // 4, 50))
        texto_botao = fonte.render(f"Escolha {i+1}", True, branco)
        tela.blit(texto_botao, (i * largura_tela // 4 + 100, 610))

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        desenhar_interface()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
