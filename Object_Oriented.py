#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python is an object oriented programming language.

#Almost everything in Python is an object, with its properties and methods.

#A Class is like an object constructor, or a "blueprint" for creating objects.
#All classes have a function called __init__(), 
#which is always executed when the class is being initiated.
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("reza",38)
#The __init__() function is called automatically every time the class 
#is being used to create a new object.
print(p1.name,"_",p1.age)


# In[2]:


p2 = person("raheleh",38)
print(p2)


# In[3]:


type(p2)


# In[4]:


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("my name is ",self.name," and I'm ",self.age," year's old")
#The self parameter is a reference to the current instance of the class, 
#and is used to access variables that belong to the class.


# In[5]:


p3 = person("reza",38)
p3.show()


# In[6]:


#It does not have to be named self , you can call it whatever you like, 
#but it has to be the first parameter of any function in the class
class person:
    def __init__(reza,name,age):
        reza.name = name
        reza.age = age
    def show(sadra):
        print("my name is ",sadra.name," and I'm ",sadra.age," year's old")


# In[8]:


p4=person("raheleh",38)
p4.show()


# In[9]:


del p4.age


# In[10]:


p4.show()


# In[11]:


del p4


# In[34]:


#To create a class that inherits the functionality from another class, 
#send the parent class as a parameter when creating the child class
class student(person):
    def __init__(self,fname,age,major):
        person.__init__(self,fname,age)
        self.major = major


# In[35]:


s1 = student("reza",34,"math")


# In[23]:


s1.show()
print(s1.major)


# In[30]:


#Python also has a super() function that will make the child class 
#inherit all the methods and properties from its parent
class teacher(person):
    def __init__(self,fname,age,department):
        super().__init__(fname,age)
        self.department = department
    def show(self):
        super().show()
        print("I'm working in ",self.department)
#By using the super() function, you do not have to use the name of the parent element, 
#it will automatically inherit the methods and properties from its parent.


# In[31]:


t1 = teacher("reza",38,"computer")
t1.show()


# In[ ]:




