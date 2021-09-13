#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[38]:


#Read a comma-separated values (csv) file into DataFrame.
df_food = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\7. Data Analytics (Pandas)\2.1 Food Orders.csv')


# In[5]:


#Return the first n rows.
df_food.head()


# In[6]:


df_food.head(10)


# In[9]:


#Get the number of rows: len(df)
len(df_food)


# In[12]:


#Get the number of columns: len(df.columns)
len(df_food.columns)


# In[14]:


#Get the number of rows and columns: df.shape
df_food.shape


# In[49]:


#The DataFrames object has a method called info(), that gives you more information about the data set.
df_food.info()


# In[16]:


#Descriptive statistics include those that summarize the central tendency, 
#dispersion and shape of a dataset’s distribution, excluding NaN values.
df_food.describe()


# In[17]:


df_food.describe(include='all')


# In[19]:


#Return the dtypes in the DataFrame.
df_food.dtypes


# In[20]:


#Cast a pandas object to a specified dtype dtype.
df_string = df_food.astype('object')
df_string.dtypes


# In[22]:


df_float = df_string.astype({'Food Order ID':'int64','Quantity':'int64','Price Per Item':'float'})
df_float.dtypes


# In[23]:


df_food.head()


# In[39]:


df_food['Total Amount'] = df_food['Quantity'] * df_food['Price Per Item']


# In[25]:


df_food.head()


# In[3]:


df_food.head()


# In[5]:


df_food[['Food Order ID','Customer ID','Restaurant Name','Meal Ordered','Quantity','Price Per Item']].head()


# In[7]:


df_food['totla amount'] = df_food['Quantity'] * df_food['Price Per Item']
df_food.head()


# In[8]:


#if you want to determined the row situation which saticfy condition or not, use filter like this
df_food['Restaurant Name'] == "Oasis Seafood"


# In[9]:


df_food[df_food['Restaurant Name'] == "Oasis Seafood"]


# In[14]:


df_food[df_food['totla amount'] > 50]


# In[15]:


#you can combine filter with logical operator & , |
df_food[(df_food['Quantity']>2)|(df_food['totla amount']>40)]


# In[16]:


df_food[(df_food['Quantity']>2)&(df_food['totla amount']>40)]


# In[19]:


df_food[((df_food['Quantity']>2)|(df_food['totla amount']>40))&(df_food['Day']=="Friday")]


# In[24]:


#Whether each element in the DataFrame is contained in values.
df_food[df_food['Customer ID'].isin(['A','B'])]


# In[25]:


df_food[(df_food['Customer ID'].isin(['A','B']))&(df_food['totla amount']>30)]


# In[31]:


#est if the start of each string element matches a pattern.
#str.startswith
df_food[df_food['Day'].str.startswith('W')]


# In[32]:


df_food[df_food['Day'].str.startswith('S')]


# In[35]:


#endswith(pat, na=None)
#Test if the end of each string element matches a pattern.
df_food[df_food['Meal Ordered'].str.endswith("er")]


# In[4]:


#str.contains(pat, case=True, flags=0, na=None, regex=True)
#Test if pattern or regex is contained within a string of a Series or Index.
df_food[df_food['Restaurant Name'].str.contains("in")]


# In[6]:


#DataFrame.sort_values
#Sort by the values along either axis
df_food.sort_values(by="Total Amount", ascending=True).head(10)


# In[7]:


df_food.sort_values(by="Total Amount", ascending=False).head(10)


# In[9]:


df_food.sort_values(by=["Total Amount","Quantity"], ascending=False).head(10)


# In[11]:


df_food.sort_values(by=["Meal Ordered","Quantity"], ascending=(False,True)).head(10)


# In[18]:


df_food.head()


# In[19]:


#pandas.DataFrame.loc
#Access a group of rows and columns by label(s) or a boolean array.
df_food.loc[1,['Meal Ordered']]


# In[20]:


df_food.loc[1,:]


# In[21]:


df_food.loc[df_food['Price Per Item']>15,:]


# In[26]:


df_food.loc[df_food['Price Per Item']>15,:].sort_values(by=['Meal Ordered','Total Amount'],                                                        ascending=(True,True))


# In[27]:


#Bucketing or Binning of continuous variable in pandas python to discrete chunks is depicted
#for bucketing using loc method, first you must create column with defualt value
df_food['Amount - Bucket'] = '--out of bound--'
df_food.head()


# In[30]:


#then filter values and assign label to them
df_food.loc[(df_food['Total Amount']>0)&(df_food['Total Amount']<=20),'Amount - Bucket']='Low'
df_food.loc[(df_food['Total Amount']>20)&(df_food['Total Amount']<=40),'Amount - Bucket']='Mid'
df_food.loc[(df_food['Total Amount']>40),'Amount - Bucket']='High'


# In[31]:


df_food.head()


# In[33]:


#for bucketing you can use another way, using cau method
#pandas.cut
#Bin values into discrete intervals.Use cut when you need to segment and sort data values into bins
bin = [0,20,40,60]
df_food['Amount - Binning'] = pd.cut(df_food['Total Amount'],bin)
df_food.head()


# In[38]:


#We will be assigning label to each bin
bin_label = ['low','mid','high']
df_food['Amount - Bucketing'] = pd.cut(df_food['Total Amount'],bin,labels=bin_label)
df_food.head()


# In[40]:


#bucketing using loc method
df_food['Vegan'] = 'Not Vegan'
df_food.loc[df_food['Restaurant Name'].str.contains('Green'),'Vegan']='Vegan'
df_food.head()


# In[4]:


#replacing data
df_food.head()


# In[6]:


df_food['Customer ID'].unique()


# In[7]:


#DataFrame.replace
#Values of the DataFrame are replaced with other values dynamically.
df_food['Customer ID'].replace({'A':'A001','B':'B001','C':'C001','D':'D001','E':'E001'                               ,'F':'F001','G':'G001','H':'H001','I':'I001','J':'J001'                               ,'K':'K001','L':'L001','M':'M001'},inplace=True)


# In[8]:


df_food.head(10)


# In[10]:


df_food['Day'].unique()


# In[11]:


df_food['Day'].replace({'Monday':'01 - Monday','Tuesday':'02 - Tuesday'                       ,'Wednesday':'03 - Wednesday','Thursday':'04 - Thursday'                       ,'Friday':'05 - Friday','Saturday':'06 - Saturday'                       ,'Sunday':'07 - Sunday'},inplace = True)


# In[12]:


df_food.head(10)


# In[15]:


df_food.sort_values(by=['Day'],ascending = True)


# In[32]:


#Group DataFrame using a mapper or by a Series of columns
df_food.groupby('Customer ID')


# In[33]:


df_food.groupby('Customer ID').max()


# In[35]:


df_food.groupby(['Customer ID'],as_index = False).mean()


# In[36]:


df_food.groupby(['Customer ID'],as_index =False).count()


# In[37]:


df_food.groupby(['Customer ID'],as_index = False).agg({'Total Amount':['max','min','mean','count']})


# In[39]:


df_food.groupby(['Restaurant Name'],as_index = False).agg({'Total Amount':['max','min','mean','count']})


# In[40]:


df_food.groupby(['Day'],as_index = False).agg({'Total Amount':['max','min','mean','count']})


# In[42]:


df_food.groupby(['Restaurant Name','Day']).mean()


# In[46]:


df_food.groupby(['Restaurant Name','Meal Ordered']).sum()


# In[1]:


import pandas as pd


# In[3]:


df_football = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\7. Data Analytics (Pandas)\38.1 Football (Soccer) Teams - Null Values.csv')


# In[4]:


df_football.head()


# In[5]:


df_football.describe()


# In[7]:


df_football.isna()


# In[9]:


#The fillna() method allows us to replace empty cells with a value
df_football['Champions League'].fillna(df_football['Champions League'].mean(),inplace=True)


# In[10]:


df_football['League Champions'].fillna(df_football['League Champions'].mean(),inplace=True)


# In[11]:


df_football


# In[12]:


new_df_football = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\7. Data Analytics (Pandas)\38.1 Football (Soccer) Teams - Null Values.csv')
new_df_football['Champions League'].fillna(1,inplace=True)
new_df_football['League Champions'].fillna(20,inplace=True)


# In[13]:


new_df_football = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\7. Data Analytics (Pandas)\38.1 Football (Soccer) Teams - Null Values.csv')


# In[14]:


new_df_football


# In[15]:


new_df_football['Champions League'].isna()


# In[17]:


any(new_df_football['Champions League'].isna())


# In[21]:


#if you want to know is NaN in the column, use any method like abouv
for x in new_df_football.columns:
    if any(new_df_football[x].isna()):
        print(x)


# In[26]:


def check_NaN(df):
    for col in df.columns:
        if any(df[col].isna()):
            df[col].fillna(df[col].mean(),inplace=True)
    return df


# In[23]:


new_df_football


# In[27]:


new_df_football_withoutNaN=check_NaN(new_df_football)


# In[28]:


new_df_football_withoutNaN


# In[29]:


df_resturant = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\7. Data Analytics (Pandas)\40.1 Restaurants - Duplicates.csv')
df_resturant.head(10)


# In[31]:


#Return boolean Series denoting duplicate rows.
df_resturant.duplicated()


# In[41]:


if any(df_resturant.duplicated()):
    print("we have duplicate")


# In[42]:


#if you want to show duplicated rows
df_resturant[df_resturant.duplicated()]


# In[49]:


df_resturant[df_resturant.duplicated(['Quantity'])]


# In[50]:


df_resturant[df_resturant.duplicated(['Meal Description'])]


# In[51]:


#DataFrame.drop_duplicates
#Return DataFrame with duplicate rows removed.
df_resturant_i = df_resturant.drop_duplicates(df_resturant.columns)


# In[54]:


any(df_resturant_i.duplicated())


# In[55]:


def check_duplicate(df):
    if any(df.duplicated()):
        return df.drop_duplicates(df.columns)


# In[57]:


df_resturant_j = check_duplicate(df_resturant)
any(df_resturant_j.duplicated())


# In[1]:


import pandas as pd


# In[2]:


df_show_A = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\7. Data Analytics (Pandas)\62.2 Joining - 2 Keys - A.csv')
df_show_B = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\7. Data Analytics (Pandas)\62.1 Joining - 2 Keys - B.csv')


# In[4]:


df_show_A.head()


# In[5]:


df_show_B.head()


# In[3]:


df_show_A.merge(df_show_B,how='inner',left_on='Shop ID',right_on='Shop ID')


# In[8]:


pd.merge(df_show_A,df_show_B,how='left',left_on=['Shop ID','Department'],right_on=['Shop ID','Department'])


# In[4]:


#if you want to join two dataframe with more than one culomns, use merge
df_merge_AB = pd.merge(df_show_A,df_show_B,how='left',left_on=['Shop ID','Department'],right_on=['Shop ID','Department'])


# In[5]:


df_merge_AB


# In[6]:


df_merge_AB['Expensive'] = df_merge_AB['Revenue'] - df_merge_AB['Profit']


# In[13]:


df_merge_AB


# In[8]:


#for cleaning data from unwanted columns, use this format
df_AB_clean = df_merge_AB[['Shop ID','Department','Shop Name_x','Shop Region','Revenue','Profit'                          ,'Expensive','No of Employees','Shop Size (Square Ft)']]


# In[16]:


df_AB_clean


# In[9]:


#for rename data frame, use dictionary like this
df_AB_master = df_AB_clean.rename(columns={'Shop Name_x':'Shop Name'})


# In[22]:


df_AB_master


# In[10]:


#if you want to calculate comulative sum or runing total, use this method
df_AB_master['Revenue - Comulative Sum'] = df_AB_master['Revenue'].expanding().sum()


# In[29]:


df_AB_master


# In[11]:


#with this method, you can calculate comulative mean
df_AB_master['Revenue - Comulative Mean'] = df_AB_master['Revenue'].expanding().mean()


# In[31]:


df_AB_master


# In[32]:


df_AB_master['Revenue - Comulative Mean'] = round(df_AB_master['Revenue'].expanding().mean(),2)
df_AB_master


# In[14]:


df_AB_master.index+1


# In[15]:


#with index attribute you can add row number to data frame
df_AB_master['Row Number'] = df_AB_master.index+1


# In[16]:


df_AB_master


# In[17]:


#if you want to ordering data based on rank, use rank() method
df_AB_master.rank()


# In[21]:


df_AB_master['Revenue'].rank(ascending=True)


# In[28]:


df_AB_master['Rank - Revenue'] = df_AB_master['Revenue'].rank(ascending=False)


# In[29]:


df_AB_master


# In[34]:


#A Pandas Series is like a column in a table.

#It is a one-dimensional array holding data of any type.
a = [1,5,7]
my_series = pd.Series(a)
my_series


# In[35]:


print(my_series[1])


# In[36]:


#With the index argument, you can name your own labels.
my_series = pd.Series(a,index = ['x','y','z'])
print(my_series['y'])


# In[37]:


#You can also use a key/value object, like a dictionary, when creating a Series.
calories = {"day1": 420, "day2": 380, "day3": 390}
my_series = pd.Series(calories)
print(my_series['day1'])


# In[45]:


#Big data sets are often stored, or extracted as JSON.

#JSON is plain text, but has the format of an object, 
#and is well known in the world of programming, including Pandas.
#JSON objects have the same format as Python dictionaries.

df_jason = pd.read_json('D:\data.js')


# In[46]:


df_jason


# In[48]:


#There is also a tail() method for viewing the last rows of the DataFrame.

#The tail() method returns the headers and a specified number of rows, starting from the bottom.
df_jason.tail()


# In[51]:


df_jason.info()


# In[64]:


df_dirty = pd.read_csv('F:\Document\PythonCode\dirtydata.csv')


# In[65]:


df_dirty.head()


# In[66]:


df_dirty.info()


# In[68]:


#Empty cells can potentially give you a wrong result when you analyze data.
#One way to deal with empty cells is to remove rows that contain empty cells.
new_df = df_dirty.dropna()
#the dropna() method returns a new DataFrame, and will not change the original.
new_df.info()


# In[69]:


temp_df_dirty = df_dirty
temp_df_dirty.info()


# In[71]:


#Now, the dropna(inplace = True) will NOT return a new DataFrame, 
#but it will remove all rows containg NULL values from the original DataFrame.
temp_df_dirty.dropna(inplace = True)
temp_df_dirty.info()


# In[73]:


df_dirty['Date']


# In[74]:


#for fix the wrong format of date, use to_datetime method
df_dirty['Date'] = pd.to_datetime(df_dirty['Date'])
df_dirty['Date']


# In[75]:


df_dirty.info()


# In[76]:


for x in df_dirty.index:
    if df_dirty.loc[x,'Duration']>120:
        df_dirty.loc[x,'Duration'] = 120


# In[78]:


df_dirty['Duration']


# In[83]:


for x in df_dirty.index:
    if df_dirty.loc[x,'Duration']>=120:
        df_dirty.loc[x,'Duration'] = (df_dirty['Duration'].mean())


# In[84]:


df_dirty['Duration']


# In[85]:


#A great aspect of the Pandas module is the corr() method.

#The corr() method calculates the relationship between each column in your data set.
#The corr() method ignores "not numeric" columns.
df_dirty.corr()


# In[87]:


#Pandas uses the plot() method to create diagrams.
df_dirty.plot()


# In[88]:


df_dirty.plot(kind='scatter',x = 'Duration', y = 'Calories')


# In[90]:


#Use the kind argument to specify that you want a histogram
df_dirty['Duration'].plot(kind='hist')


# In[ ]:




