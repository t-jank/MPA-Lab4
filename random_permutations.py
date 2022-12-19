# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:25:20 2022

@author: t-jan
"""

def random_permutation(n):
    a=[]
    for i in range(0,n):
        a.append(i+1)
    return a

print(random_permutation(10))