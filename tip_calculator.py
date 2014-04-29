meal = 100.00
tax = .18
tip = .20
tax_value = meal * tax
meal_with_tax = meal + meal * tax
tip_value = meal_with_tax + tip

total = meal_with_tax + tip_value

print "The base cost of the meal is ${0:.2f}." .format(meal)
print "The tax on the meal is ${0:.2f}." .format(tax_value)
print "You need to pay ${0:.2f} as your tip." .format(tip_value)

print "The grand total of the meal is ${0:.2f}." .format(total)