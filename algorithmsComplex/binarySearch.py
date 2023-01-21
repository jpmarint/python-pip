import random

def binarySearch(lista, comienzo, final, objective):
    print(f"Buscando {objective} entre {lista[comienzo]} y {lista[final - 1]}")
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objective:
        return True
    elif lista[medio] < objective:
        return binarySearch(lista, medio+1, final, objective)
    else:
        return binarySearch(lista, comienzo, medio-1, objective)


if __name__ == '__main__':
    list_size = int(input("De que tamño será la lista? "))
    objetive = int(input('Que número quieres encontrar? '))

    numList = sorted([random.randint(0,100) for i in range(list_size)])

    found =  binarySearch(numList, 0, len(numList), objetive)
    print(numList)
    print(f'El elemento {objetive} {"esta" if found else "No esta" } en la lista')