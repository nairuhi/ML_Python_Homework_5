#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:05:15 2021

@author: nairuhi
"""

def findDisappearedNumbers(nums):
    n = len(nums)
    l = []
    for i in range(1, n+1):
        if i not in nums:
            l.append(i)
    return l



nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))

nums = [1,1]
print(findDisappearedNumbers(nums))

