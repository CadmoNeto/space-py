from vpython import sphere, mag

class Corpo3D:
    def __init__(self, pos, massa, raio, cor):
        self.esfera = sphere(pos=pos, radius=raio, color=cor)
        self.massa = massa
        self.vx = 0
        self.vy = 0
        self.vz = 0
    
    def aplicar_forca(self, outros_corpos, g):
        fx = fy = fz = 0

        for corpo in outros_corpos:
            if self == corpo:
                continue
                
            r = corpo.esfera.pos - self.esfera.pos
            distancia_cubo = mag(r)**3

            if distancia_cubo < 1e-6:
                continue

            forca_vetor = g * (self.massa * corpo.massa / distancia_cubo) * r

            fx += forca_vetor.x
            fy += forca_vetor.y
            fz += forca_vetor.z
        
        self.vx += fx / self.massa
        self.vy += fy / self.massa
        self.vz += fz / self.massa
    
    def atualizar(self):
        self.esfera.pos.x += self.vx
        self.esfera.pos.y += self.vy
        self.esfera.pos.z += self.vz