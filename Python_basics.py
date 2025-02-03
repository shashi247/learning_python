#!/usr/bin/env python
# coding: utf-8

# In[1]:


if 5>2:
    
            print("5 is greater than 2")


# In[17]:


#print examples
x="my name is shashi"
y="i am married to nunu"
print(x)
print(y)
print(x,y)


# In[13]:


x=5
x="shashi"
print(x)
print(type(x))


# In[14]:


shashi,neha="my name is shashi","neha is my wife"
print(shashi)
print(neha)


# In[19]:


fruits=["apple","banana","orange"]
x,y,z=fruits
print(fruits)
print(x)
print(y)
print(z)
print(x,y,z)
print(x+y+z)


# In[24]:


x,y=5,"job"
print(x,y)


# In[31]:


#function
x="awesone"

def myFunc():
    global x
    x="fantastic"
    print("Python is " + x)

myFunc()

print(x)


carname="Volvo"
print(carname)
print(type(carname))


# In[7]:


#variables
x=-20
y=20.3
z=1j
print(type(x),type(y),type(z))

a=float(x)
b=int(y)
c=complex(x)

print(a, b, c)
print(type(a),type(b),type(c))

import random
print("random")
print(random.randrange(1,100))

z=str(2)
print(z)

a="hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna shashi aliqua."""
if "dolor" in a:
    print("dolor in a")
    

print(len(a))
    
#print(a)

print(a[0])

print("dolor" in a )

for x in "bananana":
    print(x)
    
    
b = "Hello, World!"
print(b.split(","))


age=36
name= "my name is shashi and I am {}"
name=name.upper()
print ((name.format(age)))

print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x, int))


# In[6]:


#operator

print(5 + 4 - 7 + 3)


# In[110]:


#list

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

list1 = ["abc", 34, True, 40, "male"]
print(list1)

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon","shashi"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1] = "watermelon"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
thislist.insert(2,"blackcurrent")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist.clear()
print("thislist")
del thislist
print("thislist")


# In[9]:


#loop list

thislist=["apple","banana","cherry"]
# for x in thislist:
#     print(x)
# print(len(thislist))
# print (range(len(thislist)))
# for i in range(len(thislist)):
#     print(thislist[i])

    
# #while loop
# print(len(thislist))
# i=0
# while i < len(thislist):
#     print(thislist[i])
#     i=i+1
[print(x) for x in thislist]
  


# In[151]:


#comprehension looping
fruits=["apple","banana","cherry"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist2=[x for x in fruits if "e" in x]
print (newlist2)

newlist3=[x for x in fruits if x!="apple"]
print(newlist3)

newlist4=[x for x in fruits]
print(newlist4)

newlist5 = [x for x in range(10)]
print(newlist5)

newlist6 = ['hello' for x in fruits]
print(newlist6)

newlist7 = [x if x != "banana" else "orange" for x in fruits]
print(newlist7)



# In[161]:


#sorting
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


fruits = ["apple", "banana", "cherry"]
print(fruits[1])


# In[167]:


#tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple = thistuple+ y

print(thistuple)


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


# In[191]:


# # # def my_function(fname):
# # #   print(fname + " Refsnes")

# # # my_function("Emil")
# # # my_function("Tobias")
# # # my_function("Linus")

# # # def my_function(*kids):
# # #   print("The youngest child is " + kids[2])

# # # my_function("Emil", "Tobias", "Linus")


# # # def _myfunct(x):
# # #     return 5*x
# # # print(_myfunct(3))

# # def tri_recursion(k):
# #   if(k > 0):
# #     result = k + tri_recursion(k - 1)
# #     print(result)
# #   else:
# #     result = 0
# #   return result

# # print("\n\nRecursion Example Results")
# # tri_recursion(6)


# x = lambda a : a + 10
# print(x(5))

# y = lambda a, b : a*b+10
# print(y(2,3))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

class MyClass:
    x=5
    y=10
p1=MyClass()
print(p1.y)

class Person:
  def __init__(self1, name, age):
    self1.name = name
    self1.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


# In[194]:


#iterators

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# In[195]:


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


# In[198]:


# #polymorphism

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
#   x.move()

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand,x.model)
  x.move()


# In[199]:


def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# In[200]:


x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


# In[205]:


import platform

x = dir(platform)
print(x)


# In[209]:


import datetime

x = datetime.datetime.now()
y=dir(datetime)
print(x)
print(x.strftime("%A"))
print(y)
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)


# In[212]:


import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

x = abs(-7.25)

print(x)

import math

x = dir(math)

print(x)


# In[217]:


#json

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(x)
#print(json.dumps(x))
print(json.dumps(x, indent=0, separators=(". ", " = ")))


# In[ ]:




