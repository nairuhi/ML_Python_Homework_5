#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:54:16 2021

@author: nairuhi
"""


def transpose(matrix):
    import numpy as np
    n = np.shape(matrix)
    
    transposed = np.zeros((n[1], n[0]), dtype = int)
    
    for i in range(n[0]):
        for j in range(n[1]):
            transposed[j][i] = matrix[i][j]
    return transposed



matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))

matrix = [[1,2,3],[4,5,6]]
print(transpose(matrix))

