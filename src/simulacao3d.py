from classes.corpo3d import Corpo3D
from vpython import scene, color, vector, rate
import math

# CONSTANTES
LARGURA, ALTURA = 1000, 800
FPS = 600
GRAVITACAO = 0.001

def main():
    index = 0
    scene.background = color.black
    scene.width = LARGURA
    scene.height = ALTURA

    sol = Corpo3D(pos=vector(0, 0, 0), massa=10000, raio=50, cor=color.yellow)
    sol_focus = True

    dist_terra = 250
    terra = Corpo3D(pos=vector(250, 0, 0), massa=10, raio=10, cor=color.blue)
    v_terra = math.sqrt((GRAVITACAO * sol.massa) / dist_terra)
    terra.vy = v_terra
    terra_focus = False

    # dist_lua_terra = 20
    # lua = Corpo3D(pos=vector(dist_terra, dist_lua_terra, 0), massa=2, raio=4, cor=color.white)
    # v_lua_terra = math.sqrt((GRAVITACAO * terra.massa) / dist_lua_terra)
    # lua.vx = -v_lua_terra
    # lua.vy = terra.vy

    dist_marte = 500
    marte = Corpo3D(pos=vector(-500, 0, 0), massa=5, raio=7, cor=color.red)
    v_marte = math.sqrt((GRAVITACAO * sol.massa) / dist_marte)
    marte.vy = -v_marte
    marte_focus = False

    corpos = [sol, terra, marte]  
    focos = [sol_focus, terra_focus, marte_focus]

    def changeFoco(index):
        for i in range(len(focos)):
            if i == index:
                focos[i] = True
            else:
                focos[i] = False

    def focar_em_corpo(index):
        corpo = corpos[index]
        scene.center = corpo.esfera.pos

    def focar_corpo():
        for foco in focos:
            if foco == True:
                i = focos.index(foco)
                scene.center = corpos[i].esfera.pos

    def handle_keys(evt):
        if evt.key == 's':
            index = corpos.index(sol)
            changeFoco(index)
        elif evt.key == 't':
            index = corpos.index(terra)
            changeFoco(index)
        # elif evt.key == 'l':
        #     index = corpos.index(lua)
        #     changeFoco(index)
        elif evt.key == 'm':
            index = corpos.index(marte)
            changeFoco(index)
        elif evt.key == 'c':
            scene.center = vector(0, 0, 0)

    scene.bind('keydown', handle_keys)

    while True:
        rate(FPS)

        # focar_em_corpo(index)
        focar_corpo()

        for corpo1 in corpos:
            corpo1.aplicar_forca(corpos, GRAVITACAO)

        for corpo2 in corpos:
            corpo2.atualizar()
        

if __name__ == "__main__":
    main()