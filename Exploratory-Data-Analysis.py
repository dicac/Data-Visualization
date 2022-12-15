url = https://www.kaggle.com/datasets/neuromusic/avocado-prices
avodata =  pd.read_csv('.../url_avocado.csv')

## Loading Packages
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# Data Wrangling
avodata= avodata.rename(index=str, 
                        columns={"Unnamed: 0": "Week", "4046" : "Small Hass", "4225" : "Large Hass","4770" : "XLarge Hass" })
                       
avodata.Date = pd.to_datetime(avodata.Date)
avodata.sort_values(by=['Date'], inplace=True, ascending=True)
avodata = avodata.reset_index(drop=True)

# Density Plot: Average Price By Type
custom_params = {"axes.spines.right": False, "axes.spines.top": False}

plt.figure(figsize=(8,4))
sns.set_theme(style="white", rc=custom_params)
sns.color_palette("hls", 8)
sns.kdeplot(data=avodata, x = 'AveragePrice', hue='type', fill=True, 
            common_norm=False, alpha=0.3, palette="crest")
plt.title('Average Price By Type')
plt.show()

# Line Chart: Average Price Evolution
plt.figure(figsize=(12,4))
sns.lineplot(x = 'Date', y = 'AveragePrice', hue="type", data=avodata, palette="crest")
plt.ticklabel_format(style='plain', axis='y')
plt.legend(loc='upper center', bbox_to_anchor=(1.1, 0.8), shadow=True, ncol=1)
plt.title('Average Price Evolution')
plt.show()

# Line Chart: Number of Avocados Sold
plt.figure(figsize=(11,4))
sns.set_theme(style="white", rc=custom_params, palette="vlag")
sns.lineplot(x = 'Date', y = 'Total Volume', data=avodata)
plt.ticklabel_format(style='plain', axis='y')
plt.xticks(rotation=45)
plt.title('Total number of Avocados Sold')
plt.show()

# Pie Chart: Sales Volume by Region(Major Regions)
filter1=avodata.region!='TotalUS'
avo=avodata[filter1]
avo_pie = avo.groupby('region')['Total Volume'].sum().sort_values(ascending = False).reset_index()

avo_pie['Eng_percent'] = (avo_bar['Total Volume'] / 
                          avo_bar['Total Volume'].sum()) * 100
avo_pie.reset_index()   
 
## Group up regions with sales volume less than 2% on 'remaining'
threshold = 2
remaining = avo_pie.loc[avo_pie['Eng_percent'] < threshold].sum(axis = 0)
remaining.loc['index'] = 'remaining'
avo_pie = avo_pie[avo_pie ['Eng_percent'] >= threshold]
avo_pie = avo_pie.append(remaining, ignore_index = True)
 
colors = ['#0038E2','#0055D4','#0071C6','#008DB8','#00AAAA','#00C69C','#00E28E','#001CF0','#00FF80','#191970',]
explode = (0.01, 0.01, 0.01, 0.03, 0.1, 0.1, 0.1, 0.2, 0.2, 0.3, 0.4, 0.5, 0.6, 0.01)

plt.figure(figsize=(20,10))
plt.pie(x = avo_bar['Total Volume'], labels= avo_bar.region, colors=colors, explode=explode,
        shadow = False, startangle = 90 , autopct = '%1.1f%%', textprops={'fontsize':15})
plt.title("Sales Volume by Region", fontsize = 23, loc="left")
plt.axis('equal')
plt.tight_layout()
plt.show()

# Stackplot: Total Monthly Annual Volume
avodata['month'] = avodata['Date'].dt.month 
avodata['month'] = avodata['month'].apply(lambda x: calendar.month_abbr[x])

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

## Create a new column months(1-12) and format Jan, Feb, Mar

a = avodata.groupby(["year", "month"]).sum("Total Volume").reset_index()

df_2015 = a.loc[0:11, ['month', 'year', 'Total Volume']]
df_2016 = a.loc[12:23, ['month', 'year', 'Total Volume']]
df_2017 = a.loc[24:35, ['month', 'year', 'Total Volume']]

df_2015['month'] = pd.Categorical(df_2015['month'], categories=month, ordered=True)
df_2015.sort_values(by='month',inplace=True)

custom_params = {"axes.spines.right": False, "axes.spines.top": False
                 plt.figure(figsize=(12,4))
sns.set_theme(style="white",  rc=custom_params, palette="Paired")
plt.stackplot(df_2015.month, df_2015['Total Volume'], df_2016['Total Volume'], df_2017['Total Volume'], 
              labels=['2015', '2016', '2017'])
plt.legend(loc='upper center', bbox_to_anchor=(1.1, 0.7))
plt.ticklabel_format(style='plain', axis='y') #Controlling Scientific notation
plt.title('Total Monthly Annual Volume')
plt.show()
                 
# PRICE BY REGION
                 
                 

# Lineplot : Average Monthly Price
plt.figure(figsize=(10,4))
sns.set_theme(style="white", rc=custom_params, palette="cubehelix")
ax = sns.lineplot(data=avodata, x='month', y='AveragePrice', hue='type',
     marker='o', markersize=9)
plt.title('Average Monthly Price ')
ax.grid(color='grey', linestyle='-', linewidth=0.15, alpha=0.9)
plt.show()
                 
# Catplot: Price Variation         
plt.figure(figsize=(10,4))
sns.set_theme(style="white",  rc=custom_params, palette="cubehelix")
ax = sns.lineplot(data=avodata, x='month', y='AveragePrice', hue='type',
    marker='o', markersize=9)#,  color='skyblue')
plt.title('Average Monthly Price ')
ax.grid(color='grey', linestyle='-', linewidth=0.15, alpha=0.9)
plt.show()                

