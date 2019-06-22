#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Queue:

        def __init__(self):
            self.queue = []

        def enqueue(self,dataval):
            # Insert method to add element
            self.queue.insert(0,dataval)
            
        # Pop method to remove element
        def dequeue(self):
            if len(self.queue)>0:
                return self.queue.pop()
            return ("No elements in Queue!")


# In[7]:


TheQueue = Queue()
TheQueue.enqueue("Mon")
TheQueue.enqueue(2)
TheQueue.enqueue(3.14)


# In[8]:


TheQueue.dequeue()


# In[ ]:




