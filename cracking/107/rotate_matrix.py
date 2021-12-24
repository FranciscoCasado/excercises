"""
Given an image represented by an N by matrix, whit int values, write a method to rotate the image by 90 degrees. Can u do it in place?
"""

# Type hint definitions

class Matrix:

    def __init__(self, size):
        self._size = size
        self.data = [ [0]*size ] * size

    @property
    def size(self):
        return self._size

def rotate_matrix(img) -> Matrix:
    return img
    