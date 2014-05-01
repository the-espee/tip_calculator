from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--meal", dest="meal", help="base cost of the meal",\
				  type="float")
parser.add_option("-x", "--tax", dest="tax_percent", type="float")
parser.add_option("-t", "--tip", dest="tip_percent", help="tip % to leave",\
				  type="float", default=.20)

(options, args) = parser.parse_args()

if not (options.meal):
	parser.error("Please indicate the base cost of your meal!")
if not (options.tax_percent):
	parser.error("Please indicate the tax percentage of your location!")

tax_value = options.meal * options.tax_percent
meal_with_tax = options.meal + options.meal * options.tax_percent
tip_value = meal_with_tax * options.tip_percent
total = meal_with_tax + tip_value

print "The base cost of your meal is ${0:.2f}.".format(options.meal)
print "The tax on your meal is ${0:.2f}.".format(tax_value)
print "The tip you should leave is ${0:.2f}.".format(tip_value)

print "The total cost of your meal is ${0:.2f}.".format(total)