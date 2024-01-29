class RadixSort:
    def __init__(self):
        self.base = 7
        self.bucket_list_history = []

    def get_bucket_list_history(self):
        return self.bucket_list_history

    def sort(self, input_array):
        """
        Sorts a given list using radix sort in descending order
        @param input_array: List of positive integer numbers to be sorted
        @returns: A sorted list
        """
        self.bucket_list_history.clear()  # Clear history list at the beginning of sorting

        # Get the maximum number of digits in the input array
        max_digits = len(str(max(input_array)))

        # Iterate over each digit position from least significant to most significant
        for pos in range(max_digits):
            # Create empty buckets
            buckets = [[] for _ in range(self.base)]

            # Distribute elements into buckets based on the current digit
            for num in input_array:
                digit = (num // (self.base ** pos)) % self.base
                buckets[digit].append(num)

            # Take a snapshot of the bucket list
            self._add_bucket_list_to_history(buckets)

            # Merge the buckets into a single list
            input_array = []
            for bucket in buckets:
                input_array.extend(bucket)

        # Return the sorted list in descending order
        return input_array[::-1]

    def _add_bucket_list_to_history(self, bucket_list):
        """
        This method creates a snapshot (clone) of the bucket list and adds it to the bucket list history.
        @param bucket_list: The current bucket list after assigning all elements to be sorted to the buckets.
        """
        arr_clone = [bucket[:] for bucket in bucket_list]
        self.bucket_list_history.append(arr_clone)
