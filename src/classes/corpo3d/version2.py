from vpython import sphere, mag, vector

class Corpo3D:
    def __init__(self, pos, massa, raio, cor, vx = 0, vy = 0, vz = 0):
        self.esfera = sphere(pos=pos, radius=raio, color=cor)
        self.massa = massa
        self.vel = vector(vx, vy, vz)
        self.aceleracao = vector(0, 0, 0)
    
    def calcular_aceleracao(self, outros_corpos, g):
        forca_total = vector(0, 0, 0)

        for corpo in outros_corpos:
            if self == corpo:
                continue

            r = corpo.esfera.pos - self.esfera.pos
            distancia_quadrado = mag(r)**2

            if distancia_quadrado < (self.esfera.radius + corpo.esfera.radius)**2:
                continue

            forca_total += g * (self.massa * corpo.massa / distancia_quadrado) * (r / mag(r))
        
        self.aceleracao = forca_total / self.massa
    
    def atualizar_posicao(self, dt):
        self.esfera.pos += self.vel * dt + 0.5 * self.aceleracao * dt**2
    
    def atualizar_velocidade(self, aceleracao_antiga, dt):
        self.vel += 0.5 * (aceleracao_antiga + self.aceleracao) * dt