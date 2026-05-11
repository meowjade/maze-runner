"""datastruct.py

# Data Structures

This module defines the LinkedList abstract data type
"""
############################### 72 chars ###############################


class Node:
    """Represents a node in a linkedlist.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
          The next node in the linkedlist, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """

    def __init__(self, data: tuple[int, int]):
        self._data = data
        self.next = None

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self) -> tuple[int, int]:
        """Return the data stored in the node.

        Arguments
            None

        Return
            tuple[int, int]
        """
        return self._data

class LinkedList:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        None

    Methods
        - length() -> int
        - get(index) -> item
        - insert(index, item) -> None
        - append(item) -> None
        - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
            None

        Return
            length of linkedlist as an integer (zero or positive)
        """
        current = self._head
        size = 0
        while current is not None:
            current = current.next
            size += 1
        return size

    def get(self, n: int) -> tuple[int, int]:
        """Returns item at n-th node.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Returns
            item

        Raises
            IndexError if n >= length
        """
        if n < 0:
            raise IndexError
        
        current = self._head
        index = 0
        while current is not None:
            if index == n:
                return current.get()
            current = current.next
            index += 1
        raise IndexError
        
    def insert(self, n: int, item: tuple[int, int]) -> None:
        """Insert item into linkedlist at position n.

        If n == 0, inserts item at the head.
        If n == length, appends item at the tail of the linkedlist.

        Arguments
            - n: int
              sequence number of item to be inserted.

        Raises
            IndexError if n > length
        """
        if n < 0:
            raise IndexError

        if n == 0:
            item_node = Node(item)
            current = self._head
            self._head = item_node
            item_node.next = current
            return
        
        previous = None
        current = self._head
        index = 0
        while True:
            if index == n:
                # found the index to add the element
                item_node = Node(item)
                if current is None:
                    previous.next = item_node
                else:
                    previous.next = item_node
                    item_node.next = current

                # Found correct index to insert, stop now
                return
            elif current is None:
                # Reached past the end of the linked list, raise error.
                raise IndexError
            previous = current
            current = current.next
            index += 1

                
    def append(self, item: tuple[int, int]) -> None:
        """Append item at the end of linkedlist.

        Arguments
            - item
              The item to be appended.

        Returns
            None
        """
        # Replace the line below with your code
        
        current = self._head
        item_node = Node(item)
        # Empty LinkedList
        if current is None:
            self._head = item_node
            return
        while current.next is not None:
            current = current.next
        current.next = item_node
        
    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Raises
            IndexError if n >= length
        """
        if n < 0:
            raise IndexError
            
        if n == 0:
            self._head = self._head.next
            return

        # Replace the line below with your code
        previous = None
        current = self._head
        index = 0
        while current is not None:
            if index == n:
                # Set previous node to point to current's next node instead
                previous.next = current.next    
                return
            previous = current
            current = current.next
            index += 1
        raise IndexError
    
    def contains(self, item: tuple[int, int]) -> bool:
        """Checks whether an item is in the linkedlist.
        Returns a boolean value to indicate the status of the search.

        Arguments
            - item
              The item to be searched for.

        Returns
            True if item is found in the linkedlist,
            otherwise False
        """
        
        current = self._head
        while current is not None:
            if current.get() == item:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python datastruct.py`
    ll = LinkedList()
    ll.append((4,5))
    ll.insert(0, (1,2))
    # ll.insert(1, (3, 69))

    print(ll.get(0))
    print(ll.get(1))
    # print(ll.get(2))
    print(ll.length())


