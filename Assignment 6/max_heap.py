class MaxHeap:
    def __init__(self, input_array):
        if input_array is None:
            raise ValueError("Input array cannot be None.")
        self.size = len(input_array)
        self.heap = input_array
        self.build_heap()

    def build_heap(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < self.size and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < self.size and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def get_heap(self):
        return self.heap

    def get_size(self):
        return self.size

    def contains(self, val):
        if val is None:
            raise ValueError("Value cannot be None.")

        for i in range(self.size):
            if self.heap[i] == val:
                return True

        return False

    def sort(self):
        for i in range(self.size - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.size -= 1
            self.heapify_down(0)

    def remove_max(self):
        if self.size == 0:
            return None

        max_element = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify_down(0)

        return max_element

