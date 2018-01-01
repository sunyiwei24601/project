# -*- coding:utf-8 -*-"""@author:Levy@file:15-3.py@time:2017/12/142:47"""
import random
import unittest
def issorted(x):
    for i in range(len(x)):
        num=x[i]
        for j in x[i+1:]:
            if(num>j):
                return False
    return True

def quicksort(x):
    if(len(x)<=1):
        return x
    mid_num=random.randrange(0,len(x))
    y=x[0:mid_num]+x[mid_num+1:]
    mid=x[mid_num]
    left=[]
    right=[]
    for i in y:
        if i<mid:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left)+[mid]+quicksort(right)

class test_quicksort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(quicksort([1,4,3,2]),[1,2,3,4])
        self.assertEqual(quicksort([1,4,6,2,3]),[1,2,3,4,6])
        self.assertEqual(quicksort([1,4,4,2,2,8,8]),[1,2,2,4,4,8,8])

unittest.main()