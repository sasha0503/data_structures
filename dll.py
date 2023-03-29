class Node:
    """Node class for doubly linked list"""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Value {value} is not an integer.")
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def prepend(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Value {value} is not an integer.")
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.head.prev = Node(value)
            self.head.prev.next = self.head
            self.head = self.head.prev

    def remove(self, value):
        if self.head is None:
            raise ValueError(f"Value {value} not found in the list.")
        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                if current.next is not None:
                    current.next.prev = current
                else:
                    self.tail = current
                return
            current = current.next
        raise ValueError(f"Value {value} not found in the list.")

    def find(self, value) -> [int, None]:
        idx = 0
        current = self.head
        while current is not None:
            if current.value == value:
                return idx
            idx += 1
            current = current.next
        return None

    def swap_neighbors(self, p):
        """swap element before p with the element after p"""
        idx = self.find(p)
        if idx is None:
            raise ValueError(f"Value {p} not found in the list.")
        if idx == 0 or idx == len(self) - 1:
            raise ValueError(f"Value {p} is the first or the last element in the list.")
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        current.value, current.next.next.value = current.next.next.value, current.value

    def split(self, idx):
        """split the list into two lists at the given index
        the idx'th element will be in the last element in the first list"""

        if idx < 0 or idx >= len(self):
            raise ValueError(f"Index {idx} is out of bounds.")
        current = self.head
        for _ in range(idx):
            current = current.next
        result = DoublyLinkedList()
        result.head = current.next
        result.head.prev = None
        result.tail = self.tail
        current.next = None
        self.tail = current
        return self.__copy__(), result

    def __copy__(self):
        result = DoublyLinkedList()
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __add__(self, other):
        result = DoublyLinkedList()
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        current = other.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __str__(self):
        if self.head is None:
            return "[]"
        current = self.head
        result = "["
        while current is not None:
            result += str(current.value) + ", "
            current = current.next
        result = result[:-2] + "]"  # remove last comma and space
        return result

    def __len__(self):
        current = self.head
        result = 0
        while current is not None:
            result += 1
            current = current.next
        return result


def swap_k(dll1, dll2, k):
    """swap k'th element in dll1 with k'th element in dll2 if they are different"""
    if k < 0 or k >= len(dll1) or k >= len(dll2):
        raise ValueError(f"Index {k} is out of bounds.")
    current1 = dll1.head
    current2 = dll2.head
    for _ in range(k):
        current1 = current1.next
        current2 = current2.next
    if current1.value != current2.value:
        current1.value, current2.value = current2.value, current1.value


if __name__ == '__main__':
    dll = DoublyLinkedList()
    print(dll)
