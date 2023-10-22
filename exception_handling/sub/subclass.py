# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:57:48 2023

@author: sushma.n
"""

class Subclass:
    def perform_action(self, val1, val2):
        # Some code that might raise an exception
        #self.val = val
        print(val1)
        print(val2)
        if val1 / val2:
            print("done")
            raise ZeroDivisionError("An error occurred in the Subclass")