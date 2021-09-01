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


# In[14]:


#mini project, creating shopping list
hardware_store_list = {}
supermarket_list = {}
def show_list(shopping_list,include_quantity=True):
    for item,quantity in shopping_list.items():
        if include_quantity:
            print(f"{quantity}x {item}")
        else:
            print(item)
def add_item(item,quantity,shopping_list):
    if not item:
        quantity = 0
    if item in shopping_list.keys():
        shopping_list[item] +=quantity
    else: shopping_list[item] = quantity
    return shopping_list


# In[15]:


hardware_store_list = add_item("Nails", 1, hardware_store_list)
hardware_store_list = add_item("Screwdriver", 1, hardware_store_list)
hardware_store_list = add_item("Glue", 3, hardware_store_list)

supermarket_list = add_item("Bread", 1, supermarket_list)
supermarket_list = add_item("Milk", 2, supermarket_list)

show_list(hardware_store_list)
show_list(supermarket_list)


# In[16]:


def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_item(item_name, quantity, shopping_list={}):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

    return shopping_list

clothes_shop_list = add_item("Shirt", 3)
electronics_store_list = add_item("USB cable", 1)
show_list(clothes_shop_list)
show_list(electronics_store_list)
#in the add_item function, shopping_list has the defualt value, you sent an immutable value
#like list or dictionary to prarameter, so this problem accure


# In[17]:


# to solve this problem, use None
def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_item(item_name, quantity, shopping_list=None):
    if shopping_list is None:
        shopping_list = {}
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

    return shopping_list

clothes_shop_list = add_item("Shirt", 3)
electronics_store_list = add_item("USB cable", 1)
show_list(clothes_shop_list)
show_list(electronics_store_list)


# In[20]:


#it is possible to define a function that accepts any number of optional arguments. 
#You can even define functions that accept any number of keyword arguments. 
#Keyword arguments are arguments that have a keyword and a value associated with them
some_items = ["Coffee", "Tea", "Cake", "Bread"]
print(some_items)
#unpacking
#it unpacks the sequence into its individual components
print(*some_items)


# In[21]:


shopping_list = {}

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_items(shopping_list, *item_names):
    for item_name in item_names:
        shopping_list[item_name] = 1

    return shopping_list

shopping_list = add_items(shopping_list, "Coffee", "Tea", "Cake", "Bread")
show_list(shopping_list)
#in the add_items we use unpacking to send more keywork argument


# In[23]:


def test_arguments(a, b):
    print(a)
    print(b)

test_arguments("first argument", "second argument")
print()
test_arguments(a="first argument", b="second argument")
print()
#In the first function call, the arguments are passed by position, 
#whereas in the second one they’re passed by keyword. 
#If you use keyword arguments, you no longer need to input arguments in the order they are defined
test_arguments(b="second argument", a="first argument")


# In[24]:


#When defining a function, you can include any number of
#optional keyword arguments to be included using kwargs, 
#which stands for keyword arguments
#The parameter name kwargs is preceded by two asterisks (**). 
#The double star or asterisk operates similarly to the single asterisk you used earlier
#to unpack items from a sequence. The double star is used to unpack items from a mapping. 
#A mapping is a data type that has paired values as items, such as a dictionary.
shopping_list = {}

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_items(shopping_list, **things_to_buy):
    for item_name, quantity in things_to_buy.items():
        shopping_list[item_name] = quantity

    return shopping_list

shopping_list = add_items(shopping_list, coffee=1, tea=2, cake=1, bread=3)
show_list(shopping_list)


# In[ ]:




