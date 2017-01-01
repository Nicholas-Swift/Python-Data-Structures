# A Doubly Linked List


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def __contains__(self, item):
        """Does it contain the item"""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __nonzero__(self):
        """Will the linked list equate to false"""
        return not self.is_empty()

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list"""
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        node = Node(item)

        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
            self.tail.next.previous = self.tail
        self.tail = node
        self.size += 1
        return

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        node = Node(item)

        if self.is_empty():
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
        self.head = node
        self.size += 1
        return

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        if self.is_empty():
            raise ValueError('Cannot delete from empty Linked List')

        current = self.head

        # If item is first!
        if current.data == item:
            if current.next is not None:
                self.head = current.next
                self.head.previous = None
            else:
                self.head = None
                self.tail = None
            self.size -= 1
            return

        while current.next is not None:
            if current.next.data == item:
                newNext = current.next.next
                if newNext is not None:
                    current.next = newNext
                    current.next.previous = current
                else:
                    current.next = None
                    self.tail = current
                self.size -= 1
                return
            current = current.next

        raise ValueError('Element not found in the Linked List')

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        current = self.head
        while current is not None:
            if quality(current.data) == True:
                return current.data
            current = current.next
        return None


def test_linked_list():
    # Test appending
    print("Testing Appending")
    ll = DoublyLinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    # Test deleteing
    print("Testing Deleting")
    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    # Test iterable
    print("Testing Iterable")
    ll.append('a')
    ll.append('b')
    ll.append('c')
    ll.append('wow')
    for item in ll:
        print("item: ", item)
        print("\n")


if __name__ == '__main__':
    test_linked_list()

