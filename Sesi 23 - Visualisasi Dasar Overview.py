#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = {'tahun': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'penjualan': [10, 12, 15, 20, 18, 25, 30, 35, 40, 45, 50]}
df = pd.DataFrame(data)
df.head()


# In[2]:


import matplotlib.pyplot as plt
plt.plot(df['tahun'], df['penjualan'])
plt.xlabel('Tahun')
plt.ylabel('Penjualan')
plt.title('Grafik Penjualan Per Tahun')
plt.show()


# In[3]:


import pandas as pd

data = {'negara': ['Indonesia', 'India', 'Cina', 'Amerika Serikat', 'Brasil'],
'populasi': [267700000, 1366000000, 1393000000, 328200000, 211800000]}
df = pd.DataFrame(data)


# In[4]:


import matplotlib.pyplot as plt

plt.bar(df['negara'], df['populasi'])
plt.xlabel('Negara')
plt.ylabel('Populasi (dalam juta)')
plt.title('Grafik Populasi Lima Negara Terbesar di Dunia')
plt.show()


# In[5]:


import pandas as pd
data = {'tahun': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'penjualan': [10, 12, 15, 20, 18, 25, 30, 35, 40, 45, 50]}
df = pd.DataFrame(data)
df.head()


# In[6]:


import matplotlib.pyplot as plt
plt.fill_between(df['tahun'], df['penjualan'], color='skyblue')
plt.plot(df['tahun'], df['penjualan'], color='blue')
plt.xlabel('Tahun')
plt.ylabel('Penjualan')
plt.title('Grafik Penjualan Per Tahun')
plt.show()


# In[7]:


import pandas as pd
data = {'kategori': ['A', 'B', 'C', 'D', 'E'],
        'nilai': [20, 10, 15, 5, 25]}
df = pd.DataFrame(data)
df.head()


# In[8]:


import matplotlib.pyplot as plt
plt.pie(df['nilai'], labels=df['kategori'], autopct='%1.1f%%')
plt.title('Grafik Persentase Kategori')
plt.show()


# In[9]:


import pandas as pd
data = {'nilai': [55, 60, 70, 75, 80, 82, 85, 90, 95, 100]}
df = pd.DataFrame(data)
df.head()


# In[10]:


import matplotlib.pyplot as plt
plt.hist(df['nilai'], bins=5)
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.title('Grafik Distribusi Nilai')
plt.show()


# In[11]:


import pandas as pd
data = {'jenis': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D', 'D'],
        'nilai': [20, 25, 10, 15, 5, 7, 10, 30, 35, 40, 45]}
df = pd.DataFrame(data)
df.head()


# In[12]:


import matplotlib.pyplot as plt
plt.boxplot([df[df['jenis'] == 'A']['nilai'], 
             df[df['jenis'] == 'B']['nilai'], 
             df[df['jenis'] == 'C']['nilai'], 
             df[df['jenis'] == 'D']['nilai']])
plt.xticks([1, 2, 3, 4], ['A', 'B', 'C', 'D'])
plt.xlabel('Jenis')
plt.ylabel('Nilai')
plt.title('Grafik Distribusi Nilai Berdasarkan Jenis')
plt.show()


# In[13]:


import pandas as pd
data = {'x': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'y': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]}
df = pd.DataFrame(data)
df.head()


# In[14]:


import matplotlib.pyplot as plt
plt.scatter(df['x'], df['y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grafik Scatter Plot')
plt.show()


# # Visualisasi Dasar 2

# In[35]:


import numpy as np
import pandas as pd


# In[36]:


import xlrd


# In[38]:


from pandas import ExcelWriter
from pandas import ExcelFile


# In[40]:


df_can = pd.read_excel('https://github.com/ardhiraka/PFDS_sources/blob/master/Canada.xlsx?raw=true',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')


# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt


# In[28]:


print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0


# In[29]:


print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style


# In[42]:


df_can.head()


# In[43]:


df_can.info()


# In[44]:


df_can.shape  


# In[45]:


df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)


# In[46]:


df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)
df_can.columns


# In[55]:


df_can['Total'] = df_can.loc[:, 1980:2013].sum(axis=1)


# In[56]:


df_can


# In[57]:


df_can.isnull().sum()


# In[58]:


df_can.describe()


# In[59]:


df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]


# In[62]:


df_can.set_index('Country', inplace=True)


# In[63]:


df_can.head(3)


# In[64]:


print(df_can.loc['Japan'])


# In[65]:


print(df_can.loc['Japan', 2013])


# In[66]:


print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1985]])


# In[67]:


df_can.columns = list(map(str, df_can.columns))


# In[68]:


years = list(map(str, range(1980, 2014)))
years


# In[69]:


condition = df_can['Continent'] == 'Asia'
print (condition)


# In[70]:


df_can[condition]


# In[71]:


df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]


# In[72]:


print ('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)


# In[73]:


haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()


# In[74]:


haiti.plot()


# In[75]:


haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() # need this line to show the updates made to the figure


# In[76]:


haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below

plt.show() 


# In[77]:


China_India = df_can.loc[['China', 'India'], years]
China_India


# In[78]:


df_CI = China_India.transpose()
df_CI.head()


# In[79]:


df_CI.plot(kind='line')
plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()


# In[80]:


df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

df_top5 = df_can.head(5)

df_top5 = df_top5[years].transpose() 

df_top5.index = df_top5.index.map(int)

df_top5.plot(kind='line', figsize=(14, 8))

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# In[81]:


df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head()

# transpose the dataframe
df_top5 = df_top5[years].transpose() 

df_top5.head()


# In[82]:


df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting

df_top5.plot(kind='area', 
             stacked=False,
             figsize=(20, 10), # pass a tuple (x, y) size
             )

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# In[83]:


df_top5.plot(kind='area', 
             alpha=0.25, # 0-1, default value a= 0.5
             stacked=False,
             figsize=(20, 10),
            )

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# In[85]:


df_top5.plot(kind='area', alpha=0.35, figsize=(20, 10)) 
plt.title('Immigration trend of top 5 countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')


# In[86]:


ax = df_top5.plot(kind='area', alpha=0.35, figsize=(20, 10))

ax.set_title('Immigration Trend of Top 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')


# In[87]:


df_least5 = df_can.tail(5)
df_least5 = df_least5[years].transpose() 

df_least5.plot(kind='area', 
             alpha=0.45, # 0-1, default value a= 0.5
             stacked=True,
             figsize=(20, 10),
            )

plt.title('Immigration Trend of Leat 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# In[88]:


ax = df_least5.plot(kind='area', alpha=0.35, figsize=(20, 10))

ax.set_title('Immigration Trend of Least 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')


# In[89]:


df_can['2013'].head()


# In[90]:


count, bin_edges = np.histogram(df_can['2013'])

print(count) # frequency count
print(bin_edges) # bin ranges, default = 10 bins


# In[91]:


df_can['2013'].plot(kind='hist', figsize=(8, 5))

plt.title('Histogram of Immigration from 195 Countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label

plt.show()


# In[92]:


# 'bin_edges' is a list of bin intervals
count, bin_edges = np.histogram(df_can['2013'])

df_can['2013'].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)

plt.title('Histogram of Immigration from 195 countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label

plt.show()


# In[93]:


df_can.loc[['Denmark', 'Norway', 'Sweden'], years]


# In[94]:


df_can.loc[['Denmark', 'Norway', 'Sweden'], years].plot.hist()


# In[95]:


df_t = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
df_t.head()


# In[96]:


df_t.plot(kind='hist', figsize=(10, 6))

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()


# In[97]:


count, bin_edges = np.histogram(df_t, 15)

# un-stacked histogram
df_t.plot(kind ='hist', 
          figsize=(10, 6),
          bins=15,
          alpha=0.6,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen']
         )

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()


# In[99]:


import matplotlib
for name, hex in matplotlib.colors.cnames.items():
    print(name, hex)
    
count, bin_edges = np.histogram(df_t, 15)
xmin = bin_edges[0] - 10   #  first bin value is 31.0, adding buffer of 10 for aesthetic purposes 
xmax = bin_edges[-1] + 10  #  last bin value is 308.0, adding buffer of 10 for aesthetic purposes



# In[100]:


# stacked Histogram
df_t.plot(kind='hist',
          figsize=(10, 6), 
          bins=15,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen'],
          stacked=True,
          xlim=(xmin, xmax)
         )

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants') 

plt.show()


# In[101]:


### type your answer here
df_cof = df_can.loc[['Greece', 'Albania', 'Bulgaria'], years]
df_cof = df_cof.transpose() 

count, bin_edges = np.histogram(df_cof, 15)
df_cof.plot(kind ='hist',
            figsize=(10, 6),
            bins=15,
            alpha=0.35,
            xticks=bin_edges,
            color=['coral', 'darkslateblue', 'mediumseagreen']
            )

plt.title('Histogram of Immigration from Greece, Albania, and Bulgaria from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
plt.show()


# In[102]:


df_iceland = df_can.loc['Iceland', years]
df_iceland.head()


# In[103]:


df_iceland.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Year') # add to x-label to the plot
plt.ylabel('Number of immigrants') # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot

plt.show()


# In[104]:


df_iceland.plot(kind='bar', figsize=(10, 6), rot=90) 

plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')

# Annotate arrow
plt.annotate('',                      # s: str. will leave it blank for no text
             xy=(32, 70),             # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),         # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',         # will use the coordinate system of the object being annotated 
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
            )

# Annotate Text
plt.annotate('2008 - 2011 Financial Crisis', # text to display
             xy=(28, 30),                    # start the text at at point (year 2008 , pop 30)
             rotation=72.5,                  # based on trial and error to match the arrow
             va='bottom',                    # want the text to be vertically 'bottom' aligned
             ha='left',                      # want the text to be horizontally 'left' algned.
            )

plt.show()


# In[105]:


df_can.sort_values(by='Total', ascending=True, inplace=True)
df_top15 = df_can['Total'].tail(15)
df_top15


# In[106]:


df_top15.plot(kind='barh', figsize=(12, 12), color='steelblue')
plt.xlabel('Number of Immigrants')
plt.title('Top 15 Conuntries Contributing to the Immigration to Canada between 1980 - 2013')
# for index, value in enumerate(df_top15): 
#     label = format(int(value), ',') # format int with commas
#     # place text at the end of bar (subtracting 47000 from x, and 0.1 from y to make it fit within the bar)
#     plt.annotate(label, xy=(value - 47000, index - 0.10), color='white')
plt.show()


# In[107]:


df_continents = df_can.groupby('Continent', axis=0).sum()

# note: the output of the groupby method is a `groupby' object. 
# we can not use it further until we apply a function (eg .sum())
print(type(df_can.groupby('Continent', axis=0)))

df_continents.head()


# In[108]:


# autopct create %, start angle represent starting point
df_continents['Total'].plot(kind='pie',
                            figsize=(5, 6),
                            autopct='%1.1f%%', # add in percentages
                            startangle=90,     # start angle 90° (Africa)
                            shadow=True,       # add shadow      
                            )

plt.title('Immigration to Canada by Continent [1980 - 2013]')
plt.axis('equal') # Sets the pie chart to look like a circle.

plt.show()


# In[109]:


colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.

df_continents['Total'].plot(kind='pie',
                            figsize=(15, 6),
                            autopct='%1.1f%%', 
                            startangle=90,    
                            shadow=True,       
                            labels=None,         # turn off labels on pie chart
                            pctdistance=1.12,    # the ratio between the center of each pie slice and the start of the text generated by autopct 
                            colors=colors_list,  # add custom colors
                            explode=explode_list # 'explode' lowest 3 continents
                            )

# scale the title up by 12% to match pctdistance
plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12) 

plt.axis('equal') 

# add legend
plt.legend(labels=df_continents.index, loc='upper left') 

plt.show()


# In[110]:


colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.05, 0.15] # ratio for each continent with which to offset each wedge.

df_continents['2013'].plot(kind='pie',
                            figsize=(15, 6),
                            autopct='%1.1f%%', 
                            startangle=90,    
                            shadow=True,       
                            labels=None,         # turn off labels on pie chart
                            pctdistance=1.12,    # the ratio between the center of each pie slice and the start of the text generated by autopct 
                            colors=colors_list,  # add custom colors
                            explode=explode_list # 'explode' lowest 3 continents
                            )

# scale the title up by 12% to match pctdistance
plt.title('Immigration to Canada by Continent Year 2013', y=1.12) 

plt.axis('equal') 

# add legend
plt.legend(labels=df_continents.index, loc='upper left') 

plt.show()


# In[111]:


df_japan = df_can.loc[['Japan'], years].transpose()
df_japan.head()


# In[112]:


df_japan.plot(kind='box', figsize=(8, 6))

plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')

plt.show()


# In[113]:


df_japan.describe()


# In[114]:


df_CI = df_can.loc[(['China', 'India']), years].transpose()
df_CI.head()


# In[115]:


df_CI.plot(kind='box', figsize=(8, 6))

plt.title('Box plot of China and India Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')

plt.show()


# In[116]:


df_CI.plot(kind='box', figsize=(10, 7), color='blue', vert=False)

plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.xlabel('Number of Immigrants')

plt.show()


# In[119]:


fig = plt.figure() # create figure

ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(1, 2, 2) # add subplot 2 (1 row, 2 columns, second plot). See tip below**

# Subplot 1: Box plot
df_CI.plot(kind='box', color='blue', vert=False, figsize=(20, 6), ax=ax0) # add to subplot 1
ax0.set_title('Box Plots of Immigrants from China and India (1980 - 2013)')
ax0.set_xlabel('Number of Immigrants')
ax0.set_ylabel('Countries')

# Subplot 2: Line plot
df_CI.plot(kind='line', figsize=(20, 6), ax=ax1) # add to subplot 2
ax1.set_title ('Line Plots of Immigrants from China and India (1980 - 2013)')
ax1.set_ylabel('Number of Immigrants')
ax1.set_xlabel('Years')

plt.show()


# In[120]:


df_top15 = df_can.sort_values(['Total'], ascending=False, axis=0).head(15)
df_top15


# In[121]:


years_80s = list(map(str, range(1980, 1990))) 
years_90s = list(map(str, range(1990, 2000))) 
years_00s = list(map(str, range(2000, 2010))) 

df_80s = df_top15.loc[:, years_80s].sum(axis=1) 
df_90s = df_top15.loc[:, years_90s].sum(axis=1) 
df_00s = df_top15.loc[:, years_00s].sum(axis=1)

new_df = pd.DataFrame({'1980s': df_80s, '1990s': df_90s, '2000s':df_00s}) 
new_df.head()


# In[122]:


new_df.describe()


# In[123]:


new_df.plot(kind='box', figsize=(10, 6))
plt.title('Immigration from top 15 countries for decades 80s, 90s and 2000s')
plt.show()


# In[124]:


new_df[new_df['2000s']> 209611.5]


# In[125]:


df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# change the years to type int (useful for regression later on)
df_tot.index = map(int, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace = True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
df_tot.head()


# In[126]:


df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

plt.show()


# In[127]:


df_countries = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
df_total = pd.DataFrame(df_countries.sum(axis=1))
df_total.reset_index(inplace=True)
df_total.columns = ['year', 'total']
df_total['year'] = df_total['year'].astype(int)
df_total.head()


# In[128]:


df_total.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')
plt.title('Immigration from Denmark, Norway, and Sweden to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.show()


# In[129]:


df_can_t = df_can[years].transpose() # transposed dataframe

# cast the Years (the index) to type int
df_can_t.index = map(int, df_can_t.index)

# let's label the index. This will automatically be the column name when we reset the index
df_can_t.index.name = 'Year'

# reset index to bring the Year in as a column
df_can_t.reset_index(inplace=True)

# view the changes
df_can_t.head()


# In[130]:


norm_brazil = (df_can_t['Brazil'] - df_can_t['Brazil'].min()) / (df_can_t['Brazil'].max() - df_can_t['Brazil'].min())

# normalize Argentina data
norm_argentina = (df_can_t['Argentina'] - df_can_t['Argentina'].min()) / (df_can_t['Argentina'].max() - df_can_t['Argentina'].min())


# In[131]:


# Brazil
ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Brazil',
                    figsize=(14, 8),
                    alpha=0.5,                  # transparency
                    color='green',
                    s=norm_brazil * 2000 + 10,  # pass in weights 
                    xlim=(1975, 2015)
                   )

# Argentina
ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Argentina',
                    alpha=0.5,
                    color="blue",
                    s=norm_argentina * 2000 + 10,
                    ax = ax0
                   )

ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from Brazil and Argentina from 1980 - 2013')
ax0.legend(['Brazil', 'Argentina'], loc='upper left', fontsize='x-large')


# In[132]:


### type your answer here
norm_china = (df_can_t['China'] - df_can_t['China'].min()) / (df_can_t['China'].max() - df_can_t['China'].min())
norm_india = (df_can_t['India'] - df_can_t['India'].min()) / (df_can_t['India'].max() - df_can_t['India'].min())


# In[133]:


ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='China',
                    figsize=(14, 8),
                    alpha=0.5,                  # transparency
                    color='green',
                    s=norm_china * 1300 + 10,  # pass in weights 
                    xlim=(1975, 2015)
                   )

ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='India',
                    alpha=0.5,
                    color="blue",
                    s=norm_india * 1300 + 10,
                    ax = ax0
                   )

ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from China and India from 1980 - 2013')
ax0.legend(['China', 'India'], loc='upper left', fontsize='x-large')


# In[ ]:





# In[ ]:




