import random


def linealSearch(list, objective):
    match = False

    for element in list: #O(n)
        if element == objective:
            match = True
            break

    return match

if __name__ == '__main__':
    list_size = int(input("De que tamño será la lista? "))
    objetive = int(input('Que número quieres encontrar? '))

    numList = [random.randint(0,100) for i in range(list_size)]

    found =  linealSearch(numList, objetive)
    print(numList)
    print(f'El elemento {objetive} {"esta" if found else "No esta" } en la lista')