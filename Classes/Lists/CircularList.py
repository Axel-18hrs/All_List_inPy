from Classes.Node import Node


class CircularList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.head.next = self.head
            self.last_node = self.head
        else:
            self.last_node.next = new_node
            new_node.next = self.head
            self.last_node = new_node

    def delete(self, data):
        copy_head = self.head
        copy_head_tracking = None
        search = False
        if self.is_empty():
            return
        while not search or copy_head != self.head:
            if copy_head.data == data:
                if copy_head == self.head:
                    self.head = self.head.next
                    self.last_node.next = self.head
                elif copy_head == self.last_node:
                    copy_head_tracking.next = self.head
                    self.last_node = copy_head_tracking
                else:
                    copy_head_tracking.next = copy_head.next
                search = True
            copy_head_tracking = copy_head
            copy_head = copy_head.next
        if not search:
            return

    def search(self, data):
        copy_head = self.head
        if self.is_empty():
            return

        while copy_head.next != self.head:
            if copy_head.data == data:
                print(f"- Dato[{data}] Existe en la lista")
                return
            copy_head = copy_head.next
        print(f"- Dato[{data}] No Existe en la lista")
        return

    def show(self):
        if self.is_empty():
            print("Lista vacía")
            return
        copy_head = self.head
        i = 1
        print("=== Mi lista Circular ===")
        while copy_head.next != self.head:
            print(f"- Nodo[{i}] y dato: {copy_head.data}")
            copy_head = copy_head.next
            i += 1
        return

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None
