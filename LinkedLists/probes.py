from node import Node

# * Creación de los nodos enlazados (linked list)
head = None
for count in range(1,6):
    head = Node(count, head)

# * Recorrer e imprimir valores de la lista
probe = head
print("Recorrido de la lista:")
while probe != None:
    print(probe.data)
    probe = probe.next

'''
Resultado -> Terminal
Recorrido de la lista:
5
4
3
2
1
'''

# * Busqueda de un elemento
probe = head
target_item = 2
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    print(f'Target item {target_item} has been found')
else:
    print(f"Target item doesn't exist")

'''
Resultado -> Terminal
Target item 2 has been found
'''

# * Remplazo de un elemento
probe = head
target_item = 3
new_item = "Z"

while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    probe.data = new_item
    print(f"{new_item} replace the old value in the node number {target_item}")
else:
    print(f"The target item {target_item} is not in the linked list")

'''
Resultado -> Terminal

Z replace the old value in the node number 3

Recorrido de la lista:
5
4
Z
2
1
'''

# * Insertar un nuevo elemento/nodo al inicio(head)
head = Node("F", head)

'''
Respuesta -> Terminal
Recorrido de la lista:
F
5
4
Z
2
1
'''

# * Insertar un nuevo elemento/nodo al final(tail)
new_node = Node("K")
if head is None:
    head = new_node
else:
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = new_node

'''
Recorrido de la lista:
F
5
4
Z
2
1
K
'''

# * Eliminar un elmento/nodo al inicio(head)
removed_item = head.data
head = head.next
print("Removed_item: ",end="")
print(removed_item)

'''
Resultado -> Terminal
Removed_item: F

Recorrido de la lista:
5
4
Z
2
1
K
'''

# * Eliminar un elmento/nodo al final(tail)
removed_item = head.data
if head.next is None:
    head = None
else:
    probe = head
    while probe.next.next != None:
        probe = probe.next
    removed_item = probe.next.data
    probe.next = None

print("Removed_item: ",end="")
print(removed_item)

'''
Removed_item: K
Recorrido de la lista:
5
4
Z
2
1 
'''

# * Agregar un nuevo elemento/nodo por "indice" inverso(Cuenta de Head - Tail)
# new_item = input("Enter new item: ")
# index = int(input("Enter the position to insert the new item: "))
new_item = "10"
index = 3

if head is None or index <= 0:
    head = Node(new_item, head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
    probe.next = Node(new_item, probe.next)

# * Agregar un nuevo elemento/nodo por "indice" inverso(Cuenta de Head - Tail)
'''
Recorrido de la lista:
5
4
Z
10
2
1
'''


# * Eliminar un nuevo elemento/nodo por "indice" inverso(Cuenta de Head - Tail)
index = 3

if head is None or index <= 0:
    removed_item = head.data
    head = head.next
    print(removed_item)
else:
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1
    removed_item = probe.next.data
    probe.next = probe.next.next

    print("Removed_item: ",end="")
    print(removed_item)

'''
Removed_item: 10
Recorrido de la lista:
5
4
Z
2
1
'''