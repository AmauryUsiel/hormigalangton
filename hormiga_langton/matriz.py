class Matriz:
    def __init__(self, ancho, altura, matriz=None):

        if matriz is None:
            self.ancho = ancho
            self.altura = altura
            self.matriz = [
                [0 for columnas in range(0, ancho)] for filas in range(0, altura)
            ]
        else:
            self.ancho = len(matriz[0])
            self.altura = len(matriz)
            self.matriz = matriz

    def obt_color_casilla(self, posicion):
        x, y = posicion
        return self.matriz[y][x]

    def est_color_casilla(self, posicion, color):
        x, y = posicion
        self.matriz[y][x] = color