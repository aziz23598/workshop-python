#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[2]:


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[3]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[4]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[5]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# In[9]:


def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# In[10]:


standard_arg(2)


# In[11]:


standard_arg(arg=2)


# In[12]:


pos_only_arg(1)


# In[13]:


pos_only_arg(arg=1)


# In[14]:


kwd_only_arg(3)


# In[15]:


kwd_only_arg(arg=3)


# In[16]:


combined_example(1, 2, 3)


# In[17]:


combined_example(1, 2, kwd_only=3)


# In[18]:


combined_example(1, standard=2, kwd_only=3)


# In[19]:


combined_example(pos_only=1, standard=2, kwd_only=3)


# In[20]:


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# In[21]:


def concat(*args, sep="/"):
    return sep.join(args)


# In[22]:


concat("earth", "mars", "venus")


# In[23]:


concat("earth", "mars", "venus", sep=".")


# In[24]:


list(range(3, 6)) 


# In[25]:


args = [3, 6]


# In[26]:


list(range(*args)) 


# In[27]:


def parrot(voltage, state='a stiff', action='voom'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.", end=' ')
        print("E's", state, "!")


# In[28]:


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}


# In[29]:


parrot(**d)


# In[30]:


def make_incrementor(n):
    return lambda x: x + n


# In[31]:


f = make_incrementor(42)


# In[32]:


f(0)


# In[33]:


f(1)


# In[34]:


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]


# In[35]:


pairs.sort(key=lambda pair: pair[1])


# In[36]:


pairs


# In[39]:


def my_function():
    """Do nothing, but document it.
    
        No, really, it doesn't do anything.
    """
    pass


# In[40]:


print(my_function.__doc__)


# In[41]:


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


# In[42]:


f('spam')


# In[ ]:




