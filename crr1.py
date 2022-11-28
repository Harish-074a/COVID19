#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df=pd.read_csv("Covid Data.csv")


# In[4]:


df


# In[5]:


df.SEX.value_counts()


# In[6]:


df["PATIENT_TYPE"].value_counts()


# In[7]:


df.info()


# In[8]:


df.PREGNANT=df.PREGNANT.replace(97,2)
df.PREGNANT=df.PREGNANT.replace(99,2)


# In[9]:


df


# In[10]:


df= df[(df.PNEUMONIA == 1) | (df.PNEUMONIA == 2)]
df = df[(df.DIABETES == 1) | (df.DIABETES == 2)]
df = df[(df.COPD == 1) | (df.COPD == 2)]
df = df[(df.ASTHMA == 1) | (df.ASTHMA == 2)]
df = df[(df.INMSUPR == 1) | (df.INMSUPR == 2)]
df = df[(df.HIPERTENSION == 1) | (df.HIPERTENSION == 2)]
df = df[(df.OTHER_DISEASE == 1) | (df.OTHER_DISEASE == 2)]
df = df[(df.CARDIOVASCULAR == 1) | (df.CARDIOVASCULAR == 2)]
df = df[(df.OBESITY == 1) | (df.OBESITY == 2)]
df = df[(df.RENAL_CHRONIC == 1) | (df.RENAL_CHRONIC == 2)]
df = df[(df.TOBACCO == 1) | (df.TOBACCO == 2)]


# In[ ]:





# In[11]:


df


# In[12]:


df[(df.PATIENT_TYPE==1)&(df.SEX==1)].count()


# In[13]:


df[(df.PATIENT_TYPE==2)&(df.SEX==1)].count()


# In[14]:


df[(df.PATIENT_TYPE==1)&(df.SEX==2)].count()


# In[15]:


df[(df.PATIENT_TYPE==2)&(df.SEX==2)].count()


# In[ ]:


# subsetting the patients whoes age is less than 20


# In[40]:


less20=df.query("AGE<20")


# In[41]:


less20


# In[42]:


less20.AGE.count()


# In[43]:


# finding out the patients who are less than 20 age who having a smoking habbit


# In[44]:


less20.TOBACCO.value_counts()


# In[45]:


# 


# In[46]:


df.PREGNANT.value_counts()


# In[47]:


less20.PREGNANT.value_counts()


# In[51]:


less20.PREGNANT=less20.PREGNANT.replace(98,2)


# In[49]:


# fetching out no of people who are pregnent below age 


# In[52]:


less20.PREGNANT.value_counts()


# In[38]:


less20


# In[ ]:




