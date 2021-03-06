#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

df = pd.read_excel("/Users/victoreduardo/Downloads/league_of_legends.xlsx", )


# In[3]:


df.tail()


# In[47]:


k=df.keys();

#Columns 1-20 correspond to blue marks, we will forget about "gameId"
blue = df[k[1:21]]

#For the red, we still want to keep the first two columns
red = pd.concat([df['blueWins'], df[k[21:40]]], axis=1)

#We change blueWins for redWins, later we will rename the column "victory"
red['blueWins'] = (red['blueWins']+1)%2

#Now we rename the columns. 
newkeys=[];
for i in range(len(k)):
    if k[i][0] == 'b':
        newkeys.append(k[i][4:]) 
    if k[i][0] == 'r':
        newkeys.append(k[i][3:])

#Rename the columns for the blue data set
bk = blue.keys();
blue1 = blue.rename(columns = {bk[i]:newkeys[i] for i in range(len(bk))})
blue1['Color'] = 'Blue';
#Rename the columns for the red data set
rk = red.keys();
red1 = red.rename(columns = {rk[i]:newkeys[i] for i in range(len(rk))})
red1['Color'] = 'Red';

#Finally, we concatenate the two dataframes
dfn = pd.concat([blue1,red1],  ignore_index=True)
dfn = dfn.rename(columns = {"Wins":"Victory"})
dfn


# In[56]:


fig = px.scatter_matrix(dfn,
    dimensions=dfn.keys()[1:20:3],
    color="Victory")
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




