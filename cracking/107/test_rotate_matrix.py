import unittest

from rotate_matrix import Matrix, rotate_matrix



class TestRotateMatrix(unittest.TestCase):

    def test_empty_matrix(self):
        z = Matrix(4)
        p = Matrix(4)

        for i in range(z.size):
            rotate_matrix(z)
            self.assertCountEqual(z.data[i], p.data[i])


if __name__ == '__main__':
    unittest.main()