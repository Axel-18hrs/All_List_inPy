import random


class Auto:

    def Auto_Add_LinkedList(self, LinkedList):
        cant = int(input("Cuantos datos quieres añadir: "))
        for i in range(cant):
            LinkedList.add(random.randint(0, 24))
        LinkedList.show()

    def Auto_Remove_LinkedList(self, LinkedList):
        cant = int(input("Cuantos datos quieres borrar: "))
        for i in range(cant):
            LinkedList.remove(random.randint(0, 24))
        LinkedList.show()

    def Auto_Search_LinkedList(self, LinkedList):
        cant = int(input("Cuantos datos quieres buscar: "))
        for i in range(cant):
            LinkedList.search(random.randint(0, 24))

    def Auto_Add_CircleLinkedList(self, CircleLinkedList):
        cant = int(input("Cuantos datos quieres añadir: "))
        for i in range(cant):
            CircleLinkedList.add(random.randint(0, 24))
        CircleLinkedList.show()

    def Auto_Remove_CircleLinkedList(self, CircleLinkedList):
        cant = int(input("Cuantos datos quieres borrar: "))
        for i in range(cant):
            CircleLinkedList.remove(random.randint(0, 24))
        CircleLinkedList.show()

    def Auto_Search_CircleLinkedList(self, CircleLinkedList):
        cant = int(input("Cuantos datos quieres buscar: "))
        for i in range(cant):
            CircleLinkedList.search(random.randint(0, 24))

    def Auto_Add_DoublyLinkedList(self, DoublyLinkedList):
        cant = int(input("Cuantos datos quieres añadir: "))
        for i in range(cant):
            DoublyLinkedList.add(random.randint(0, 24))
        DoublyLinkedList.show()
        DoublyLinkedList.show_reverse()

    def Auto_Remove_DoublyLinkedList(self, DoublyLinkedList):
        cant = int(input("Cuantos datos quieres borrar: "))
        for i in range(cant):
            DoublyLinkedList.remove(random.randint(0, 24))
        DoublyLinkedList.show()
        DoublyLinkedList.show_reverse()

    def Auto_Search_DoublyListLinked(self, DoublyLinkedList):
        cant = int(input("Cuantos datos quieres buscar: "))
        for i in range(cant):
            DoublyLinkedList.search(random.randint(0, 24))

    def Auto_Add_DoublyCircleLinkedList(self, DoublyCircleLinkedList):
        cant = int(input("Cuantos datos quieres añadir: "))
        for i in range(cant):
            DoublyCircleLinkedList.add(random.randint(0, 24))
        DoublyCircleLinkedList.show()
        DoublyCircleLinkedList.show_reverse()

    def Auto_Remove_DoublyCircleLinkedList(self, DoublyCircleLinkedList):
        cant = int(input("Cuantos datos quieres borrar: "))
        for i in range(cant):
            DoublyCircleLinkedList.remove(random.randint(0, 24))
        DoublyCircleLinkedList.show()
        DoublyCircleLinkedList.show_reverse()

    def Auto_Search_DoublyCircleLinkedList(self, DoublyCircleLinkedList):
        cant = int(input("Cuantos datos quieres buscar: "))
        for i in range(cant):
            DoublyCircleLinkedList.search(random.randint(0, 24))
