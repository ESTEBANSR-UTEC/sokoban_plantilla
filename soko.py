import os
import random

class JuegoSokoban:
    def __init__(self):
        self.tamanio_tablero = 7
        self.mapas = [mapa1, mapa2, mapa3]
        self.indice_mapa_actual = 0
        self.posicion_jugador = [0, 0]
        self.posiciones_cajas = []
        self.posiciones_metas = []
        self.tablero = []
        self.movimientos = {
            'w': [-1, 0],
            'a': [0, -1],
            's': [1, 0],
            'd': [0, 1]
        }

    def generar_tablero(self):
        mapa_actual = self.mapas[self.indice_mapa_actual]
        self.tablero = [[celda for celda in fila] for fila in mapa_actual]

        for i in range(self.tamanio_tablero):
            for j in range(self.tamanio_tablero):
                if mapa_actual[i][j] == personaje:
                    self.posicion_jugador = [i, j]
                elif mapa_actual[i][j] == caja:
                    self.posiciones_cajas.append([i, j])
                elif mapa_actual[i][j] == meta:
                    self.posiciones_metas.append([i, j])

    def imprimir_tablero(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar terminal
        for fila in self.tablero:
            print(''.join(fila))
        print()

    def mover_jugador(self, direccion):
        movimiento = self.movimientos.get(direccion)
        if not movimiento:
            return

        nueva_posicion = [self.posicion_jugador[0] + movimiento[0], self.posicion_jugador[1] + movimiento[1]]

        if not (0 <= nueva_posicion[0] < self.tamanio_tablero and 0 <= nueva_posicion[1] < self.tamanio_tablero):
            return

        if self.tablero[nueva_posicion[0]][nueva_posicion[1]] == paredes:
            return

        if [nueva_posicion[0], nueva_posicion[1]] in self.posiciones_cajas:
            nueva_posicion_caja = [nueva_posicion[0] + movimiento[0], nueva_posicion[1] + movimiento[1]]
            if not (0 <= nueva_posicion_caja[0] < self.tamanio_tablero and 0 <= nueva_posicion_caja[1] < self.tamanio_tablero):
                return
            if self.tablero[nueva_posicion_caja[0]][nueva_posicion_caja[1]] in [paredes, caja]:
                return
            index_caja = self.posiciones_cajas.index([nueva_posicion[0], nueva_posicion[1]])
            self.tablero[self.posiciones_cajas[index_caja][0]][self.posiciones_cajas[index_caja][1]] = espacio_piso
            self.posiciones_cajas[index_caja] = nueva_posicion_caja
            if self.tablero[self.posiciones_cajas[index_caja][0]][self.posiciones_cajas[index_caja][1]] == meta:
                self.tablero[self.posiciones_cajas[index_caja][0]][self.posiciones_cajas[index_caja][1]] = caja_meta
            else:
                self.tablero[self.posiciones_cajas[index_caja][0]][self.posiciones_cajas[index_caja][1]] = caja

        if self.tablero[self.posicion_jugador[0]][self.posicion_jugador[1]] == personaje_meta:
            self.tablero[self.posicion_jugador[0]][self.posicion_jugador[1]] = meta
        else:
            self.tablero[self.posicion_jugador[0]][self.posicion_jugador[1]] = espacio_piso

        self.posicion_jugador = nueva_posicion
        if self.tablero[self.posicion_jugador[0]][self.posicion_jugador[1]] == meta:
            self.tablero[self.posicion_jugador[0]][self.posicion_jugador[1]] = personaje_meta
        elif self.tablero[self.posicion_jugador[0]][self.posicion_jugador[1]] == caja_meta:
            # Verificamos si la caja_meta está al lado de una meta
            if [self.posicion_jugador[0] - movimiento[0], self.posicion_jugador[1] - movimiento[1]] in self.posiciones_metas:
                # Si es así, cambiamos la posición de la caja_meta a meta
                self.tablero[self.posicion_jugador[0]][self.posicion_jugador[1]] = meta
            else:
                self.tablero[self.posicion_jugador[0]][self.posicion_jugador[1]] = personaje
        else:
            self.tablero[self.posicion_jugador[0]][self.posicion_jugador[1]] = personaje

    def verificar_condicion_victoria(self):
        for meta in self.posiciones_metas:
            if self.tablero[meta[0]][meta[1]] != caja_meta:
                return False
        return True

    def cargar_siguiente_mapa(self):
        self.indice_mapa_actual += 1
        if self.indice_mapa_actual >= len(self.mapas):
            print("¡Felicidades! ¡Has completado todos los niveles!")
            return False
        else:
            print("¡Has completado el nivel! Pasando al siguiente nivel...")
            self.generar_tablero()
            return True

def main():
    juego = JuegoSokoban()
    juego.generar_tablero()

    while True:
        juego.imprimir_tablero()
        movimiento = input("Ingresa tu movimiento (w/a/s/d): ")
        juego.mover_jugador(movimiento)
        if juego.verificar_condicion_victoria():
            if not juego.cargar_siguiente_mapa():
                break

if __name__ == "__main__":
    personaje = '*'
    caja = '🐚'
    meta = '🦐'
    paredes = '🐋'
    espacio_piso = '  '
    personaje_meta = 'PM'
    caja_meta = 'CM'
    
    mapa1 = [
        [paredes, paredes, paredes, paredes, paredes, paredes, paredes],
        [paredes, espacio_piso, espacio_piso, espacio_piso, espacio_piso, espacio_piso, paredes],
        [paredes, espacio_piso, caja, espacio_piso, espacio_piso, espacio_piso, paredes],
        [paredes, espacio_piso, espacio_piso, meta, espacio_piso, espacio_piso, paredes],
        [paredes, espacio_piso, caja, espacio_piso, meta, personaje, paredes],
        [paredes, espacio_piso, espacio_piso, espacio_piso, espacio_piso, espacio_piso, paredes],
        [paredes, paredes, paredes, paredes, paredes, paredes, paredes],
    ]
    
    mapa2 = [
        [paredes, paredes, paredes, paredes, paredes, paredes, paredes],
        [paredes, espacio_piso, espacio_piso, espacio_piso, espacio_piso, espacio_piso, paredes],
        [paredes, espacio_piso, personaje, espacio_piso, espacio_piso, espacio_piso, paredes],
        [paredes, espacio_piso, caja, espacio_piso, espacio_piso, espacio_piso, paredes],
        [paredes, espacio_piso, caja, espacio_piso, espacio_piso, meta, paredes],
        [paredes, espacio_piso, espacio_piso, espacio_piso, espacio_piso, meta, paredes],
        [paredes, paredes, paredes, paredes, paredes, paredes, paredes],
    ]
    mapa3 = [
    [paredes, paredes, paredes, paredes, paredes, paredes, paredes],
    [paredes, espacio_piso, espacio_piso, espacio_piso, espacio_piso, espacio_piso, paredes],
    [paredes, caja, caja, caja, espacio_piso, espacio_piso, paredes],
    [paredes, espacio_piso, espacio_piso, espacio_piso, espacio_piso, espacio_piso, paredes],
    [paredes, espacio_piso, meta, espacio_piso, espacio_piso, personaje, paredes],
    [paredes, meta, espacio_piso, meta, espacio_piso, espacio_piso, paredes],
    [paredes, paredes, paredes, paredes, paredes, paredes, paredes],
]
    main()
