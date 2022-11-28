#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


# Importing a CSV File by pandas 


# In[2]:


df=pd.read_csv("Covid Data.csv")


# In[3]:


df


# In[ ]:


# Total count of each Column to find the  no.of values present in it 


# In[4]:


df.USMER.value_counts()


# In[5]:


df.MEDICAL_UNIT.value_counts()


# In[6]:



df.SEX.value_counts()


# In[7]:


df.PATIENT_TYPE.value_counts()


# In[8]:


df.INTUBED.value_counts()


# In[ ]:


# replacing the null values 97 & 99 are the unkowen values of the data set.


# In[9]:


df.INTUBED=df[df.columns[5]].replace(97,2)
df.INTUBED=df[df.columns[5]].replace(99,2)


# In[10]:


df.INTUBED.value_counts()


# In[67]:


df.PREGNANT=df.PREGNANT.replace(97,2)
df.PREGNANT=df.PREGNANT.replace(98,2)


# In[11]:


df.PREGNANT.value_counts()


# In[12]:


df.AGE.count()


# In[13]:


df.COPD=df.COPD.replace(98,2)


# In[14]:


df.ASTHMA=df.ASTHMA.replace(98,2)


# In[15]:


df.INMSUPR=df.INMSUPR.replace(98,2)


# In[16]:


df.HIPERTENSION=df.HIPERTENSION.replace(98,2)


# In[17]:


df.OTHER_DISEASE=df.OTHER_DISEASE.replace(98,2)


# In[18]:


df.CARDIOVASCULAR=df.CARDIOVASCULAR.replace(98,2)


# In[19]:


df.OBESITY=df.OBESITY.replace(98,2)


# In[20]:


df.RENAL_CHRONIC=df.RENAL_CHRONIC.replace(98,2)


# In[21]:


df.TOBACCO=df.TOBACCO.replace(98,2)


# In[22]:


df


# In[23]:


df.PATIENT_TYPE.value_counts()


# In[25]:


df.AGE.mean()


# In[28]:


df.ICU=df.ICU.replace(97,2)
df.ICU=df.ICU.replace(97,2)


# In[42]:


pplicu=df[(df.SEX) &(df.ICU==1)]


# In[43]:


print(ppl_icu)


# In[ ]:




