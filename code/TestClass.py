#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:11:32 2022

@author: ajaygunacr7
"""

class Mesh:
    def __init__(self):
        self.points = [[0,0,0],[0,1,0],[1,1,0],[1,0,0]]
        self.faces = [4,0,1,2,3]
    def tell(self):
        print(self.points)
        print(self.faces)
    
    class cell:
        def __init__(self):
            self.cells = 1
            self.cell = [1]
            
        def tell(self):
            print(self.cells)
            print(self.cell)
    
