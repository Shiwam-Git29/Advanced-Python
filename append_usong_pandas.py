import pandas as pd   
# Create a DataFrame of E-commerce data 
pd =pd.DataFrame({
    'Order ID': [6, 7, 8, 9, 10],
    'Customer Name': ['Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
    'Product': ['Monitor', 'Keyboard', 'Mouse', 'Printer', 'Scanner'],
    'Quantity': [2, 1, 3, 1, 2],
    'Price': [200, 50, 25, 150, 100],
    'customer city': ['Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'] 
})

print(pd)
pd.to_csv('ecommerce_data.csv', mode='a', index=False, header=False)