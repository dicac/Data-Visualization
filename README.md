# Data Analysis: Avocado Price

Avodata represents weekly national (US) retail avocado sales data from 2015 to I-2018. The average price in the table reflects a cost per unit even when multiple units (avocados) are sold in bags. PLUs correspond to Product Lookup codes and comes from the retailer's register for Hass avocados only.

#### Features

	“Date”, weekly dates from 2015 to 2018.
	“AveragePrice”, average price of a single avocado.
	“Total Volume”, total number of avocados sold. 
	“4046”, total number of avocados with PLU 4046 (Small Hass).
	“4225”, total number of avocados with PLU 4225 (Large Hass).
	“4770”, total number of avocados with PLU 4770 (XLarge Hass).
    “Small Bags...”, total number of bags sold.
	“Total Bags”, sum of the 3 bag sizes.
	“type”, conventional or organic.
	“region”, city or region of the observation.
  
 ### Dataset
| Date | AveragePrice | Total Volume | Small Hass | Large Hass | XLarge Hass | Total Bags | Small Bags | Large Bags | XLarge Bags | type | year | region|
|-------------| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |------------- |
| 2015-01-04 | 1.75  | 27365.89  | 9307.34  | 3844.81 | 615.28 | 13598.46 | 13061.10 | 537.36 | 0.0 | organic| 2015	| Albany
| 2015-12-20 | 1.35  | 54876.98  | 674.28  | 44638.81 |58.33 | 9505.56 | 9408.07 | 97.49 | 0.0 | conventional | 2015	| Albany 

<p align="center">
  <img src=https://github.com/dicac/Data-Visualization/blob/main/Total%20volume%20by%20region.png> 
</p>

[**Check Notebook**](https://github.com/dicac/Data-Visualization/blob/80bb940c796b7a9edb917633bd3f490c046fe2be/Data%20Analysis%20Avocado%20Price.ipynb)

