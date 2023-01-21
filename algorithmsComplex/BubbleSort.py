import random

def BubbleSort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): #O(n) * O(n) = O(n**2)
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j + 1], lista[j]
    return lista


if __name__ == '__main__':
    list_size = int(input("De que tamaño será la lista? "))
    numList = [random.randint(0,100) for i in range(list_size)]
    print(numList)
    OrderedList =  BubbleSort(numList)
    print(OrderedList)