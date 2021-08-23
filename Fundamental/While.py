#!/usr/bin/env python
# coding: utf-8

# In[1]:


#With the while loop we can execute a set of statements as long as a condition is true.
i = 0
while i < 10 :
    print("the value of i is :",i)
    i = i + 1


# In[2]:


i = 1
while i < 6:
  print(i)
  i += 1


# In[15]:


#With the break statement we can stop the loop even if the while condition is true
flag = True
while flag:
    name = input("please enter your name:")
    grade = int(input("please enter your grade:"))
    my_dic[name] = grade
    yn = input("do you want to continue?")
    if yn == "no":break
i = len(my_dic.keys()) -1
sum = 0
for x in my_dic:
    sum += my_dic[x]
print("average is :",sum/len(my_dic.keys()))


# In[17]:


#With the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# In[18]:


while True:
    name = input("please enter your name:")
    grade = int(input("please enter your grade:"))
    my_dic[name] = grade
    yn = input("do you want to continue?")
    if yn == "no":break
i = len(my_dic.keys()) -1
sum = 0
for x in my_dic:
    sum += my_dic[x]
print("average is :",sum/len(my_dic.keys()))


# In[24]:


my_list = ["reza",12,"ali",16,"raheleh",20]
new_list = []
i = -1
while True:
    i += 1
    if i >= len(my_list):
        break
    if type(my_list[i]) == str:
        new_list.append(my_list[i])
        continue
    elif not(type(my_list[i]) == "str"):
        continue
print(new_list)


# In[ ]:




