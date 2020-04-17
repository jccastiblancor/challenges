from challenges.solved.mergeArrays import merge
import unittest

class MyTest(unittest.TestCase):
    def test_general(self):
        A = [-100, -20, -10, 0, 30, 40, 90]
        B = [-90, 0, 0, 20, 30]
        C = [-50, -10, 0, 5, 30, 70, 100]
        ans=merge(A,B,C)
        self.assertEqual(ans, [-100, -90, -50, -20, -10, 0, 5, 20, 30, 40, 70, 90, 100])
        self.assertEqual(len(ans), 13)

    def test_repetidos(self):
        A = [0,0,0,0,0,0,0,0,0,0]
        B = [0,0,0,0,0,0,0,0]
        C = [0,0,0,0,0,0,0,0]
        ans = merge(A,B,C)
        self.assertEqual(len(ans), 1)

    def test_con_arrays_vacios(self):
        A = [0,1,2,3]
        B = []
        C = []
        ans = merge(A,B,C)
        self.assertEqual(ans, A)

    def test_primer_ultimo_dato(self):
        A = [-10,10]
        B = [-30,30]
        C = [-50,0,50]

        ans = merge(A,B,C)
        self.assertEqual(ans[0], -50)
        self.assertEqual(ans[len(ans)-1], 50)

# Casos de prueba X.

    def test_1(self):
        A = [-100, -20, -10, 0, 30, 40, 90]
        B = [-90, 0, 0, 20, 30]
        C = [-50, -10, 0, 5, 30, 70, 100]
        self.assertEqual(merge(A,B,C), [-100, -90, -50, -20, -10, 0, 5, 20, 30, 40, 70, 90, 100])