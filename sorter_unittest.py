import sorter
import unittest

# to run use python -m unittest sorter_unittest.py from cmd

class sortTestCase(unittest.TestCase):
    def test_1(self):
        t = "hello, kkk, Margo, google, PC, rain, mam, electricity, cake"
        res = sorter.str_to_arr(t)
        exp_res = ['hello', 'kkk', 'Margo', 'google', 'PC', 'rain', 'mam', 'electricity', 'cake']

        self.assertEqual(res, exp_res)

    def test_2(self):
        arr = ['hello', 'kkk', 'Margo', 'google', 'PC', 'rain', 'mam', 'electricity', 'cake']
        res = sorter.sortt(arr)
        exp_res =['PC', 'kkk', 'mam', 'rain', 'cake', 'hello', 'Margo', 'google', 'electricity']

        self.assertEqual(res, exp_res)
