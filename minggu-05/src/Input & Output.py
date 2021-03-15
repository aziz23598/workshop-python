#!/usr/bin/env python
# coding: utf-8

# In[1]:


year = 2016
event = 'Referendum'
f'Results of the {year} {event}'


# In[2]:


yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)


# In[3]:


s = 'Hello, world.'
str(s)


# In[4]:


repr(s)


# In[5]:


str(1/7)


# In[6]:


x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)


# In[7]:


# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)


# In[8]:


# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))


# In[9]:


import math
print(f'The value of pi is approximately {math.pi:.3f}.')


# In[10]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


# In[11]:


animals = 'eels'
print(f'My hovercraft is full of {animals}.')


# In[12]:


print(f'My hovercraft is full of {animals!r}.')


# In[13]:


print('We are the {} who say "{}!"'.format('knights', 'Ni'))


# In[14]:


print('{0} and {1}'.format('spam', 'eggs'))


# In[15]:


print('{1} and {0}'.format('spam', 'eggs'))


# In[16]:


print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))


# In[17]:


print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))


# In[18]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))


# In[19]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# In[20]:


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# In[21]:


for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))


# In[22]:


'12'.zfill(5)


# In[23]:


'-3.14'.zfill(7)


# In[24]:


'3.14159265359'.zfill(5)


# In[25]:


import math
print('The value of pi is approximately %5.3f.' % math.pi)


# In[26]:


f = open('workfile', 'w')


# In[28]:


with open('workfile') as f:
    read_data = f.read()
# We can check that the file has been automatically closed.
f.closed


# In[29]:


f.close()
f.read()


# In[30]:


f.read()


# In[31]:


f.read()


# In[32]:


f.readline()


# In[33]:


f.readline()
f.readline()
f.readline()


# In[34]:


for line in f:
    print(line, end='')


# In[35]:


f.write('This is a test\n')


# In[38]:


value = ('the answer', 42)
s = str(value)
f.write(s)


# In[39]:


f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')


# In[40]:


f.seek(5)      # Go to the 6th byte in the file


# In[41]:


f.read(1)


# In[42]:


f.seek(-3, 2)  # Go to the 3rd byte before the end


# In[43]:


f.read(1)


# In[44]:


import json
json.dumps([1, 'simple', 'list'])


# In[45]:


json.dump(x, f)


# In[ ]:




