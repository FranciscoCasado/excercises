"""
Given an image represented by an N by matrix, whit int values, write a method to rotate the image by 90 degrees. Can u do it in place?
"""

# Type hint definitions

class Matrix:

    def __init__(self, size):
        self._size = size
        self.data = []

        for i in range(size):
            self.data.append([])
            for j in range(size):
                self.data[i].append(0)


    @property
    def size(self):
        return self._size

    def __repr__(self):
        s = ''
        for l in self.data:
            s += str(l) + '\n' 
        return s

def rotate_matrix(img) -> Matrix:
    N = img.size
    stop = int(N/2) + (N%2)

    for i in range(stop):
        for j in range(stop):
            temp = img.data[i][j]
            img.data[i][j] = img.data[j][N-1-i]
            img.data[j][N-1-i] = img.data[N-1-i][N-1-j]
            img.data[N-1-i][N-1-j] = img.data[N-1-j][i]
            img.data[N-1-j][i] = temp

    return img
    