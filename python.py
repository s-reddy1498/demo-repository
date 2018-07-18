
# coding: utf-8

# In[2]:


print("Hello")


# In[4]:


a=5
print(a)


# In[7]:


print("hello",a)


# In[8]:


a=12
b=23
print(a+b)


# In[14]:



a=12
if(a==12):
    print("YES")
    print("NO")
else:
    print("!@#")


# In[19]:


import matplotlib.pyplot as plt
plt.plot([1,3,3,1])
plt.ylabel('some numbers')
plt.show()


# In[32]:


plt.plot([1,3,2,5,4,6,2])
plt.plot([1,4,3,5,6,7,3])
#plt.plot([5,6,7,3,5,2,6])
plt.ylabel('some numbers')
plt.show()


# In[28]:


import random
for x in range(10):
   print (random.randint(1,101))


# In[33]:


x = [2 4 7 2 4 5 2 5 1 4];
bar(x);
saveas(gcf,'Barchart','epsc')

