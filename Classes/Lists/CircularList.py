from Classes.Node import Node
from Classes.Lists.Lists_Interface import ListBase


class CircularList(ListBase):

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)

        # case 1: List is empty
        if self.head is None:
            self.tail = new_node
            self.head = new_node
            new_node.next = self.head
            return

        # case 2: List is not empty
        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node
        pass

    def delete(self, data):
        # case 1: the head has the courage to delete
        if self.head.data == data:
            self.head = self.head.next

        # case 2: Any of the following nodes has the value to be deleted
        current_node = self.head
        while current_node.next is not self.head:
            if current_node.next.data == data:
                # caso 2.1: cuando el nodo a eliminar es la cola de la lista
                if current_node.next == self.tail:
                    current_node.next = self.tail.next
                    self.tail = current_node
                    return
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # case 3: When we reached the end of the list and it was not found
        print("Doesn't search")
        pass

    def transverse(self):
        # case 1: List is empty
        if self.head is None:
            print("List is empty")
            return

        # case 2: List is not empty or is not None
        current_node = self.head
        while True:
            print(current_node.data)
            current_node = current_node.next
            if current_node is self.head:
                break
        pass

    def transverse_reverse(self):
        pass

    def exist(self, data):
        # case 1: List is empty
        if self.head is None:
            print("List is empty")
            return False

        # case 2: List is not empty or is not None
        current_node = self.head
        while True:
            if current_node.data == data:
                return True
            current_node = current_node.next
            if current_node is self.head:
                break

        # case 3: We reached the end and found nothing
        return False
        pass

    # made by israel and refactored for me
    def search(self, data):
        # case 1: List is empty
        if self.head is None:
            print("List is empty")
            return

        # case 2: List is not empty or is not None
        current_node = self.head
        while True:
            # case 2.1: We reached the end and found nothing
            if current_node.data == data:
                print(f"- Dato[{data}] Existe en la lista")
                return

            current_node = current_node.next
            if current_node is self.head:
                print(f"- Dato[{data}] No Existe en la lista")
                return
        pass
    
    def show(self):
        # case 1: List is empty
        if self.head is None:
            print("List is empty")
            return

        # case 2: List is not empty or is not None
        print("=== Mi lista Circular ===")
        i = 1
        current_node = self.head
        while True:
            print(f"- Nodo[{i}] y dato: {current_node.data}")
            current_node = current_node.next
            i += 1
            if current_node is self.head:
                break
        pass
                