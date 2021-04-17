#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.getcwd()


# In[3]:


os.chdir('/server/accesslogs')


# In[4]:


import os


# In[5]:


dir(os)


# In[7]:


help(os)


# In[8]:


import shutil


# In[9]:


import glob


# In[10]:


glob.glob('*.py')


# In[11]:


import sys


# In[12]:


print(sys.argv)


# In[13]:


from datetime import date


# In[14]:


now = date.today()


# In[15]:


now


# In[16]:


now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


# In[17]:


birthday = date(1964, 7, 31)


# In[18]:


age = now - birthday


# In[19]:


age.days


# In[20]:


from timeit import Timer


# In[21]:


Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()


# In[22]:


Timer('a,b = b,a', 'a=1; b=2').timeit()


# In[23]:


import reprlib


# In[24]:


reprlib.repr(set('supercalifragilisticexpialidocious'))


# In[25]:


import pprint


# In[26]:


t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]


# In[27]:


pprint.pprint(t, width=30)


# In[28]:


import textwrap


# In[29]:


doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""


# In[30]:


print(textwrap.fill(doc, width=40))


# In[31]:


from string import Template


# In[32]:


t = Template('${village}folk send $$10 to $cause.')


# In[33]:


t.substitute(village='Nottingham', cause='the ditch fund')


# In[34]:


import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


# In[35]:


from array import array


# In[36]:


a = array('H', [4000, 10, 700, 22222])


# In[37]:


sum(a)


# In[38]:


a[1:3]


# In[39]:


from collections import deque


# In[40]:


d = deque(["task1", "task2", "task3"])


# In[41]:


d.append("task4")


# In[42]:


print("Handling", d.popleft())


# In[43]:


unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)


# In[44]:


import bisect


# In[45]:


scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]


# In[46]:


bisect.insort(scores, (300, 'ruby'))


# In[47]:


scores


# In[48]:


from heapq import heapify, heappop, heappush


# In[49]:


data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]


# In[50]:


heapify(data) 


# In[51]:


heappush(data, -5)   


# In[52]:


[heappop(data) for i in range(3)]


# In[53]:


from decimal import *


# In[54]:


round(Decimal('0.70') * Decimal('1.05'), 2)


# In[55]:


round(.70 * 1.05, 2)


# In[56]:


Decimal('1.00') % Decimal('.10')


# In[57]:


1.00 % 0.10


# In[58]:


sum([Decimal('0.1')]*10) == Decimal('1.0')


# In[60]:


sum([0.1]*10) == 1.0


# In[61]:


getcontext().prec = 36


# In[62]:


Decimal(1) / Decimal(7)


# In[ ]:




