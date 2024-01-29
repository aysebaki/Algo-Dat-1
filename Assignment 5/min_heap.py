from typing import Optional


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = len(self.heap)

    def get_size(self) -> int:
        """
        @return number of elements in the min heap
        """
        return self.size

    def is_empty(self) -> bool:
        """
        @return True if the min heap is empty, False otherwise
        """
        return self.size == 0

    def insert(self, integer_val: int) -> None:
        """
        inserts integer_val into the min heap
        @param integer_val: the value to be inserted
        @raises ValueError if integer_val is None or not an int
        """
        if integer_val is None or not isinstance(integer_val, int):
            raise ValueError("ERROR: integer_val must be an int and not None")
        self.heap.append(integer_val)
        self.size += 1
        self.up_heap(self.size -1)

    def get_min(self) -> Optional[int]:
        """
        returns the value of the minimum element of the PQ without removing it
        @return the minimum value of the PQ or None if no element exists
        """
        return None if self.is_empty() else self.heap[0]

    def remove_min(self) -> Optional[int]:
        """
        removes the minimum element from the PQ and returns its value
        @return the value of the removed element or None if no element exists
        """
        if self.is_empty():
            return None
        min_val = self.heap[0]
        last_val = self.heap.pop()
        self.size -= 1
        if not self.is_empty():
            self.heap[0] = last_val
            self.down_heap(0)
        return min_val

    def up_heap(self, index: int) -> None:
        """
        Helper method to percolate the element up to its correct position
        after insertion.
        """
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def down_heap(self, index: int) -> None:
        """
        Helper method to percolate the element down to its correct position
        after removal.
        """
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < self.size and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < self.size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.down_heap(smallest)