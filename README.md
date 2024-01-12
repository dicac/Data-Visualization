# Data Analysis: Avocado Price

Avodata represents weekly national (US) retail avocado sales data from 2015 to I-2018. The average price in the table reflects a cost per unit even when multiple units (avocados) are sold in bags. PLUs correspond to Product Lookup codes and comes from the retailer's register for Hass avocados only.

#### Variables

	“Date”
	“AveragePrice”, average price of a single avocado.
	“Total Volume”, total number of avocados sold. 
	“4046”, total number of avocados with PLU 4046 (Small Hass).
	“4225”, total number of avocados with PLU 4225 (Large Hass).
	“4770”, total number of avocados with PLU 4770 (XLarge Hass).
	“Total Bags”, sum of the 3 bag sizes.
	“type”, conventional or organic.
	“region”, city or region of the observation.
  
 ### Dataset
| Date | AveragePrice | Total Volume | Small Hass | Large Hass | XLarge Hass | Total Bags | XLarge Bags |type | year | region|
|-------------| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 2015-12-27 | 1.33  | 64236.62  | 1036.74  | 54454.85 | 48.16 | 8696.87 | 8603.62 | 93.25 | 0.0 | conventional	| 2015	| Albany
| 2015-12-20 | 1.35  | 54876.98  | 674.28  | 44638.81 |58.33 | 9505.56 | 9408.07 | 97.49 | 0.0 | conventional | 2015	| Albany 

[**Check Notebook**](https://github.com/dicac/Data-Visualization/blob/80bb940c796b7a9edb917633bd3f490c046fe2be/Data%20Analysis%20Avocado%20Price.ipynb)

