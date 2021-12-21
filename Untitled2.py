#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


# In[2]:


from datetime import datetime
import pandas as pd


# In[ ]:


#First off i will be using pandas , and i will create  dataframes for text and calls
# creates variables to store timestamp, calling numbers, receiving number, and call duration
# convert timestamps to datetime object, and convert durations to integer


# In[3]:



times_stamp = [x[2] for x in calls]


# In[4]:


calling_number = [x[0] for x in calls]


# In[5]:


receiving_number = [x[1] for x in calls]


# In[6]:


duration_seconds = [x[3] for x in calls]


# In[7]:


duration_seconds2 =[]
for x in duration_seconds:
    x = int(x)
    duration_seconds2.append(x)


# In[8]:


times_stamp2 =[]
for x in times_stamp:
    x = datetime.strptime(x,'%d-%m-%Y %H:%M:%S')
    times_stamp2.append(x)


# In[9]:


my_calls_dict ={'calling_number': calling_number,'receiving_number':receiving_number, 'times_stamp':times_stamp2,'duration_seconds':duration_seconds2 }


# In[10]:


df = pd.DataFrame(my_calls_dict)


# In[11]:


df.head()


# In[12]:


last_call = df.times_stamp.max()


# In[13]:


last_record = df[df.times_stamp == last_call]


# In[14]:


last_record[['calling_number']]


# In[15]:


for index, row in last_record.iterrows():
    print("Last record of calls,",row['calling_number'],"calls", row['receiving_number'],"at time", row['times_stamp'],",","lasting",row['duration_seconds'],"seconds")


# In[ ]:





# In[ ]:





# In[16]:


longest_call = df.duration_seconds.max()


# In[17]:


longest_time = df[df.duration_seconds == longest_call]


# In[18]:


calling_num = [x[0] for x in texts]


# In[19]:


receiving_number = [x[1] for x in texts]


# In[20]:


times = [x[2] for x in texts]


# In[21]:


times_stamp =[]
for x in times:
    x = datetime.strptime(x,'%d-%m-%Y %H:%M:%S')
    times_stamp.append(x)


# In[22]:


my_text_dict ={'calling_number': calling_num,'receiving_number':receiving_number,'times_stamp':times_stamp }


# In[23]:


my_text_dict.keys()


# In[24]:


#my_text_dict[0]


# In[25]:


first_text = min(times_stamp)


# In[26]:


first_text


# In[27]:


text_df = pd.DataFrame(my_text_dict)


# In[28]:


text_df.info()


# In[29]:


first_text = text_df.times_stamp.min()


# In[30]:


first_text_record = text_df[text_df.times_stamp == first_text]


# In[31]:


first_text_record


# In[32]:


for index, row in first_text_record.iterrows():
    print("First record of texts,",row['calling_number'],"texts", row['receiving_number'],"at time", row['times_stamp'])


# In[33]:


df.calling_number.nunique()


# In[34]:


df.receiving_number.nunique()


# In[35]:


text_df.calling_number.nunique()


# In[36]:


text_df.receiving_number.nunique()


# In[37]:


df.calling_number.value_counts().head(10)


# In[64]:


df2 = df.groupby(['calling_number'])[['duration_seconds']].sum()


# In[73]:


df2[df2.duration_seconds == df2.duration_seconds.max()]


# In[69]:


df3 = df.groupby(['receiving_number'])[['duration_seconds']].sum()


# In[70]:


df3.duration_seconds.max()


# In[ ]:





# In[54]:


for index, row in longest_time.iterrows():
    print(row['calling_number'],"spent the longest time,", row['times_stamp'])


# In[ ]:





# In[ ]:


for record in call_records:
    if record['times_stamp'] == first_text:
        print(record)
    


# In[ ]:


call_records[0]['times_stamp'] == first_text


# In[ ]:




