from exceptions import * 

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    
    def __init__(self):
        """Create an empty stack."""
        self._data = []
        
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
    
    def __str__(self):
        """Return string represintation of the stack."""
        return 'Stack: bottom [' + ', '.join([str(e) for e in self._data]) + '] top'
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0
    
    def push(self, e):
        """Add an element e to the top of the stack."""
        self._data.append(e)
        
    def pop(self):
        """Remove and return the element from the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()       
    
    def top(self):
        """Return (but not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]