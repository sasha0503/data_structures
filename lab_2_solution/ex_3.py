class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def delete_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        min_element = self.heap[0]
        last_element = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last_element
            self._sift_down(0)

        return min_element

    def _sift_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def _sift_down(self, index):
        while index * 2 + 1 < len(self.heap):
            child_index = index * 2 + 1
            if child_index + 1 < len(self.heap) and self.heap[child_index + 1] < self.heap[child_index]:
                child_index += 1
            if self.heap[child_index] < self.heap[index]:
                self.heap[child_index], self.heap[index] = self.heap[index], self.heap[child_index]
                index = child_index
            else:
                break


# Приклад використання

# Створення бінарної піраміди
heap = BinaryHeap()

# Додавання елементів до піраміди
values = [9, 5, 7, 1, 3, 10, 6, 2, 8, 4, 15, 12, 11, 14, 13, 17, 19, 18, 16, 20]
for value in values:
    heap.insert(value)

# Виведення побудованої піраміди
print("Побудована бінарна піраміда:")
print(heap.heap)

# Видалення мінімального елемента з піраміди
min_element = heap.delete_min()
print("Мінімальний елемент:", min_element)

# Виведення піраміди після видалення мінімального елемента
print("Піраміда після видалення мінімального елемента:")
print(heap.heap)
