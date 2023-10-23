#!/usr/bin/env python
# coding: utf-8

# # Assignment Instructions
# 
# `Hello Innominion,`
# 
# - **Try to attempt all the questions in every possible way.**
# - **Some other topics are required to solve some questions. don't panic.**
# - **Those questions can be answered after the topics are taught.**
# 
# 
# - `Join Mentoring Session for the Support/Doubts Resolving with Our Technical Mentors (2.00 PM - 6.00 PM  Mon-Sat)` 
# 
# Happy Learning !!!

# ## Basics of Python

# > `Question:` Print your name

# In[3]:


name=input()
print(f"My name is {name}")


# > `Question:` What is a variable? Write a Few words about Variables. Create a Variable with an Example. 

# Variable: Giving a name to value is called variable.
# 1. The variable name must should be starts with alphanumaricals and underscore("_").
# 2. The variable name should not starts with numbers/digits and special characters (except underscore("_"))
# 2. The  variable name should not contains any keywords(ex: for, if,is,in.etc)
# 3. The variable name can be function name(or) class name (or) object name (or) class name(or) module name.

# In[ ]:


name="Innomatics research lab"
marks=98
score=56.8
n=4+6j
result= True
lst=[1,2,3,4,5,6]
tup=(1,2,3,4,5,6,7)
set1={1,2,3,4,5,6,78}


# >`Question:` Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# delimiter = '.'
# For each of the following expressions, write the value of the expression and the type (of the value of
# the expression).
# 1. width/2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5
# 5. delimiter * 5

# In[6]:


width=int(input())
height=float(input())
delimiter=input()
print("width/2=", width/2)
print("width/2.0=", width/2.0)
print("height/3=", height/3)
print(1+2*5)
print(delimiter*5)

# Sample Outputs
1. width/2 = 8.5
2. width/2.0 = 8.5
3. height/3 = 4.0
4. 11
5. .....
# > `Question:` Add two number by taking variable names as first and seccond

# In[7]:


num1=int(input("first number is:"))
num2=int(input("second number is:"))
print("Addition of two numbers are :", num1+num2)


# In[6]:





# > `Question:` Add your first name and second name

# In[9]:


fisrt_name=input("My first name is: ")
second_name=input("My second name is: ")
print("My full name is :",fisrt_name+" "+second_name)


# In[8]:





# In[ ]:





# > `Question:` print the datatypes of the following
# - 10,'10',True,10.5

# In[11]:


print("10 - ",type(10))
print("'10' - ", type("10"))
print("True - ", type(True))
print("10.5 - ",type(10.5))


# In[11]:





#  `Question:` 
# > - num_int = 123
# > - num_str = "456"
# > - Add num_int and num_str
# - `hint: first need to convert num_str into integer`

# In[14]:


num_int=int(input())
num_str=input()
result=num_int+int(num_str)
print(f"Addition of {num_int} and {num_str} is: ",result)


# In[13]:





# ### Advanced Questions

# > `Question:` The volume of a sphere with radius r is  4/3πr3  . What is the volume of a sphere with radius 5?

# In[1]:


r=int(input())
volume_of_a_sphere=(4/3)*(3.14)*(r**3)
print(volume_of_a_sphere)


# > `Question:` Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. Shipping costs Rs.3 for the first copy and 75 paise for each additional copy. What is the total wholesale cost for 60 copies?

# In[2]:


cover_price = float(input("Enter the cover price of a book:"))
discount=int(input("Enter the discount:"))
shipping_cost = float(input("Enter the shipping cost for the first copy:"))
shipping_cost_remaing = float(input("enter the shipping cost for remaing copies:"))
total_copies = int(input("Enter the total copies:"))
cost_before_shippint=(cover_price*(100/discount))*total_copies
cost_for_shipping=shipping_cost+((shipping_cost_remaing)*(total_copies-1))
total_cost=cost_before_shippint+cost_for_shipping
print(total_cost)


# In[ ]:





# # [Innomatics Research Labs](https:/innomatics.in/)
# [www.innomatics.in](https:/innomatics.in/)
