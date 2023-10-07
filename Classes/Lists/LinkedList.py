from Classes.DoubleNode import Node


class ListLinked:
    def __init__(self):
        self.head = None
        self.last_node = None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.head.next = None
            self.head.back = None
            self.last_node = self.head
        else:
            self.last_node.next = new_node
            new_node.next = None
            new_node.back = self.last_node
            self.last_node = new_node

    def delete(self, data):
        copy_head = self.head
        copy_head_tracking = None
        search = False
        while copy_head is not None and not search:
            if copy_head.data == data:
                if copy_head == self.head:
                    self.head = self.head.next
                    self.head.back = None
                elif copy_head == self.last_node:
                    copy_head_tracking.next = None
                    self.last_node = copy_head_tracking
                else:
                    copy_head_tracking.next = copy_head.next
                    copy_head.next.back = copy_head_tracking
                search = True
            copy_head_tracking = copy_head
            copy_head = copy_head.next
        if not search:
            return

    def search(self, data):
        copy_head = self.head
        search = False
        while copy_head is not None and not search:
            if copy_head.data == data:
                print(f"- Dato[{data}] Existe en la lista")
                search = True
            copy_head = copy_head.next
        if not search:
            print(f"- Dato[{data}] No Existe en la lista")
            return

    def show(self):
        copy_head = self.head
        i = 1
        print("=== Mi Lista doblemente enlazada ===")
        while copy_head is not None:
            print(f"- Nodo[{i}] y dato: {copy_head.data}")
            copy_head = copy_head.next
            i += 1

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None
