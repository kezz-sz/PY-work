import pygame
import sys

pygame.init()

largura_tela = 1200
altura_tela = 650
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("(Un)Dating Simulator")

branco = (255, 255, 255)

background_image = pygame.image.load("menu.png").convert_alpha()
background_image = pygame.transform.scale(background_image, (largura_tela, 780))

character_image = pygame.image.load("luigi1.png").convert_alpha()
novo_tamanho_personagem = (320, 500)
character_image = pygame.transform.scale(character_image, novo_tamanho_personagem)

fonte = pygame.font.Font(None, 36)

areas_botoes = [
    pygame.Rect(100, 610, largura_tela // 4, 40),
    pygame.Rect(300, 610, largura_tela // 4, 40),
    pygame.Rect(500, 610, largura_tela // 4, 40),
    pygame.Rect(700, 610, largura_tela // 4, 40)
]

estado_historia = 0
textos_historia = [
    "A fala vem aqui...",
    "Próxima parte da história...",
    "Continuando a saga...",
    "E assim por diante..."
]

def desenhar_interface():
    tela.fill(branco)
    tela.blit(background_image, (0, -70))
    tela.blit(character_image, (450, 100))

    superficie_dialogo = pygame.Surface((largura_tela, 200), pygame.SRCALPHA)
    pygame.draw.rect(superficie_dialogo, (0, 0, 0, 128), (0, 0, largura_tela, 200))

    tela.blit(superficie_dialogo, (0, 450))

    texto = fonte.render(textos_historia[estado_historia], True, branco)
    tela.blit(texto, (20, 470))

    for i in range(4):
        texto_botao = fonte.render(f"Escolha {i + 1}", True, branco)
        tela.blit(texto_botao, (i * largura_tela // 4 + 100, 610))

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, area in enumerate(areas_botoes):
                    if area.collidepoint(event.pos):
                        print(f"Clicou no botão {i + 1}")

        desenhar_interface()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
