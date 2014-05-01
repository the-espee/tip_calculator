import sys

meal = float(sys.argv[1])
tax = float(sys.argv[2])
tip = float(sys.argv[3])

tax_value = meal * tax
meal_with_tax = meal + meal * tax
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "The base cost of your meal is ${0:.2f}.".format(meal)
print "The tax on your meal is ${0:.2f}.".format(tax)
print "The tip you should leave is ${0:.2f}.".format(tip_value)

print "The total cost of your meal is ${0:.2f}.".format(total)