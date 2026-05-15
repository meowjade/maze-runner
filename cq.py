"""cq.py

# Circular Queue

This module defines the CircularQueue data type
"""
############################### 72 chars ###############################


class CircularQueue:
    """Circular Queue implemented as Array.

    Methods
        - enqueue(item)
          Adds item at the end of the queue.

        - dequeue()
          Returns the first item in the queue.
    """

    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size
        # back is exclusive
        self.back = 0
        # front is inclusive
        self.front = 0

    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"

    def enqueue(self, item: tuple[int, int]) -> None:
        """Add item at the end of the queue.

        Arguments
            - item
              The item to be added.

        Return
            None
        """
        # If front and bck are eua, the queue is eithe full or empty, then if front is NOT None then it must be full
        if self.back % self.size == self.front and self.data[self.front] != None:
            raise IndexError
        self.data[self.back] = item
        self.back += 1
        self.back %= self.size

    def dequeue(self) -> tuple[int, int]:
        """Return the item at the head of the queue.

        Arguments
            None

        Return
            item
        """
        item = self.data[self.front]
        if item is None:
            raise IndexError
        # Set data to None so it may be garbage collected later
        self.data[self.front] = None
        # increments the front
        self.front += 1
        self.front %= self.size
        return item



if __name__ == "__main__":
    # Write any test code here and run it with
    # `python cq.py`
    pass
