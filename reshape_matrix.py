#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:58:57 2021

@author: nairuhi
"""

def matrixReshape(mat, r, c):
    m = len(mat)
    n = len(mat[0])
    
    if m * n != r * c:
        return mat
            
    reshaped = [[]]
    
    for i in range(m):
        for j in range(n):
            k = mat[i][j]
            if len(reshaped[-1]) < c:
                reshaped[-1].append(k)
            else:
                reshaped.append([k])
                
    return reshaped 
                  


mat = [[1,2],[3,4]]
print(matrixReshape(mat, 1, 4))

mat = [[1,2],[3,4]]
print(matrixReshape(mat, 2, 4))

