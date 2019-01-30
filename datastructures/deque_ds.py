from exceptions import * 

class ArrayDeque:
    """Deque implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        """Create an empty deque."""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size
    
    def __str__(self):
        """Return string represintation of the deque."""
        if self._size > 0:
            result = ', '.join([str(self._data[(self._front + i) % len(self._data)])\
                                for i in range(self._size)])
        else:
            result = ''
        return 'Deque: front [' + result + '] end'
    
    def is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but not remove) the element at the front of the deque.
        
        Raise Empty exception if deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]
    
    def last(self):
        """Return (but not remove) the element at the end of the deque.
        
        Raise Empty exception if deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]
    
    def add_first(self, e):
        """Add an element e to the front of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        pos = (self._front - 1) % len(self._data)
        self._data[pos] = e
        self._front = (self._front - 1) % len(self._data)
        self._size += 1
    
    def add_last(self, e):
        """Add an element e to the back of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        pos = (self._front + self._size) % len(self._data)
        self._data[pos] = e
        self._size += 1   
        
    def delete_first(self):
        """Remove and return the first element of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def delete_last(self):
        """Remove and return the last element of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def _resize(self, cap):
        """Resize to a new list of capacity cap."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0