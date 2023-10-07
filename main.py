from Classes.Lists.SimpleList import SimpleList
from Classes.Lists.LinkedList import ListLinked
from Classes.Lists.CircularList import CircularList
from Classes.Lists.DoublyLinkedList import CircularDoublyLinkedList


exit_program = False
while not exit_program:
    print(
        "# Ver todas las Listas #\n[1] Lista simple.\n[2] Lista circular.\n[3] Lista doble enlazada.\n[4] Lista circular doble enlazada.\n[5] Salir.")
    option = int(input("Ingresa una opción (1 - 5): "))
    print()
    if option == 1:
        s_list = SimpleList()
        s_list.add(1)
        s_list.add(10)
        s_list.add(100)
        s_list.add(1000)
        s_list.add(10000)
        s_list.show()
        s_list.search(100)
        s_list.delete(1)
        s_list.show()
        s_list.search(1)
        input()
    elif option == 2:

        c_list = CircularList()
        c_list.add(1)
        c_list.add(10)
        c_list.add(100)
        c_list.add(1000)
        c_list.add(10000)
        c_list.show()
        c_list.search(100)
        c_list.delete(1)
        c_list.show()
        c_list.search(1)
        input()
    elif option == 3:

        l_list = ListLinked()
        l_list.add(1)
        l_list.add(10)
        l_list.add(100)
        l_list.add(1000)
        l_list.add(10000)
        l_list.show()
        l_list.search(100)
        l_list.delete(1)
        l_list.show()
        l_list.search(1)
        input()
    elif option == 4:

        cd_list = CircularDoublyLinkedList()
        cd_list.add(1)
        cd_list.add(10)
        cd_list.add(100)
        cd_list.add(1000)
        cd_list.add(10000)
        cd_list.show()
        cd_list.search(100)
        cd_list.delete(1)
        cd_list.show()
        cd_list.search(1)
        input()
    elif option == 5:
        input("Fin del programa...")
        exit_program = True
    else:

        input("Ingresa un valor de (1 a 5)...")


