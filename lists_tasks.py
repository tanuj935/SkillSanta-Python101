#!/usr/bin/env python
# coding: utf-8

# ## lists_task      (  python101  )        Author:Tanuj         Email:tanujraghavan@gmail.com

# ### Q1)Python Program to Find the largest Number in a list.

# In[9]:


#CODE
list=[2,7,3,9,11,5,6]
print(max(list))


# ### Q2)Python Program to Find the Second largest Number in a list.

# In[10]:


##CODE
list=[2,7,3,9,11,5,1]
list.sort()
print(list[-2])


# ### Q3)Python Program to Merge Two lists and sort it.

# In[11]:


##CODE
list1=[3,11,5,9]
list2=[10,2,8,6]
list3=list1+list2
list3.sort()
print(list3)


# ### Q4)Python Program to swap the First and Last Value of a list.

# In[12]:


##CODE
list=[1,2,3,4,5,6,7]
temp=list[1]
list[0]=list[-1]
list[-1]=temp
print(list)

