# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 00:06:55 2022

@author: nikky
"""


class TestStack:
    
    def __init__(self,size):
        self.size = size
        self.container = []
        
    def push(self, item):
        
        if(len(self.container) >= self.size):
            print("Over Flow")
        else:
            self.container.append(item)
            
    def pop(self):
        if (len(self.container) < 1):
            print("Under Flow")
        else:
            print(self.container.pop())
            
    def printPeek(self):
        if(len(self.container) > 1):
            print(self.container[-1])
        else:
            print("Stack is Khali hai")
            
    def printStack(self):
        print(self.container)             



a = TestStack(2)
b = TestStack(5)


a.push(4)
a.push(5)
a.push(6)
a.push(7)
a.push(8)
a.pop()
a.printStack()

b.push(4)
b.push(5)
b.push(6)
b.push(7)
b.push(8)
b.pop()
b.printStack()
 

        