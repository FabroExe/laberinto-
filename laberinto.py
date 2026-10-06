laberinto = [
    [1,  1,  1,  1,  0,  1,  1,  1,  1],   
    [-2, 0,  0, -1,  0,  1,  0,  1,  0],   
    [1,  1,  0,  1,  1,  1,  0,  1,  0],   
    [0,  1,  0, -1,  0,  0,  0, -1,  0],   
    [1,  1,  1,  1,  1,  1,  1,  1,  0],   
    [-1, 0,  0,  0,  0,  0,  0,  1,  1],   
    [1,  1,  1,  1, -1,  1,  1,  1,  0],   
    [1,  0,  0,  1,  0,  1,  0,  1,  0],   
    [1,  1, -1,  1,  1,  1,  0,  1,  1],   
]

FILAS = len(laberinto)
COLUMNAS = len(laberinto[0])

INICIO = (8, 0)   
FIN = (0, 0)      

VIDAS_INICIALES = 3

MOVIMIENTOS = [
    (1,  0, "ABAJO"),
    (0,  1, "DERECHA"),
    (-1, 0, "ARRIBA"),
    (0, -1, "IZQUIERDA"),
]

camino_solucion = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]
visitada = [[False for _ in range(COLUMNAS)] for _ in range(FILAS)]

paso_contador = 0          
solucion_encontrada = False


def es_valida(fila, col):
    """La celda existe, no es pared (0) y no ha sido visitada en el camino actual."""
    if fila < 0 or fila >= FILAS or col < 0 or col >= COLUMNAS:
        return False
    if laberinto[fila][col] == 0:
        return False
    if visitada[fila][col]:
        return False
    return True


def mostrar_matriz(matriz, titulo):
    print(f"\n{titulo}")
    encabezado = "      " + "  ".join(f"C{c}" for c in range(COLUMNAS))
    print(encabezado)
    for f in range(FILAS):
        fila_txt = f"F{f:<2} | "
        for c in range(COLUMNAS):
            valor = matriz[f][c]
            if (f, c) == INICIO:
                celda = "I"
            elif (f, c) == FIN:
                celda = "F"
            else:
                celda = str(valor)
            fila_txt += f"{celda:>3}"
        print(fila_txt)


def backtracking(fila, col, vidas, paso):
  
    global paso_contador, solucion_encontrada

    valor_celda = laberinto[fila][col]
    if (fila, col) not in (INICIO, FIN):
        if valor_celda == -1:
            vidas -= 1
        elif valor_celda == -2:
            vidas -= 2

    if vidas <= 0:
        print(f"  Paso {paso}: ({fila},{col}) -> vidas={vidas}. "
              f"SIN VIDAS, camino inviable. Retrocediendo...")
        return False

    visitada[fila][col] = True
    paso_contador += 1
    camino_solucion[fila][col] = paso_contador
    print(f"  Paso {paso}: avanza a ({fila},{col})  valor={valor_celda}  "
          f"vidas restantes={vidas}")

    if (fila, col) == FIN:
        print(f"  >>> Se alcanzo la celda de LLEGADA (F) en ({fila},{col}) "
              f"con {vidas} vida(s) restante(s).")
        solucion_encontrada = True
        return True

    for d_fila, d_col, nombre in MOVIMIENTOS:
        nueva_fila, nueva_col = fila + d_fila, col + d_col
        if es_valida(nueva_fila, nueva_col):
            print(f"      Intentando moverse {nombre} hacia "
                  f"({nueva_fila},{nueva_col})")
            if backtracking(nueva_fila, nueva_col, vidas, paso + 1):
                return True

    print(f"  Paso {paso}: ({fila},{col}) sin salidas validas. "
          f"Backtracking (deshace celda)...")
    visitada[fila][col] = False
    camino_solucion[fila][col] = 0
    paso_contador -= 1
    return False


def main():
    print("=" * 70)
    print(" PROBLEMA 1 - LABERINTO DEL RATON (Backtracking)")
    print("=" * 70)

    mostrar_matriz(laberinto, "LABERINTO ORIGINAL (9 x 9):")
    print(f"\nInicio (I): {INICIO}   Fin/Llegada (F): {FIN}")
    print(f"Vidas iniciales del raton: {VIDAS_INICIALES}")
    print(f"Orden de movimiento: ABAJO -> DERECHA -> ARRIBA -> IZQUIERDA")

    print("\n" + "-" * 70)
    print(" INICIANDO BUSQUEDA (avance paso a paso) ")
    print("-" * 70)

    exito = backtracking(INICIO[0], INICIO[1], VIDAS_INICIALES, 1)

    print("\n" + "=" * 70)
    if exito:
        print(" RESULTADO: EL RATON LOGRO SALIR DEL LABERINTO. ")
        print("=" * 70)
        mostrar_matriz(camino_solucion,
                        "MATRIZ DE CAMINO (numero = orden de paso recorrido):")
    else:
        print(" RESULTADO: EL RATON NO PUDO SALIR DEL LABERINTO "
              "(no existe camino viable). ")
        print("=" * 70)

    print()


if __name__ == "__main__":
    main()

print(" RESULTADO: EL RATON NO PUDO SALIR DEL LABERINTO ")