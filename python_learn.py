#!/usr/bin/env python
# coding: utf-8

# In[58]:


a=1
b=2
c=3
d=4

def add(i,k):
    return i+k

add(4,5)

class Question:
    def __init__(self,description,answer):
        self.description = description
        self.answer = answer

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def name(self):
        print(self.name)
    def age(self):
        print(self.age)

class Student(Person):
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school        
    def school(self):
        print(self.school)

