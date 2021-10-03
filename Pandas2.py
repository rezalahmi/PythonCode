#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


titanic = pd.read_csv(r'titanic.csv')


# In[3]:


titanic


# In[4]:


titanic.info()


# In[5]:


titanic.describe()


# In[6]:


#if you want to desctibe just non numeric value use O in include
titanic.describe(include='O')


# In[8]:


titanic.describe(include = 'all')


# In[9]:


type(titanic)


# In[10]:


len(titanic)


# In[11]:


round(titanic,0)


# In[12]:


titanic.shape


# In[13]:


titanic.size


# In[14]:


titanic.index


# In[15]:


titanic.columns


# In[16]:


#return min values from each columns
titanic.min()


# In[17]:


titanic.max()


# In[18]:


#mean values of each columns
titanic.mean()


# In[23]:


titanic.sort_values(by='Age',ascending=False)


# In[6]:


type(titanic['Age'])


# In[7]:


type(titanic[['Age']])


# In[ ]:


#if you want to select one column 
#from data frame you should decide which output is benefical, data frame or data seires.


# In[8]:


#also you can use dot notation
titanic.Age


# In[2]:


olympics = pd.read_csv(r'athlete_events.csv')


# In[10]:


olympics.info()


# In[11]:


olympics.describe()


# In[12]:


olympics.head()


# In[38]:


olympics = pd.read_csv(r'athlete_events.csv',index_col = 'ID')
#index_col:Column(s) to use as the row labels of the DataFrame, either given as string name or column index.


# In[4]:


olympics


# In[16]:


olympics.iloc[0]


# In[18]:


type(olympics.iloc[0])


# In[20]:


olympics.iloc[-1]


# In[23]:


olympics.iloc[[0,1,2]]


# In[24]:


olympics.iloc[0:5]


# In[25]:


olympics.iloc[-5:]


# In[26]:


olympics.iloc[[4,67,123]]


# In[28]:


#with iloc, you can get two index and return the cell of data frame
olympics.iloc[0,1]


# In[30]:


olympics.iloc[0,0:5]


# In[31]:


olympics.iloc[0:3,0:5]


# In[33]:


#.loc[] is primarily label based, but may also be used with a boolean array.
olympics.loc[3]


# In[34]:


olympics.loc[3,'Medal']


# In[35]:


olympics.loc[3,['Medal','Year']]


# In[36]:


olympics.loc[[3,4],['Medal','Year']]


# In[37]:


olympics.loc[1:5,'Name':'Team']


# In[38]:


olympics.loc[5]


# In[39]:


#Data Series
age = olympics['Age']


# In[4]:


age


# In[5]:


age.describe()


# In[6]:


age.count()


# In[7]:


age.size


# In[8]:


len(age)


# In[9]:


#sum function can't handle nan values
sum(age)


# In[10]:


age.sum()


# In[11]:


#skipna is a prameter in sum method to ignore the nan values
age.sum(skipna=True)


# In[12]:


age.sum(skipna=False)


# In[13]:


age.mean()


# In[14]:


age.median()


# In[15]:


age.std()


# In[16]:


age.min()


# In[17]:


age.max()


# In[18]:


#return unique values
age.unique()


# In[20]:


#if you want to count number of unique element, use len function
len(age.unique())


# In[21]:


#also this method return number of unique values
age.nunique()


# In[22]:


#you can see, there is a differente, nunique method has parameteres for NAN
age.nunique(dropna=False)
#dropna is True by defualt, so didn't count NAN


# In[23]:


#if you want to frequency of each element, use this method
age.value_counts()


# In[24]:


#if you set sort by false, the data show by apperiance
age.value_counts(sort = False)


# In[25]:


#this parameter ignore NaN
age.value_counts(dropna=True)


# In[28]:


age.value_counts(ascending=True)


# In[29]:


age.value_counts(normalize=True)
# If True then the object returned will contain the relative
    #frequencies of the unique values.


# In[30]:


#Rather than count values, group them into half-open bins
age.value_counts(bins=5)


# In[5]:


name = olympics['Name']


# In[6]:


name.head()


# In[7]:


name.tail()


# In[10]:


name.describe()


# In[11]:


name.shape


# In[12]:


name.size


# In[14]:


name.count()


# In[15]:


name.min()


# In[16]:


name.unique()


# In[17]:


len(name.unique())


# In[18]:


name.nunique()


# In[19]:


name.nunique(dropna=False)


# In[20]:


name.nunique(dropna=True)


# In[21]:


name.value_counts()


# In[24]:


name.value_counts(normalize=True)


# In[25]:


name.value_counts(normalize=True).head()


# In[26]:


summer = pd.read_csv(r'Summer-Olympic-medals-1976-to-2008.csv')


# In[27]:


summer.head()


# In[29]:


summer.iloc[0]


# In[31]:


#for creating data series, you can use column for importing data
pd.read_csv(r'Summer-Olympic-medals-1976-to-2008.csv',squeeze=True,usecols=['Athlete'])


# In[32]:


athlete = pd.read_csv(r'Summer-Olympic-medals-1976-to-2008.csv',squeeze=True,usecols=['Athlete'])


# In[33]:


athlete.head()


# In[34]:


athlete.tail()


# In[35]:


athlete.sort_values()


# In[36]:


#if you want sort the values of data series
athlete.sort_values(inplace=True)


# In[37]:


athlete


# In[44]:


#if you want 3th largest age
age.sort_values(ascending=False).head(3)


# In[45]:


#also you can use nlargest
age.nlargest(3)


# In[48]:


age.sort_values(ascending=True).iloc[:3]


# In[49]:


age.nsmallest(3)


# In[53]:


olympics


# In[55]:


olympics.Age.idxmax()


# In[58]:


olympics.Age.idxmin()


# In[73]:


olympics.loc[71691]


# In[74]:


olympics.loc[128719]


# In[75]:


olympics.info()


# In[76]:


olympics.index


# In[77]:


type(olympics.index)


# In[78]:


olympics.columns


# In[79]:


type(olympics.columns)


# In[13]:


olympics = pd.read_csv(r'athlete_events.csv',index_col='Name')


# In[85]:


olympics.head()


# In[86]:


olympics.index


# In[87]:


type(olympics.index)


# In[88]:


olympics.index[0]


# In[91]:


#if you want to know column values are unique, use is_unique attribute
olympics.index.is_unique


# In[94]:


#get_loc method, get label and retrun location
olympics.index.get_loc('A Dijiang')


# In[96]:


olympics.index


# In[99]:


#sometime you should reset the index on data frame. use reset_index
olympics.reset_index()


# In[100]:


olympics.head()


# In[107]:


#be sure use inplace parameter
olympics.reset_index(inplace=True)


# In[108]:


olympics.head()


# In[98]:


#if you want to set index, use set_index
olympics.set_index('ID')


# In[109]:


#if you set index column, the index_column remove from list of column, so use
#drop parameter to don't do that
#olympics.reset_index(inplace=True)
olympics.set_index('ID',drop=False)
olympics.head()


# In[111]:


olympics.index


# In[112]:


olympics.index.is_unique


# In[113]:


#if you want to create uniqu index, use this technique
new_index = ['Athlete_{}'.format(i) for i in range(1,olympics.index.size+1)]


# In[114]:


new_index


# In[115]:


olympics.index = new_index


# In[116]:


olympics.head()


# In[117]:


olympics.tail()


# In[118]:


#to change the name of columns
olympics.rename(columns={'Sex':'Gender'},inplace=True)


# In[119]:


olympics.head()


# In[5]:


titanic[titanic.Sex == 'male']


# In[6]:


titanic.Fare[titanic.Sex == 'male']


# In[7]:


#we recomend this method, because this format can use for more than one columns
titanic.loc[titanic.Sex == 'male',['Age','Fare']]


# In[10]:


#if you want to show all numeric data. use this techniqu
mask = titanic.dtypes != object
titanic.loc[:,mask]


# In[12]:


titanic.loc[:,~mask]


# In[14]:


olympics.info()


# In[17]:


#between is usefull filter
olympics[olympics.Year.between(1990,1999)]


# In[18]:


olympics[olympics.Year.between(1990,1999,inclusive=True)]


# In[19]:


#if you want to check something within a set use isin
mask1 = [1992,2012]
olympics.loc[olympics.Year.isin(mask1)]


# In[28]:


olympics.loc[~olympics.Year.isin(mask1)]['Year'].unique()


# In[29]:


titanic.info()


# In[44]:


#Return whether any element is True, potentially over an axis.
(titanic.Sex == 'Male').any()


# In[34]:


#Return whether all elements are True, potentially over an axis.
(titanic.Sex != 'Male').all()


# In[37]:


titanic.loc[titanic.Sex == 'Male']


# In[38]:


titanic.Age.mean()


# In[43]:


(titanic.Age >= 90).any()


# In[45]:


titanic.head()


# In[46]:


titanic.drop(index=0,inplace=True)


# In[47]:


titanic.head()


# In[51]:


(titanic.Age >=80).value_counts()


# In[52]:


titanic.loc[titanic.Age>=80]


# In[53]:


olympics.info()


# In[55]:


#if you want to know is a value in the data frame
1996 in olympics.Year.values


# In[56]:


olympics.head(10)


# In[3]:


(titanic.Age <=1).any()


# In[4]:


titanic.loc[titanic.Age <=1,'Age']=1


# In[5]:


(titanic.Age <1).any()


# In[6]:


#if you want to replace one value to new value, use replace method
titanic.replace(0,'Zero')


# In[7]:


age = titanic.Age


# In[9]:


age._is_view


# In[11]:


temp = titanic


# In[12]:


temp._is_view


# In[14]:


age = titanic.Age.copy()


# In[15]:


age._is_view


# In[3]:


titanic.agg('mean')


# In[4]:


titanic.mean()


# In[5]:


titanic.max()


# In[6]:


titanic.agg('max')


# In[7]:


titanic.agg(['mean','std'])


# In[8]:


titanic.agg({'survived':'mean','age':['mean','max','min']})


# In[12]:


titanic[titanic.survived==1].agg({'age':['mean','max','min','median']})


# In[16]:


sales = pd.read_csv(r'sales.csv')
sales


# In[17]:


sales.min(axis=0)


# In[19]:


sales.min(axis=1)


# In[25]:


def range(series):
    return series.max() - series.min()


# In[29]:


sales.apply(lambda x:x.max(),axis=0)


# In[32]:


sales.apply(lambda x : x.min(),axis=0)


# In[33]:


summer = pd.read_csv(r'summer.csv')


# In[34]:


summer.head()


# In[35]:


summer.Athlete.head()


# In[48]:


def findComma(s):
    index = 1
    for i in s:
        if i != ',':
            index+=1
        else:
            break
    return index-1


# In[49]:


summer.Athlete.apply(lambda x : x[0:findComma(x)])


# In[51]:


summer.Athlete.map(lambda x : x[0:findComma(x)])


# In[80]:


summer.Athlete.apply(lambda x : x.split(',') )


# In[81]:


names = summer.Athlete.loc[:10].copy()


# In[82]:


names


# In[83]:


#in pandas, you can use strig method with str
names.str.lower()


# In[84]:


names.str.len()


# In[86]:


names.str.split(',')


# In[87]:


names.str.find('AND')


# In[90]:


names.str.split(',',n=2,expand=True)


# In[57]:


titanic = titanic.iloc[0:50,:]


# In[58]:


titanic.info()


# In[66]:


#if you use list of columns to set index, you define heirachical indexing
titanic.set_index(['pclass','sex'],inplace=True)


# In[60]:


titanic.sort_index()


# In[63]:


titanic.sort_index(ascending=[False,True],inplace=True)


# In[64]:


#if you have heirachical index and want to swap between them
titanic.swaplevel()


# In[65]:


titanic.reset_index(inplace=True)


# In[69]:


#if you have heirachical index, loc can slice you data base on index
titanic.loc[1]


# In[71]:


titanic.loc[[1,2]]


# In[73]:


titanic.loc[(1,'male')]


# In[74]:


titanic.loc[(1,'male'),'age']


# In[ ]:




