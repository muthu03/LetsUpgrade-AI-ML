#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
mail=input("Enter mail id:")
a=mail.index("@")
b=mail.index(".")
print(mail[a+1:b])


# In[ ]:





# In[2]:


#Question 2
items = input("Enter the words")
words = [word for word in items.split(",")]
print(",".join(sorted(words)))


# In[11]:


#Question 3
s={"abc",1,2,2,3}
print(s)
print(1 in s)
s.add("NUM")
print(s)
print(len(s))
s.remove("NUM")
print(s)
s1={"a","b"}
s2={1,2}
print(s1.union(s2))
del s1
s2.clear()
print(s2)


# In[7]:


#Question 4amp
arr=[1,2,3,4,5,6,7,8,10]
n=len(arr)
total=((n+1)*(n+2))/2
arrSUM=sum(arr)
print("the missing no is ")
print(total-arrSUM)


# In[1]:


#Question 5
duplicate = [2,12,123,435,57,8,93,2,1] 
print(list(set(duplicate)))


# In[ ]:




