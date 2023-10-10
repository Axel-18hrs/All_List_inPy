from Classes.Node import Node


class SimpleList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        if self.exist(new_node.data):
            return
        else:
            copy_head = self.head
            while copy_head.next is not None:
                copy_head = copy_head.next
            copy_head.next = new_node

    def delete(self, data):
        copy_head = self.head
        copy_head_tracking = None
        if self.is_empty():
            return
        if self.head is not None:
            copy_head = self.head
            while copy_head.next is not None and copy_head.data != data:
                copy_head_tracking = copy_head
                copy_head = copy_head.next
            if copy_head.data != data:
                return
            else:
                if self.head == copy_head:
                    self.head = copy_head.next
                else:
                    copy_head_tracking.next = copy_head.next
                copy_head = None

    def search(self, data):
        if self.is_empty():
            print("Lista vacia...")
        if self.head is not None and self.head.data == data:
            print(f"- Dato[{data}] Existe en la lista")
            return
        copy_head = self.head
        while copy_head.next is not None:
            if copy_head.next.data == data:
                break
            copy_head = copy_head.next
        if copy_head.next is not None and copy_head.next.data == data:
            print(f"- Dato[{data}] Existe en la lista")
            return
        print(f"- Dato[{data}] No Existe en la lista")

    def show(self):
        if self.is_empty():
            print("Lista vacia")
            return
        copy_head = self.head
        i = 1
        print("=== Mi lista simple ===")
        while copy_head is not None:
            print(f"- Nodo[{i}] y dato: {copy_head.data}")
            copy_head = copy_head.next
            i += 1

    def exist(self, data):
        if self.is_empty():
            return False
        if self.head is not None and self.head.data == data:
            return True
        copy_head = self.head
        while copy_head.next is not None:
            if copy_head.next.data >= data:
                break
            copy_head = copy_head.next
        if copy_head.next is not None and copy_head.next.data == data:
            return True
        return False

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None
