#!/usr/bin/env python
# coding: utf-8

# In[2]:


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')


# In[3]:


fruits.count('tangerine')


# In[4]:


fruits.index('banana')


# In[5]:


fruits.index('banana', 4)  # Find next banana starting a position 4


# In[6]:


fruits.reverse()
fruits


# In[7]:


fruits.append('grape')


# In[8]:


fruits


# In[9]:


fruits.sort()
fruits


# In[10]:


fruits.pop()


# In[11]:


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack


# In[12]:


stack.pop()


# In[13]:


stack


# In[14]:


stack.pop()


# In[15]:


stack.pop()


# In[16]:


stack


# In[17]:


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves


# In[18]:


queue.popleft()                 # The second to arrive now leaves


# In[19]:


queue                           # Remaining queue in order of arrival


# In[71]:


squares = []
for x in range(10):
    squares.append(x**2)
squares


# In[28]:


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# In[27]:


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
combs


# In[29]:


from math import pi
[str(round(pi, i)) for i in range(1, 6)]


# In[42]:


matrix = [
    [1, 2, 3, 4],
     [5, 6, 7, 8],
    [9, 10, 11, 12],
]


# In[33]:


[[row[i] for row in matrix] for i in range(4)]


# In[34]:


transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
transposed


# In[35]:


list(zip(*matrix))


# In[36]:


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a


# In[37]:


del a[2:4]
a


# In[38]:


del a[:]
a


# In[39]:


del a


# In[41]:


t = 12345, 54321, 'hello!'
t[0]


# In[43]:


t


# In[44]:


# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u


# In[45]:


# Tuples are immutable:
t[0] = 88888


# In[46]:


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v


# In[47]:


empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)


# In[48]:


len(singleton)


# In[49]:


singleton


# In[50]:


x, y, z = t


# In[51]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)


# In[52]:


'orange' in basket                 # fast membership testing


# In[53]:


'crabgrass' in basket


# In[54]:


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a # unique letters in a


# In[55]:


a | b                              # letters in a or b or both


# In[56]:


a & b                              # letters in both a and b


# In[57]:


a ^ b                              # letters in a or b but not both


# In[58]:


a = {x for x in 'abracadabra' if x not in 'abc'}
a


# In[59]:


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel


# In[60]:


tel['jack']


# In[61]:


del tel['sape']
tel['irv'] = 4127
tel


# In[62]:


list(tel)


# In[63]:


sorted(tel)


# In[64]:


'guido' in tel


# In[65]:


'jack' not in tel


# In[66]:


dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


# In[67]:


{x: x**2 for x in (2, 4, 6)}


# In[68]:


dict(sape=4139, guido=4127, jack=4098)


# In[70]:


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
         print(k, v)


# In[72]:


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# In[73]:


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# In[74]:


for i in reversed(range(1, 10, 2)):
    print(i)


# In[75]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)


# In[76]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


# In[78]:


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
filtered_data


# In[79]:


string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null


# In[80]:


(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)


# In[ ]:




