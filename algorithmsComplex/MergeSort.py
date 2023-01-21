import random

def MergeSort(lista):
    if len(lista) > 1:
        medio = len(lista)//2
        leftList = lista[:medio]
        rightList = lista[medio:]
        print(leftList, '*'*5, rightList)

        #llamada recursiva a cada mitad
        MergeSort(leftList)
        MergeSort(rightList)

        #Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador para la lista principal
        k=0

        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                lista[k] = leftList[i]
                i += 1
            else:
                lista[k] = rightList[j]
                j += 1

            k += 1

        while i < len(leftList):
            lista[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):
            lista[k] = rightList[j]
            j += 1
            k += 1

        print(f'Left {leftList}, right {rightList}')
        print(lista)
        print('-'*20)
 
    return lista


if __name__ == '__main__':
    list_size = int(input("De que tamaño será la lista? "))
    numList = [random.randint(0,100) for i in range(list_size)]
    print(numList)
    print("-"*2)
    OrderedList =  MergeSort(numList)
    print(OrderedList)