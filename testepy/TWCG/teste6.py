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

botoes = [pygame.Rect(i * largura_tela // 4 + 100, 610, largura_tela // 4, 40) for i in range(4)]

historia = [
    {"fala": "A fala vem aqui...", "escolhas": ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]}
]

def desenhar_interface(parte_atual):
    tela.fill(branco)
    tela.blit(background_image, (0, -70))
    tela.blit(character_image, (450, 100))

    superficie_dialogo = pygame.Surface((largura_tela, 200), pygame.SRCALPHA)
    pygame.draw.rect(superficie_dialogo, (0, 0, 0, 128), (0, 0, largura_tela, 200))

    tela.blit(superficie_dialogo, (0, 450))

    texto = fonte.render(historia[parte_atual]["fala"], True, branco)
    tela.blit(texto, (20, 470))

    for i, botao in enumerate(botoes):
        texto_botao = fonte.render(historia[parte_atual]["escolhas"][i], True, branco)
        tela.blit(texto_botao, (i * largura_tela // 4 + 100, 610))

def main():
    running = True
    clock = pygame.time.Clock()

    parte_atual = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, botao in enumerate(botoes):
                    if botao.collidepoint(event.pos):
                        print(f"Clicou no botão {i + 1}")
                        if len(historia[parte_atual]["escolhas"]) > i:
                            parte_atual += 1  

        desenhar_interface(parte_atual)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
