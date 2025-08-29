from classes.corpo import Corpo
import pygame
import math

# CONSTANTES
LARGURA, ALTURA = 1000, 800
FPS = 60
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simulador Gravitacional")

# CORES
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)
AZUL = (100, 149, 237)
VERMELHO = (188, 39, 50)
CINZA_ESCURO = (50, 50, 50)

def main():
    rodando = True
    clock = pygame.time.Clock()

    sol = Corpo(LARGURA / 2, ALTURA / 2, 1000, 20, AMARELO)
    terra  = Corpo(LARGURA / 2 - 200, ALTURA / 2, 1, 10, AZUL)
    terra.vy = 2.0

    marte = Corpo(LARGURA / 2 + 300, ALTURA / 2, 0.5, 8, VERMELHO)
    marte.vy = -1.5

    corpos = [sol, terra, marte]

    while rodando:
        clock.tick(FPS)
        TELA.fill(CINZA_ESCURO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            
        for corpo1 in corpos:
            corpo1.aplicar_forca(corpos)

        for corpo2 in corpos:
            corpo2.atualizar()
            corpo2.desenhar(TELA)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()