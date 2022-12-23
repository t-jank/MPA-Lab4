# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:25:20 2022

@author: t-jan
"""
import random

def random_permutation(n):
    a=[]
    for i in range(0,n): a.append(i+1)
    for i in range(0,n-1): # Fisher–Yates shuffle
        j = random.randint(i,n-1)
        a[i], a[j] = a[j], a[i]
    return a

def records(permutation):
    n=len(permutation)
    records_counter=0
    for i in range(0,n-1):
        if permutation[i+1]>permutation[i]:
            records_counter+=1
    return records_counter


a=random_permutation(10)
print(a)
print('records:',records(a))
