# Cafe menu
result = []

#Variable for menu List items available on
menu = ['croissant', 'cake','bagel', 'scone', 'tea', 'coffee', 'water','soda', 'juice']

#Variable stock and price dictionaries containing items and prices
stock = {"croissant": 2.40,
         "cake": 4.00
         "bagel": 1.00,
         "scone": 0.90,
         "tea": 0.50,
         "coffee": 3.10
         "water": 1.00
         "soda": 2.00,
         "juice": 1.50}

price = {"croissant": 2.40,
         "cake": 4.00
         "bagel": 1.00,
         "scone": 0.90,
         "tea": 0.50,
         "coffee": 3.10,
         "water": 1.00
         "soda": 2.00,
         "juice": 1.50}


#Empty variable to store total
total = 0

#For loop to run through items
for i in menu:
        total += (stock[i] * price[i])
print(total)