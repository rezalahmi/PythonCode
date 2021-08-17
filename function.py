#!/usr/bin/env python
# coding: utf-8

# In[3]:


def bmi(height, weight):
    x = weight / (height ** 2)
    print("your bmi is :",x)
    if x <= 18.5 :
        print("Underweight")
    elif x > 18.5 and x < 25 :
        print("normal")
    elif x >= 25 and x < 30:
        print("Overweight")
    elif x >= 30:
        print("Obese")


# In[4]:


bmi(1.78,80.7)


# In[5]:


def bmi_calculator(height,weight):
    return weight/(height**2)

def bmi(height, weight):
    x = bmi_calculator(height,weight)
    print("your bmi is :",x)
    if x <= 18.5 :
        print("Underweight")
    elif x > 18.5 and x < 25 :
        print("normal")
    elif x >= 25 and x < 30:
        print("Overweight")
    elif x >= 30:
        print("Obese")


# In[6]:


bmi(1.78,80.7)


# In[9]:


bmi(1.78,78)


# In[10]:


#If you do not know how many arguments that will be passed into your function, 
#add a * before the parameter name in the function definition
def print_name(*names):
    for n in names:
        print("the name is :", n)


# In[11]:


print_name("reza","eli")


# In[12]:


#Passing a List as an Argument
names = ["reza","raheleh"]
def print_name(names):
    for n in names:
        print("the name is :",n)


# In[13]:


print_name(names)


# In[14]:


def square_list(num):
    result = []
    for i in num:
        result.append(i**2)
    return result


# In[15]:


x = square_list(range(0,10))
print(x)


# In[16]:


#Recursion
def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)


# In[19]:


factorial(10)


# In[20]:


def add_two_list(list_a,list_b):
    return(list(map(sum,zip(list_a,list_b))))


# In[21]:


list_a = [1,2,3]
list_b = range(0,3)
add_two_list(list_a,list_b)


# In[3]:


#https://docs.python.org/3/library/functions.html
#for study built in function in python
#Return the absolute value of a number
abs(-12.3)


# In[6]:


my_list = [1,1,0,1,1]
#Return True if all elements of the iterable are true
all(my_list)


# In[7]:


#Return True if any element of the iterable is true
any(my_list)


# In[9]:


#return a string containing a printable representation of an object
my_str = 104
ascii(my_str)


# In[30]:


#Return the string representing a character whose Unicode code point is the integer i.
chr(my_str)


# In[32]:


#Given a string representing one Unicode character, return an integer representing 
#the Unicode code point of that character
ord('h')


# In[20]:


#Without arguments, return the list of names in the current local scope
dir()


# In[22]:


globals()


# In[14]:


#Take two (non complex) numbers as arguments and return a pair of numbers consisting of 
#their quotient and remainder when using integer division
divmod(6,3)


# In[15]:


temp_list = list(enumerate(my_list))
print(temp_list)


# In[16]:


x = 2
y = 3
#The expression argument is parsed and evaluated as a Python expression
eval('x+y')


# In[19]:


#The format() method formats the specified value(s) and 
#insert them inside the string's placeholder.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
txt2 = "My name is {0}, I'm {1}".format("John",36)
print(txt2)


# In[28]:


#Convert an integer number to a lowercase hexadecimal string prefixed with “0x”
hex(255)


# In[29]:


#Convert an integer number to an octal string prefixed with “0o”
oct(255)


# In[24]:


my_list = [1,2,3,4]
max(my_list)


# In[25]:


min(my_list)


# In[33]:


#Return a string containing a printable representation of an object.
repr(1234)


# In[36]:


my_list = list(reversed(repr(1234)))
print(my_list)


# In[41]:


round(13.1654,2)


# In[42]:


sorted(my_list)


# In[44]:


#Sums start and the items of an iterable from left to right and returns the total
sum([1,2,3])


# In[45]:


#A lambda function can take any number of arguments, but can only have one expression.
#The expression is executed and the result is returned
my_fun = lambda x : x**2
my_fun(4)


# In[46]:


#Lambda functions can take any number of arguments
my_pow = lambda x,y : x**y
my_pow(2,4)


# In[47]:


#The power of lambda is better shown when you use them 
#as an anonymous function inside another function.
def my_fun(text):
    return lambda x : text.find(x)
search = my_fun("my name is reza")
search('r')


# In[ ]:




