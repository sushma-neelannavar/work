# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:56:43 2023

@author: sushma.n
"""

#from exception_handling.sub.subclass import Subclass


#from sub import subclass
from sub.subclass import *



class MainClass:
    def __init__(self):
        self.sub = Subclass()

    def run(self):
        try:
            self.sub.perform_action(5,0)
        #except ZeroDivisionError as e:
        #    print(repr(e))
        except Exception as e:
            #print(f"Caught a different exception in MainClass: {e}")
            print('Caught this error: ' + repr(e))

if __name__ == "__main__":
    main = MainClass()
    main.run()