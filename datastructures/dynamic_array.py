import ctypes
import random

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    
    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        
    def __len__(self):
        """Return the number of elements stored in the array."""
        return self._n
        
    def __getitem__(self, k):
        """Return the element at index k."""
        if not -self._n - 1 <= k <= self._n:
            raise IndexError('Invalid index')
        return self._A[k]

    def __setitem__(self, k, value):
        """Set element at index k to value"""
        if not 0 <= k <= self._n:
            raise IndexError('Invalid index')
        self._A[k] = value
        
    def __contains__(self, e):
        """Return True if element in the array, otherwise False"""
        for k in range(self._n):
            if self._A[k] == e:
                return True
        return False
    
    def append(self, e):
        """Add an element to the end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = e
        self._n += 1
        
    def insert(self, k, value):
        """Insert value at index k, shifting subsequence values rightward."""
        if k > n:
            raise IndexError('Invalid index')
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
        
    def remove(self, value):
        """Remove the first occurrence of value (or raise ValueError)."""
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('Value not found')

    def remove_all(self, value):
        """Remove all elements equal to value (or raise ValueError)."""
        B = self._make_array(self._capacity)
        counter = 0
        initial_len = self._n
        for k in range(self._n):
            if self._A[k] == value:
                counter += 1
                continue
            else:
                B[k - counter] = self._A[k]
        if counter == 0:
            raise ValueError('Value not found')
        self._A = B
        self._n = initial_len - counter
        
    def pop(self):
        """Remove and return the last element of the array."""
        if self._n == 0:
            raise IndexError('Array is empty')
        if 4 * self._n < self._capacity:
            self._resize(self._capacity // 2)
        output = self._A[self._n - 1]  
        self._A[self._n - 1] = None
        self._n -= 1
        return output
        
    def shuffle(self):
        """Shuffle the array."""
        # start from end of array and chose position to swap
        for k in range(self._n - 1, 0, -1):
            pos = random.randrange(start=0, stop=k)
            self._A[k], self._A[pos] = self._A[pos], self._A[k]
            
    def __str__(self):
        """Return string represintation of an array."""
        return ', '.join([str(self._A[i]) for i in range(self._n)])
    
    def __repr__(self):
        """Return string represintation of an array."""
        return self.__str__()   
    
    def _resize(self, c):
        """Resize internal array to a capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
        
    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()     