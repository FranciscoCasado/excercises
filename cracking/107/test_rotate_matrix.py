import unittest

from rotate_matrix import Matrix, rotate_matrix


class TestRotateMatrix(unittest.TestCase):
    def test_rotate_empty_matrix(self):
        z = Matrix(4)
        p = Matrix(4)

        rotate_matrix(z)
        for i in range(z.size):
            self.assertCountEqual(z.data[i], p.data[i])

    def test_rotate_matrix(self):
        p = Matrix(4)
        p.data[1][2] = 56
        q = Matrix(4)
        q.data[1][1] = 56

        rotate_matrix(p)
        for i in range(p.size):
            self.assertCountEqual(p.data[i], q.data[i])

    def test_rotate_matrix_odd_size(self):
        p = Matrix(9)
        p.data[1][8] = 56
        q = Matrix(9)
        q.data[0][1] = 56

        rotate_matrix(p)
        for i in range(p.size):
            self.assertCountEqual(p.data[i], q.data[i])


if __name__ == "__main__":
    unittest.main()
