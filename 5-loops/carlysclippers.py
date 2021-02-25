# Cindy's Clippers
# A Codecademy Project from Learn Python
# mattRicotta

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# calculate average haircut price
total_price = 0
for price in prices:
  total_price += price
average_price = total_price/len(prices)
print("Average Haircut Price: ", average_price)

# reduce haircut prices by 5
new_prices = []
for price in prices:
  new_prices.append(price - 5)
print("New Prices: ", new_prices)

# calculate revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: ", total_revenue)
average_daily_revenue = total_revenue/7
print("Average Daily Revenue: ", average_daily_revenue)

# create list of cuts under 30 using new prices
cuts_under_30 = []
for i in range(len(hairstyles)):
  if new_prices[i] >= 30:
    continue
  cuts_under_30.append(hairstyles[i])
print("Cuts Under 30: ", cuts_under_30)