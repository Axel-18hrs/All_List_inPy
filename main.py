import sys
import random
from Classes.Lists.LinkedList import LinkedList
from Classes.Lists.Doubly_LinkedList import DoublyLinkedList
from Classes.Lists.Circle_LinkedList import CircleLinkedList
from Classes.Lists.DoublyCircle_LinkedList import DoublyCircleLinkedList


def operation(value):
    match value:
        case 1:
            s_list = LinkedList()
            s_list.add(random.randint(1, 1000))
            s_list.add(random.randint(1, 1000))
            s_list.add(random.randint(1, 1000))
            s_list.add(random.randint(1, 1000))
            s_list.add(random.randint(1, 1000))
            s_list.show()
            s_list.search(random.randint(1, 1000))
            s_list.delete(random.randint(1, 1000))
            s_list.show()
            s_list.search(random.randint(1, 1000))
            print()

        case 2:
            c_list = CircleLinkedList()
            c_list.add(random.randint(1, 1000))
            c_list.add(random.randint(1, 1000))
            c_list.add(random.randint(1, 1000))
            c_list.add(random.randint(1, 1000))
            c_list.add(random.randint(1, 1000))
            c_list.show()
            c_list.search(random.randint(1, 1000))
            c_list.delete(random.randint(1, 1000))
            c_list.show()
            c_list.search(random.randint(1, 1000))
            print()

        case 3:
            doubly_list = DoublyLinkedList()
            doubly_list.add(random.randint(1, 1000))
            doubly_list.add(random.randint(1, 1000))
            doubly_list.add(random.randint(1, 1000))
            doubly_list.add(random.randint(1, 1000))
            doubly_list.add(random.randint(1, 1000))
            doubly_list.show()
            doubly_list.show_reverse()
            doubly_list.search(random.randint(1, 1000))
            doubly_list.delete(random.randint(1, 1000))
            doubly_list.show()
            doubly_list.show_reverse()
            doubly_list.search(random.randint(1, 1000))
            print()

        case 4:
            cd_list = DoublyCircleLinkedList()
            cd_list.add(random.randint(1, 1000))
            cd_list.add(random.randint(1, 1000))
            cd_list.add(random.randint(1, 1000))
            cd_list.add(random.randint(1, 1000))
            cd_list.add(random.randint(1, 1000))
            cd_list.show()
            cd_list.show_reverse()
            cd_list.search(random.randint(1, 1000))
            cd_list.delete(random.randint(1, 1000))
            cd_list.show()
            cd_list.show_reverse()
            cd_list.search(random.randint(1, 1000))
            print()

        case 5:
            input("Fin del programa...")
            sys.exit()

        case x:
            input("Ingresa un valor de (1 a 5)...")


while True:
    print("# Ver todas las Listas #\n" +
          "[1] Lista simple.\n" +
          "[2] Lista circular.\n" +
          "[3] Lista doble enlazada.\n" +
          "[4] Lista circular doble enlazada.\n" +
          "[5] Salir.")

    try:
        operation(int(input("Ingresa una opción (1 - 5): ")))

    except ValueError:
        print()
        input("Ingresa un valor de (1 a 5)...")
        print("\n" * 10)
