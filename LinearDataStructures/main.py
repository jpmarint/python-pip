from arrays import Array
from grids import Grid, Cube

def runArray():
    size =  int(input('Ingrese el tamaño del arreglo: '))
    arreglo =  Array(size)
    print('Longitud del arreglo: ', arreglo.__len__())
    [arreglo.__setItem__(i, i+1) for i in range(arreglo.__len__())]
    print("Arreglo con datos secuenciales: \n", arreglo.__str__())
    arreglo.__randReplace__()
    print("Arreglo con datos al azar: \n", arreglo.__str__())
    print("Sumatoria del arreglo: ", arreglo.__sum__())

def runGrid():
    matrix = Grid(3, 3)
    print(matrix)
    for row in range(matrix.get_height()):
        for column in range(matrix.get_width()):
            matrix[row][column] = row * column

    print(matrix)
    matrix.get_height()
    matrix.get_width()
    matrix.__getitem__()
    matrix.__getitem__(1)
    matrix.__getitem__(2)[0]
    matrix.__str__()

def runCube():
    cubo = Cube(3,3,3)
    for row in range(cubo.get_height()):
        for column in range(cubo.get_width()):
            for depth in range (cubo.get_depth()):
                cubo[row][column][depth] = f'[fila {row}, columna {column}, casilla {depth}]'
    print(cubo)

if __name__ == '__main__':
    #runArray()
    #runGrid()
    runCube()