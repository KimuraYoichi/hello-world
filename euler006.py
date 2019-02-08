#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:44:53 2019

@author: zx7y-kmr
"""

"""
最初の10個の自然数について, その二乗の和は,

12 + 22 + ... + 102 = 385
最初の10個の自然数について, その和の二乗は,

(1 + 2 + ... + 10)2 = 3025
これらの数の差は 3025 - 385 = 2640 となる.

同様にして, 最初の100個の自然数について二乗の和と和の二乗の差を求めよ.
"""

n=100
answer=0
seq1=list(range(1,n+1))


for i in range(n):
    for j in range(n):
        if seq1[i] != seq1[j]:
            answer += seq1[i]*seq1[j]

print(answer)