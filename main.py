import sys
from Classes.Lists.LinkedList import LinkedList
from Classes.Lists.Doubly_LinkedList import DoublyLinkedList
from Classes.Lists.Circle_LinkedList import CircleLinkedList
from Classes.Lists.DoublyCircle_LinkedList import DoublyCircleLinkedList
from Classes.Auto import Auto


def operation(value):
    automatic = Auto()
    match value:

        case 1:
            s_list = LinkedList()
            automatic.Auto_Add_LinkedList(s_list)
            automatic.Auto_Delete_LinkedList(s_list)
            automatic.Auto_Search_LinkedList(s_list)
            print()

        case 2:
            c_list = CircleLinkedList()
            automatic.Auto_Add_CircleLinkedList(c_list)
            automatic.Auto_Delete_CircleLinkedList(c_list)
            automatic.Auto_Search_CircleLinkedList(c_list)
            print()

        case 3:
            doubly_list = DoublyLinkedList()
            automatic.Auto_Add_DoublyLinkedList(doubly_list)
            automatic.Auto_Delete_DoublyLinkedList(doubly_list)
            automatic.Auto_Search_DoublyListLinked(doubly_list)
            print()

        case 4:
            cd_list = DoublyCircleLinkedList()
            automatic.Auto_Add_DoublyCircleLinkedList(cd_list)
            automatic.Auto_Delete_DoublyCircleLinkedList(cd_list)
            automatic.Auto_Search_DoublyCircleLinkedList(cd_list)
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
