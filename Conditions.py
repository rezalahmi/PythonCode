#!/usr/bin/env python
# coding: utf-8

# In[2]:


#if
#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
#Other programming languages often use curly-brackets for this purpose.
age = 17
if age > 15 :
    print("you are younge")
else:
    print("you are teenager")
    


# In[4]:


#elif
#The elif keyword is pythons way of saying "if the previous conditions were not true, 
#then try this condition".
color = "blue"
if color == "blue":
    print("Esteglal")
elif color == "red":
    print("perspolis")
elif color == "yellow":
    print("sepahan")
else:
    print("wrong color")


# In[9]:


#and
age = int(input("Enter your age:"))
if age >= 22 and age <=65 :
    print("you are ",age," year's old")
    print("You can get the job")
elif age < 22:
    print("you are so younge")
else :
    print("you are so old")


# In[11]:


#or
age = int(input("Enter your age:"))
city = input("Enter your city:")
if age >= 45 or city == "Mashhad":
    print("you can get the vaccine covid 19")
else:
    print("you can't get the vaccine covid 19")


# In[13]:


#or
age = int(input("Enter your age:"))
city = input("Enter your city:")
if age >= 45 or city == "Mashhad":
    print("you can get the vaccine covid 19")
elif not(city == "Karaj"):
    print("you are so lucky")
else:
    print("you can't get the vaccine covid 19")


# In[17]:


x = int(input("what is the first number:"))
y = int(input("what is the second number:"))
op = input("what is the operation(+,-,*,/):")
if op == "+":
    print("result is :",x+y)
elif op == "-":
    print("result is :",x-y)
elif op == "*":
    print("result is :",x*y)
elif op == "/":
    print("result is :",x/y)
else :
    print("something is wrong")


# In[18]:


#If you have only one statement to execute, you can put it on the same line as the if statement.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if a > b: print("a is greater than b")


# In[20]:


#If you have only one statement to execute, one for if, 
#and one for else, you can put it all on the same line
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("A") if a > b else print("B")


# In[23]:


#This technique is known as Ternary Operators, or Conditional Expressions.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("A") if a > b else print("=") if a == b else print("B")


# In[25]:


#if statements cannot be empty, but if you for some reason have an if statement with no content, 
#put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass


# In[ ]:




