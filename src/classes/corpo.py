import pygame
import math

# CONTANTES
GRAVITACAO = 0.6

class Corpo:
    def __init__(self, x, y, massa, raio, cor):
        self.x = x
        self.y = y
        self.massa = massa
        self.raio = raio
        self.cor = cor
        self.vx = 0
        self.vy = 0

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), self.raio)

    def aplicar_forca(self, outros_corpos):
        fx = 0
        fy = 0

        for corpo in outros_corpos:
            if self == corpo:
                continue

            dx = corpo.x - self.x
            dy = corpo.y - self.y
            distancia_quadrada = dx**2 + dy**2

            if distancia_quadrada < 100:
                continue

            forca = (GRAVITACAO * self.massa * corpo.massa) / distancia_quadrada

            angulo = math.atan2(dy, dx)
            fx += math.cos(angulo) * forca
            fy += math.sin(angulo) * forca

        self.vx += fx / self.massa
        self.vy += fy / self.massa

    def atualizar(self):
        self.x += self.vx
        self.y += self.vy