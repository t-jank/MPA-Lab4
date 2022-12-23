# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:25:20 2022

@author: t-jan
"""
import random
import math

def random_permutation(n):
    a=[]
    for i in range(0,n): a.append(i+1)
    for i in range(0,n-1): # Fisher–Yates shuffle
        j = random.randint(i,n-1)
        a[i], a[j] = a[j], a[i]
    return a

def fixed_points(permutation):
    n=len(permutation)
    fixed_points_counter=0
    for i in range(0,n):
        if permutation[i]==i+1:
            fixed_points_counter+=1
    return fixed_points_counter

def records(permutation):
    n=len(permutation)
    records_counter=0
    for i in range(0,n-1):
        if permutation[i+1]>permutation[i]:
            records_counter+=1
    return records_counter

def cycles(permutation):
    n=len(permutation)
 #   expected_number_of_cycles = 0
  #  for i in range(1,n+1): expected_number_of_cycles+=(1/i)
   # gamma=0.57721566490153286
    #exnoc=math.log1p(n)+gamma
    identity=[]
    for i in range(0,n): identity.append(i+1)
    print(identity)
    flags=[]
    for i in range(0,n): flags.append('n')
    print(flags)
    pom=0
    if 'n' in flags:
        flags[pom]='t'
        pom=flags[pom-1]
        


a=random_permutation(10)
print(a)
cycles(a)
