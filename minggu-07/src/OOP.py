#!/usr/bin/env python
# coding: utf-8

# In[1]:


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


# In[2]:


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


# In[3]:


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


# In[4]:


x = Complex(3.0, -4.5)


# In[5]:


x.r, x.i


# In[6]:


x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


# In[13]:


class Dog:
     kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
            self.name = name    # instance variable unique to each instance
d = Dog('Fido')
e = Dog('Buddy')
d.kind 


# In[14]:


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


# In[15]:


d = Dog('Fido')


# In[16]:


e = Dog('Buddy')


# In[17]:


d.add_trick('roll over')


# In[18]:


e.add_trick('play dead')


# In[19]:


d.tricks


# In[20]:


e.tricks


# In[22]:


class Warehouse:
    purpose = 'storage'
    region = 'west'


# In[23]:


w1 = Warehouse()


# In[24]:


print(w1.purpose, w1.region)


# In[25]:


w2 = Warehouse()


# In[26]:


w2.region = 'east'


# In[27]:


print(w2.purpose, w2.region)


# In[28]:


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


# In[29]:


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


# In[30]:


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


# In[31]:


class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000


# In[32]:


for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')


# In[33]:


s = 'abc'


# In[34]:


it = iter(s)


# In[35]:


it


# In[36]:


next(it)


# In[37]:


next(it)


# In[38]:


next(it)


# In[39]:


next(it)


# In[40]:


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# In[41]:


rev = Reverse('spam')


# In[42]:


iter(rev)


# In[44]:


for char in rev:
    print(char)


# In[45]:


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# In[46]:


for char in reverse('golf'):
    print(char)


# In[47]:


sum(i*i for i in range(10))                 # sum of squares


# In[48]:


xvec = [10, 20, 30]


# In[49]:


yvec = [7, 5, 3]


# In[50]:


sum(x*y for x,y in zip(xvec, yvec))         # dot product


# In[55]:


unique_words = set(word for line in page  for word in line.split())


# In[56]:


valedictorian = max((student.gpa, student.name) for student in graduates)


# In[57]:


data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))


# In[ ]:




