# A Linked List

class Node():

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
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
        """Iterate through the linked list"""
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
        return self.head == None

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        node = Node(item)

        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        return

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        node = Node(item)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
        self.head = node
        return True

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        current = self.head
        while current is not None:
            if quality(current.data) is True:
                return current.data
            current = current.next
        return None

    def replace(self, quality, item):
        """Replace an item from this linked list satisfying the given quality"""
        current = self.head
        while current is not None:
            if quality(current.data) is True:
                current.data = item
            current = current.next
        raise ValueError('Cannot replace from empty Linked List')

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        if self.head is None:
            raise ValueError('Cannot delete from empty Linked List')

        current = self.head

        # If item is first!
        if current.data == item:
            self.head = current.next
            if self.head is None:
                self.tail = None
            return

        while current.next is not None:
            if current.next.data == item:
                newNext = current.next.next
                if newNext is not None:
                    current.next = newNext
                else:
                    current.next = None
                    self.tail = current
                return
            current = current.next

        raise ValueError('Cannot delete this element from the linked list')

