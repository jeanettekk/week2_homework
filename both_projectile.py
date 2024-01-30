# week 2 homework Exercise 9 part 3
# This program does some complex math to calculate height of a projectile fired from a gun

# Math module provides calculations like tan and cos of theta
import math

# Assigning given barrel height to variable
yb = 1

# Assigning given horizontal_distance to variable
x = 0.5

#  Assigning given elevation in degree to variable
deg = 80

# Calculating elevation in radian by converting degree into radian
theta = deg * 22 / (7 * 180)

# The variable 'g' stores the acceleration due to gravity, a float
g = 9.81

# Assigning value of initial velocity to variable vi
vi = 44

# Printing formula for the height of projectile
print("\n Formula version1: Height of Projectile, yp = "
      "yb + (x * tan(theta)) - ((g * x * x)/(2 * (vi * cos(theta)) * (vi * cos(theta))))")

# Calculating height of projectile using given formula and values
yp = yb + (x * math.tan(theta)) - ((g * x * x)/(2 * (vi * math.cos(theta)) * (vi * math.cos(theta))))

# Printing the result after converting into string to join with left hand side string
print("\n Therefore, height of projectile, yp = " + str(yp) + ' units')


# Another approach to find out the height of projectile

# Used **2 to square a numeric value
a = g * x**2

# The cos() function returns the cosine of the angle 'theta'
b = 2 * (vi * math.cos(theta))**2

# The tan() function returns the tangent of the angle 'theta'
# The a, b and c variables store immediate results for simplifying the final calculation
c = x * math.tan(theta)

# The variable 'proj_height' stores the calculated height of the projectile
proj_height = yb + c - (a / b)
print('\nFormula version2: proj_height = yb + c - (a / b)')

# Outputs a string and the rounded float value of 'proj_height'
# The function round() rounds a number to a specified number of decimal places
# Rounds 'proj_height' to two decimal places
print('\nThe height of the projectile is', round(proj_height, 2), 'meters.')
