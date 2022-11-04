url = https://www.kaggle.com/datasets/neuromusic/avocado-prices
avodata =  pd.read_csv('.../url_avocado.csv')

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
sns.kdeplot(data=avodata, x = 'AveragePrice', hue='type', fill=True, common_norm=False, 
            alpha=0.3, palette="crest")
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
 
 ## Pie Chart
colors = ['#0038E2','#0055D4','#0071C6','#008DB8','#00AAAA','#00C69C','#00E28E','#001CF0','#00FF80','#191970',]
explode = (0.01, 0.01, 0.01, 0.03, 0.1, 0.1, 0.1, 0.2, 0.2, 0.3, 0.4, 0.5, 0.6, 0.01)

plt.figure(figsize=(20,10))
plt.pie(x = avo_bar['Total Volume'], labels= avo_bar.region, colors=colors, explode=explode,
        shadow = False, startangle = 90 , autopct = '%1.1f%%', textprops={'fontsize':15})
plt.title("Sales Volume by Region", fontsize = 23, loc="left")
plt.axis('equal')
plt.tight_layout()
plt.show()

