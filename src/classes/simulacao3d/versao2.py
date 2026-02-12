from ..corpo3d.version2 import Corpo3D
from vpython import scene, color, vector, rate, mag
import math

# CONSTANTES
LARGURA, ALTURA = 1000, 800
FPS = 600000000
GRAVITACAO = 0.001
DT = 1 / 60

def main():
    index = 0
    scene.background = color.black
    scene.width = LARGURA
    scene.height = ALTURA

    sol = Corpo3D(pos=vector(0, 0, 0), massa=10000, raio=50, cor=color.yellow)
    terra = Corpo3D(pos=vector(250, 0, 0), massa=10, raio=10, cor=color.blue)
    marte = Corpo3D(pos=vector(-500, 0, 0), massa=5, raio=7, cor=color.red)

    sol_focus = True
    terra_focus = False
    lua_focus = False
    marte_focus = False

    v_terra = math.sqrt((GRAVITACAO * sol.massa) / mag(terra.esfera.pos))
    terra.vel.y = v_terra

    v_marte = math.sqrt((GRAVITACAO * sol.massa) / mag(marte.esfera.pos))
    marte.vel.y = -v_marte

    dist_lua_terra = 20
    lua = Corpo3D(pos=terra.esfera.pos + vector(0, dist_lua_terra, 0), massa=2, raio=4, cor=color.white)
    v_lua_terra = math.sqrt((GRAVITACAO * terra.massa) / dist_lua_terra)
    lua.vel.x = terra.vel.x + v_lua_terra
    lua.vel.y = terra.vel.y


    corpos = [sol, terra, lua, marte]  
    focos = [sol_focus, terra_focus, lua_focus, marte_focus]

    def changeFoco(index):
        for i in range(len(focos)):
            focos[i] = (i == index)

    def focar_corpo():
        for i, foco in enumerate(focos):
            if foco == True:
                scene.center = corpos[i].esfera.pos
                break

    def handle_keys(evt):
        if evt.key == 's':
            index = corpos.index(sol)
            changeFoco(index)
        elif evt.key == 't':
            index = corpos.index(terra)
            changeFoco(index)
        elif evt.key == 'l':
            index = corpos.index(lua)
            changeFoco(index)
        elif evt.key == 'm':
            index = corpos.index(marte)
            changeFoco(index)
        elif evt.key == 'c':
            scene.center = vector(0, 0, 0)

    scene.bind('keydown', handle_keys)

    for corpo in corpos:
        corpo.calcular_aceleracao(corpos, GRAVITACAO)

    while True:
        rate(FPS)
        focar_corpo()

        aceleracoes_antigas = [corpo.aceleracao for corpo in corpos]

        for corpo in corpos:
            corpo.atualizar_posicao(DT)

        for corpo in corpos:
            corpo.calcular_aceleracao(corpos, GRAVITACAO)

        for i, corpo in enumerate(corpos):
            corpo.atualizar_velocidade(aceleracoes_antigas[i], DT)
        

if __name__ == "__main__":
    main()