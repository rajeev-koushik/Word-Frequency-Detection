#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import nltk
# nltk.download('stopwords') #Uncomment when running for the first time to download, comment it out after
from nltk.corpus import stopwords
stop = stopwords.words('english')

col = [2] #Index of the column to read
df = pd.read_excel('set_1_4.xlsx', usecols=col) #Enter filename
df.columns = ["tweet"] #Name the column for simplicity

df["tweet"] = df["tweet"].str.lower()
df["cleaned"] = df["tweet"].apply(lambda x: ' '.join([word for word in str(x).split() if word not in (stop)])) #Stop words removal
df["cleaned"] = df["cleaned"].str.replace('[#,@,&,?,!,.,\,,-]', '') #Special characters removal
freq = pd.Series(' '.join(df["cleaned"]).split()).value_counts()[:75] #Change the value of 75 to see the desired number of words

print(freq)
freq.to_csv("Word_Freq.csv")

