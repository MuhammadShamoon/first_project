#!/usr/bin/env python
# coding: utf-8

# In[22]:


class student:
    #class attributes
    department='Electrical'
    #initialiser
    def __init__(self):
        self.rollNo=list()
        self.name=list()
        self.year=list()
        self.cgpa=list()
     


# In[23]:


studentdatabase=student()


# In[25]:


print(studentdatabase.rollNo)

