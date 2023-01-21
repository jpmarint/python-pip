from node import Node
from LinkedList import SinglyLinkedList

def runNode():
    print('*** Manual ***')
    node3 = Node("C", None)
    node2 = Node("B", node3)
    node1 = Node("A", node2)

    print(f'nodo 1: {node1} \n--> nodo 2: {node2}  \n--> nodo 3: {node3} \n')

    print("*** Iterative ***")
    head = None

    for count in range (1,5):
        head = Node(count, head)

    numero_nodo = 0
    while head != None:
        print(f'nodo {numero_nodo}: {head}', f'--- Data del nodo {numero_nodo}: {head. data}')
        head = head.next
        numero_nodo += 1

def runSinglyLinkedList():
    words = SinglyLinkedList()
    words.append('egg')
    words.append('ham')
    words.append('spam')

    current = words.tail

    while current:
        print(current.data)
        current = current.next

    for word in words.iter():
        print(word)

    words.search('spam')
    words.search('juice')

    words.clear()
    while current:
        print(current.data)
        current = current.next

def challengeSinglyLinkedLists():
    array = [2, 4, 6]
    datos = SinglyLinkedList()

    for i in array:
        datos.append(i)
    current = datos.tail
    
    while current:
        print(current.data)
        current = current.next

if __name__ == '__main__':
    
    #runNode()
    #runSinglyLinkedList()
    challengeSinglyLinkedLists()

