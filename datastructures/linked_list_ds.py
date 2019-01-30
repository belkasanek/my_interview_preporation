from exceptions import *

class SinglyLinkedList:
    """Singly linked list"""
    
    class _Node:
        """Lightweight, nonpublic class for storing  a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        """Create an empty linked list."""
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the linked list."""
        return self._size
    
    def __str__(self):
        """Return string represintation of the linked list."""
        if self._size > 0:
            result = []
            initial = self._head
            result.append(str(initial._element))
            for i in range(self._size-1):
                initial = initial._next
                result.append(str(initial._element))
            result = ', '.join(result)
        else:
            result = ''
        return 'Linked list: head [' + result + '] tail'
    
    def is_empty(self):
        """Return True if the linked list is empty."""
        return self._size == 0
    
    def add_first(self, e):
        """Add an element e to the head of the linked list."""
        self._head = self._Node(e, self._head)
        if self._tail == None:
            self._tail = self._head
        self._size += 1
        
    def add_last(self, e): 
        """Add an element e to the tail of the linked list."""
        newest = self._Node(e, None)
        if self._head == None:
            raise Empty('Linked list is empty')
        self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def remove_first(self):
        """Remove the element from the head of the linked list."""
        if self.is_empty():
            raise Empty('Linked list is empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        return result
    
class LinkedStack:
    """LIFO Stack implementation using singly linked list for storage."""
    
    class _Node:
        """Lightweight, nonpublic class for storing  a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size
    
    def __str__(self):
        """Return string represintation of the stack."""
        if self._size > 0:
            result = []
            initial = self._head
            result.append(str(initial._element))
            for i in range(self._size-1):
                initial = initial._next
                result.append(str(initial._element))
            result = ', '.join(result)
        else:
            result = ''
        return 'Stack: top [' + result + '] bottom'
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0
    
    def push(self, e):
        """Add an element e to the head of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        """Remove and return the element from the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        return result
    
    def top(self):
        """Return (but not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    
class LinkedQueue:
    """LIFO Queue implementation using singly linked list for storage."""
    
    class _Node:
        """Lightweight, nonpublic class for storing  a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def __str__(self):
        """Return string represintation of the queue."""
        if self._size > 0:
            result = []
            initial = self._head
            result.append(str(initial._element))
            for i in range(self._size-1):
                initial = initial._next
                result.append(str(initial._element))
            result = ', '.join(result)
        else:
            result = ''
        return 'Queue: front [' + result + '] end'
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but not remove) the element at the top of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    
    def enqueue(self, e):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def dequeue(self):
        """Remove and return the first element from the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result
    
    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            second = self._head._next
            self._head._next = None
            self._tail._next = self._head
            self._tail = self._head
            self._head = second
            
class CircularQueue:
    """Queue implementation using circulary linked list for storage."""
    
    class _Node:
        """Lightweight, nonpublic class for storing  a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        """Create an empty queue."""
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def __str__(self):
        """Return string represintation of the queue."""
        if self._size > 0:
            result = []
            initial = self._tail
            result.append(str(initial._element))
            for i in range(self._size-1):
                initial = initial._next
                result.append(str(initial._element))
            result = ', '.join(result)
        else:
            result = ''
        return 'Queue: front [' + result + '] end'
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but not remove) the element at the top of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._tail._next._element
    
    def enqueue(self, e):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def dequeue(self):
        """Remove and return the first element from the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next
            
class _DoublyLinked:
    """A base class providing a doubly linked list representation."""
    
    class _Node:
        """Lightweight, nonpublic class for storing  a doubly linked node."""
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element, prev, next):
            self._element = element
            self._next = next
            self._prev = prev
    
    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer 
        self._trailer._prev = self._header 
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the list."""
        return self._size
    
    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add an element e between two existing nodes and retrun new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest 
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Delete nonsential node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
    
class LinkedDeque(_DoublyLinked):
    """Doubly-ended queue implementation based on a doubly linked list."""
    
    def first(self):
        """Return (but not remove) the element at the front of the deque."""
        if self._size == 0:
            raise Empty('Deque is empty.')
        return self._header._next._element
    
    def last(self):
        """Return (but not remove) the element at the end of the deque."""
        if self._size == 0:
            raise Empty('Deque is empty.')
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)
        
    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)
        
    def delete_first(self):
        """Remove and return the element from the front of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self._size == 0:
            raise Empty('Deque is empty.')
        return self._delete_node(self._header._next)    
        
    def delete_last(self):
        """Remove and return the element from the back of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self._size == 0:
            raise Empty('Deque is empty.')
        return self._delete_node(self._trailer._prev)       
    
    def __str__(self):
        """Return string represintation of the queue."""
        if self._size > 0:
            result = []
            initial = self._header._next
            result.append(str(initial._element))
            for i in range(self._size-1):
                initial = initial._next
                result.append(str(initial._element))
            result = ', '.join(result)
        else:
            result = ''
        return 'Deque: front [' + result + '] end'
    
class PositionalList(_DoublyLinked):
    """A sequential container of elements allowing positional access."""

    class Position:
        """An abstraction representing the location of a single element."""
        
        def __init__(self, container, node):
            """Constructor should not invoked by user."""
            self._container = container
            self._node = node
    
        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)               


    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value