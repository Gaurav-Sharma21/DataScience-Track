import codecademylib3	
import pandas as pd	
import numpy as np	
	
ad_clicks = pd.read_csv('ad_clicks.csv')	
	
print(ad_clicks.head())	
	
x = ad_clicks.groupby("utm_source").user_id.count().reset_index()	
	
print(x)	
	
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()	
	
print(ad_clicks)	
	
clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()	
	
print(clicks_by_source)	
	
clicks_pivot = clicks_by_source.pivot(columns = "is_click", index = "utm_source", values = "user_id")	
print(clicks_pivot)	
	
clicks_pivot["percent_clicked"] = clicks_pivot[True]/(clicks_pivot[False] + clicks_pivot[True])	
	
print(clicks_pivot)	
	
x = ad_clicks.groupby(["experimental_group","is_click"]).user_id.count().reset_index()	
	
print(x)	
	
x_pivot = x.pivot(columns = "is_click", index = "experimental_group", values = "user_id")	
print(x_pivot)	
	
x_pivot["percentage"] = x_pivot[True] / (x_pivot[True] + x_pivot[False])	
	
print(x_pivot)	
	
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]	
print(a_clicks)	
	
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]	
print(b_clicks)	
	
a_s = a_clicks.groupby("day").user_id.count().reset_index()	
print(a_s)	
	
b_s = b_clicks.groupby("day").user_id.count().reset_index()	
print(b_s)	
	
total_clicks = pd.concat([a_s,b_s])	
print(total_clicks)	
	