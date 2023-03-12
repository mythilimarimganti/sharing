#!/usr/bin/env python
# coding: utf-8

# # MYTHILI MARIMGANTI

# 
# # <font color=RED>SPARKS fOUNDATION : EXPLORATORY DATA ANALYSIS USING SAMPLESUPERSTORE DATA SET </font>

# # IMPORTING NECESSARY LIBRARIES AND REQUIRED DATA

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data=pd.read_csv(r"C:\Users\HP\Downloads\SampleSuperstore.csv")


# In[4]:


data.head()


# In[5]:


data.shape


# In[6]:


data.columns


# In[7]:


data.info


# In[8]:


data.isnull().sum()


# In[9]:


print(data['Category'].unique())


# In[10]:


print(data['State'].unique())


# In[11]:


total_states=data['State'].nunique()
print("There are %d states in this df."%total_states)


# In[12]:


print(data['Sub-Category'].unique())


# In[13]:


total_subcategory=data['Sub-Category'].nunique()
print("Categories are divided into %d subcategories"%total_subcategory)


# In[14]:


data['Segment'].value_counts()


# In[15]:


data.describe()


# # CREATING LOSS DATA FRAME

# In[16]:


loss=data[data['Profit'] < 0]
loss


# In[17]:


loss.shape


# In[18]:


loss.describe()


# In[19]:


total_loss=np.negative(loss['Profit'].sum())
print("Total loss = %.2f" %total_loss)


# In[23]:


loss.groupby(by='Segment').sum()


# In[73]:


loss.groupby(by='Sub-Category').sum()


# In[74]:


loss['Sub-Category'].value_counts()


# In[75]:


loss.groupby(by='City').sum().sort_values('Profit',ascending=True).head(10)


# In[76]:


loss.sort_values(['Sales'],ascending=True).groupby(by='Category').mean()


# In[77]:


data.groupby(['State']).sum()['Sales'].nsmallest(10)


# In[78]:


data.sort_values(['Segment'],ascending=True).groupby('Segment').sum()


# In[79]:


data.groupby(by='Region').sum()


# # VISUALIZATION

# In[22]:


plt.rcParams['figure.figsize']=(15,10)
plt.bar(loss['Sub-Category'],loss['Sales'])
plt.rcParams.update({'font.size':10})
plt.xlabel('Sub_Category')
plt.ylabel('Sales')


# In[81]:


plt.rcParams['figure.figsize']=(28,8)
plt.bar(data['Sub-Category'],data['Sales'])
plt.rcParams.update({'font.size':14})
plt.xlabel('Sub_Category')
plt.ylabel('Sales')


# In[82]:


plt.rcParams['figure.figsize']=(28,8)
plt.bar(data['Sub-Category'],data['Discount'])
plt.rcParams.update({'font.size':14})
plt.xlabel('Sub_Category')
plt.ylabel('Discount')


# In[83]:


plt.rcParams['figure.figsize']=(8,6)
plt.bar(data['Ship Mode'],data['Sales'])
plt.rcParams.update({'font.size':14})
plt.xlabel('Ship Mode')
plt.ylabel('Sales')


# In[84]:


plt.rcParams['figure.figsize']=(5,5)
sns.countplot(x=data.Segment)
plt.show()


# In[88]:


plt.rcParams['figure.figsize']=(10,5)
plt.rcParams.update({'font.size':12})
sns.countplot(x='Region',data=data)
plt.show()


# In[92]:


data.corr()
sns.heatmap(data.corr(),cmap='Reds',annot=True);
plt.rcParams['figure.figsize']=(8,8)


# * sales and profit are moderately correlated
# * discount and profit are negatively correlated

# The main reason which leads to loss is Discount as if some areas lead to loss due to more discounts, and some areas lead to fewer sales due to fewer discounts, hence it needs to be improved.
# 
# It is better to give more discounts during festival seasons, additionally, that will result in more sales.
# 
# The Home office segment needs better improvement.
# 
# Some cities have fewer sales, lack of awareness can be the reason for this, hence advertising in those cities might help in more sales.
