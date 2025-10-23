# You just finished eating at a restaurant, and received this bill:
#Cost of meal: $44.50

"""
Restaurant tax: 6.75%

Tip: 15%

You’ll apply the tip to the overall cost of the meal (including tax). 
First, declare a variable called meal and assign it the value 44.50."""

meal = 44.50
tax = 6.75 / 100
tip = 15 / 100
meal = meal + (meal * tax)
meal = meal + (meal * tip)


print ("Your total meal cost is $", meal)