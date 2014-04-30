meal = float(raw_input("What is the base cost of your meal? "))
tax = float(raw_input("What is the tax rate (as a decimal) on your meal? "))
tip = float(raw_input("What percentage (as a decimal) would you like to leav\
e for tip? "))

tax_value = meal * tax
meal_with_tax = meal + meal * tax
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "The base cost of your meal is ${0:.2f}.".format(meal)
print "The tax on your meal is ${0:.2f}.".format(tax)
print "The tip you should leave is ${0:.2f}.".format(tip_value)

print "The total cost of your meal is ${0:.2f}.".format(total)