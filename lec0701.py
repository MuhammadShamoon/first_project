#!/usr/bin/env python
# coding: utf-8

# In[22]:


class Stack:
        def __init__(self):
            #object attribute: list to store
            self.stack = []

        def isEmpty(self):
            return self.stack == []

        def push(self, item):
            #entering values into object
            self.stack.append(item)

        def pop(self):
            #removing values from the top
            return self.stack.pop()

        def peek(self):
            #additional method that allows you 
            #to just loop at what is at the top
            return self.stack[len(self.stack)-1]

        def size(self):
            #tells the current size of stack
            return len(self.stack)


# In[23]:


s=Stack()

print(s.isEmpty())


# In[24]:


s.push('Ahmed')
s.push(5)
s.push(3.12)
s.push('Jamal')


# In[25]:


s.peek()


# In[26]:


s.pop()


# In[27]:


s.peek()


# In[29]:


s.size()

