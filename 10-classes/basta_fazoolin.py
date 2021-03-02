# Basta Fazoolin' project from Codecademy
# Learn Python: Classes
# mattRicotta

# Import time:
from datetime import datetime
# Test time function:
#print(datetime.strptime('4pm', '%I%p'))

# Define Menu Class:
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return self.name + " menu available from " + self.start_time + " to " + self.end_time
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total

# Define Franchise Class:
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    try:
      time_datetime = datetime.strptime(time, '%I%p')
    except:
      print("ERROR: Enter a time in the format of '3am' or '6pm'")
    available_menu_list = []
    for menu in self.menus:  
      menu_start = datetime.strptime(menu.start_time, '%I%p')
      menu_end = datetime.strptime(menu.end_time, '%I%p')
      if time_datetime >= menu_start and time_datetime <= menu_end:
        available_menu_list.append(menu)
    return available_menu_list

# Define Business Class:
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#------------- Basta Fazoolin' ---------------------------
# Define Basta Fazoolin' Menus:
brunch = Menu('Brunch', {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, '11am', '4pm')

early_bird = Menu('Early Bird',{'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00} ,'3pm', '6pm')

dinner = Menu('Dinner', {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, '5pm', '11pm')

kids = Menu('Kids', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, '11am', '9pm')

# Print Menus:
print("Basta Fazoolin':")
print(brunch)
print(early_bird)
print(dinner)
print(kids)

# Test calculate_bill():
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Create two franchises (Step 14):
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

# Print franchises
print("Flagship Store: ", flagship_store)
print("New Installment: ", new_installment)

# Test available_menus function:
time_requests = ['12pm', '5pm']
for time_requested in time_requests:
  print("Time Requested: ", time_requested)
  for menu in flagship_store.available_menus(time_requested):
    print(menu)

# Create Basta Fazoolin' Business:
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

print("")
#------------- Take a' Arepa ---------------------------

# Define Take a' Arepa menus:
arepas_menu = Menu("Take a' Arepas", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, '10am', '8pm')

# Create Take a' Arepa franchises:
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)

# Create Take a' Arepa business:
take_a_arepa = ("Take a' Arepa", [arepas_place])

print("Take a' Arepa")
print(arepas_place)
print(arepas_menu)

