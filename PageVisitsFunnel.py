import codecademylib3	
import pandas as pd	
	
visits = pd.read_csv('visits.csv',	
                     parse_dates=[1])	
cart = pd.read_csv('cart.csv',	
                   parse_dates=[1])	
checkout = pd.read_csv('checkout.csv',	
                       parse_dates=[1])	
purchase = pd.read_csv('purchase.csv',	
                       parse_dates=[1])	
	
	
print(visits.head())	
print(cart.head())	
print(checkout.head())	
print(purchase.head())	
	
visit_cart = pd.merge(visits,cart, how = "left")	
print(visit_cart)	
	
x_visit_cart = visit_cart.user_id.count()	
print(x_visit_cart)	
	
visit_cart["null"] = visit_cart.cart_time.isnull()	
print(visit_cart)	
	
count_null = visit_cart.groupby("null").user_id.count()	
print(count_null)	
	
cart_checkout = pd.merge(cart,checkout, how = "left")	
print(cart_checkout)	
	
cart_checkout["null"] = cart_checkout.checkout_time.isnull()	
print(cart_checkout)	
	
count_null_checkout = cart_checkout.groupby("null").user_id.count()	
print(count_null_checkout)	
	
	
all_data = visits.merge(cart,how = "left").merge(checkout, how = "left").merge(purchase, how = "left")	
print(all_data.head())	
	
all_data["average"] = all_data.purchase_time - all_data.visit_time	
print(all_data)	
	
print(all_data.average)	
	
print(all_data.average.mean())	
