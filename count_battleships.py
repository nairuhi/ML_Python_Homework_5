#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:35:24 2021

@author: nairuhi
"""


def countBattleships(board):
    m = len(board)
    n = len(board[0])
    
    count = 0
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X':
                increase = 1
                if (i > 0 and board[i-1][j] == 'X') or (j > 0 and board[i][j-1] == 'X'):
                    increase = 0
                count += increase 
            
    return count


board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(countBattleships(board))

board = [["."]]
print(countBattleships(board))
 
                 