# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 20:19:24 2021

@author: Erick

get, push, pop, delete
"""

#Implement an array

class Array:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __str__(self):
        return str(self.__dict__)
    
    def get(self, index):
        return self.data[index]
    
    def push(self, value):
        self.data[self.length] = value
        self.length += 1
    def pop(self):
        value = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return value


myArr = Array()
myArr.push(1)
myArr.push(2)
myArr.push(3)
myArr.push(4)
myArr.push(5)

print(myArr)

myArr.pop()
print(myArr)