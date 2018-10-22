
# coding: utf-8

# In[95]:


import pandas as pd
import seaborn as sns
import pandas as pd
import numpy as np
from plotnine import *
import folium


# In[103]:


sidata = pd.read_csv("https://raw.githubusercontent.com/nschettini/CUNY-MSDS-DATA-607/master/NYPD_Motor_Vehicle_Collisions%202017.csv")


# In[104]:


sidata.head()


# In[105]:


sidata.drop(columns=['OFF STREET NAME', 'UNIQUE KEY'])


# In[108]:


(ggplot(sidata, aes('CONTRIBUTING FACTOR VEHICLE 1')) + 
 geom_bar(aes(fill= 'VEHICLE TYPE CODE 1'), show_legend=False) + 
 coord_flip() + 
 theme_xkcd() + 
 xlab("Contributing Factor") )


# In[77]:


from folium.plugins import HeatMap


# In[99]:


maps = folium.Map(location=[40.579021, -74.151535])

sidata1 = sidata

sidata1 = sidata1.dropna()

sidata1['LATITUDE'] = sidata1['LATITUDE'].astype(float)
sidata1['LONGITUDE'] = sidata1['LONGITUDE'].astype(float)

heat_data = [[column['LATITUDE'],column['LONGITUDE']] for index, column in sidata1.iterrows()]

HeatMap(heat_data).add_to(maps)

maps

