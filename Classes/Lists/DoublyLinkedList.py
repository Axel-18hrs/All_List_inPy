from Classes.DoubleNode import Node


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.head.next = new_node
            self.head.back = new_node
            self.last_node = self.head
        else:
            self.last_node.next = new_node
            new_node.next = self.head
            new_node.back = self.last_node
            self.last_node = new_node
            self.head.back = new_node

    def delete(self, data):
        copy_head = self.head
        copy_head_tracking = None
        buscar = False
        while not buscar or copy_head != self.head:
            if copy_head.data == data:
                if copy_head == self.head:
                    self.head = self.head.next
                    self.head.back = self.last_node
                    self.last_node.next = self.head
                elif copy_head == self.last_node:
                    copy_head_tracking.next = self.head
                    self.last_node = copy_head_tracking
                else:
                    copy_head_tracking.next = copy_head.next
                    copy_head.next.back = copy_head_tracking
                buscar = True
            copy_head_tracking = copy_head
            copy_head = copy_head.next
        if not buscar:
            return

    def search(self, data):

        if self.head.data == data:
            print(f"- Dato[{data}] Existe en la lista")
            return

        copy_head = self.head
        while copy_head.next != self.head:
            if copy_head.data == data:
                print(f"- Dato[{data}] Existe en la lista")
                return
            copy_head = copy_head.next
        print(f"- Dato[{data}] No Existe en la lista")
        return

    def show(self):
        copy_head = self.head
        i = 1
        print("=== Mi Lista doblemente enlazada circular ===")
        while copy_head.next != self.head:
            print(f"- Nodo[{i}] y dato: {copy_head.data}")
            copy_head = copy_head.next
            i += 1

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None
