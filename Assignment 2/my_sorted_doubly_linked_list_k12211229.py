from my_list_node import MyListNode


class MySortedDoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    def __init__(self, head: 'MyListNode' = None, tail: 'MyListNode' = None, size: int = 0) -> None:
        """Create a list and default values are None."""
        self._head = head
        self._tail = tail
        self._size = size

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def __str__(self) -> str:
        """Return linked list in string representation."""
        result = []
        node = self._head
        while node:
            result.append(node.elem)
            node = node.next_node
        return str(result)

    # The following methods have to be implemented.

    def get_value(self, index: int) -> int:
        """Return the value (elem) at position 'index' without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            (int): Retrieved value.

        Raises:
            ValueError: If the passed index is not an int or out of range.
        """
        if not isinstance(index, int) or index < 0 or index >= self._size:
            raise ValueError("Invalid index")
        node = self._head
        for a in range(index):
            node = node.next_node
        return node.elem

    def search_value(self, val: int) -> int:
        """Return the index of the first occurrence of 'val' in the list.

        Args:
            val (int): Value to be searched.

        Returns:
            (int): Retrieved index.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("Value must be an integer")
        node = self._head
        index = 0
        while node:
            if node.elem == val:
                return index
            node = node.next_node
            index += 1
        return -1

    def insert(self, val: int) -> None:
        """Add a new node containing 'val' to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("Value must be an integer")
        new_node = MyListNode(val)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            node = self._head
            prev = None
            while node and node.elem < val:
                prev = node
                node = node.next_node
            if prev is None:
                self._head = new_node
            else:
                prev.next_node = new_node
            new_node.prev_node = prev
            new_node.next_node = node
            if node is None:
                self._tail = new_node
        self._size += 1

    def remove_first(self, val: int) -> bool:
        """Remove the first occurrence of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether an element was successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("val must be an integer")

        try:
            idx = self._data.index(val)
        except ValueError:
            return False

        del self._data[idx]
        return True

    def remove_all(self, val: int) -> bool:
        """Remove all occurrences of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether elements were successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("val should be an integer")

        removed = False
        curr = self.head
        prev = None

        while curr is not None:
            if curr.data == val:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                removed = True
            else:
                prev = curr
            curr = curr.next

        return removed

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""
        unique_set = set()

        current = self.head
        prev = None

        while current:
            if current.val in unique_set:
                prev.next = current.next
                current = None
            else:
                unique_set.add(current.val)
                prev = current
            current = prev.next

    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the 'n' highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            ValueError: If the passed value n is not an int or out of range.
        """
        if not isinstance(n, int):
            raise ValueError("n must be an integer")
        if n <= 0:
            self.data = []
            return
        if n >= len(self.data):
            return
        self.data = sorted(self.data, reverse=True)[:n]

        def filter_odd(self) -> None:
            """Filter the list to only contain odd values."""
            self._list = [x for x in self._list if x % 2 == 0]

    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        self.num_list = list(filter(lambda x: x % 2 != 0, self.num_list))