#!/usr/bin/env python
# coding: utf-8

# In[48]:


class student:
    #class attributes
    department='Electrical'
    #initialiser
    def __init__(self):
        self.rollNo=list()
        self.name=list()
        self.year=list()
        self.cgpa=list()
    def enterRecords(self,noOfStudents):
        for i in range(1,noOfStudents+1):
            print('Enter record no '+str(i)+'\n')
            print('Enter Roll Number:')
            a=int(input())
            self.rollNo.append(a)
            print('Enter name:')
            b=str(input())
            self.name.append(b)
            print('Enter Year of study:')
            c=str(input())
            self.year.append(c)
            print('Enter cgpa:')
            d=float(input())
            self.cgpa.append(d)
    def displayRecords(self):
        print('S.No|RollNo|Name|Year|CGPA')
        for i in range(0,len(self.rollNo)):
            print(str(i+1)+'      '+str(self.rollNo[i])+'    '+
                  self.name[i]+'     '+self.year[i]
                  +'      '+str(self.cgpa[i]))
    def sortwrtRollNo(self):
        for i in range(len(self.rollNo)):
            # Find the minimum element in remaining
            minPosition = i
            for j in range(i+1, len(self.rollNo)):
                if self.rollNo[minPosition] < self.rollNo[j]:
                    minPosition = j        
            # Swap the found minimum element with minPosition       
            temp = self.rollNo[i]
            self.rollNo[i] = self.rollNo[minPosition]
            self.rollNo[minPosition] = temp
            # swap the other three
            temp = self.name[i]
            self.name[i] = self.name[minPosition]
            self.name[minPosition] = temp
            
            temp = self.year[i]
            self.year[i] = self.year[minPosition]
            self.year[minPosition] = temp
            
            temp = self.cgpa[i]
            self.cgpa[i] = self.cgpa[minPosition]
            self.cgpa[minPosition] = temp
            
    def sortwrtNames(self):
        


# In[49]:


a=student()
a.enterRecords(2)


# In[50]:


a.displayRecords()


# In[51]:


a.sortwrtRollNo()
a.displayRecords()

