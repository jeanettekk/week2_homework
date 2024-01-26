from math import pi, tan, cos
# Imported pi (math constant), tan (function), and cos (function) from the math module
# Math module provides functions for calculations

g = 9.81
# The variable 'g' stores the acceleration due to gravity, a float
v0 = 44
# The variable 'v0' stores the initial velocity of the projectile in meters per second, an integer
elev_deg = 80
# The variable 'elev_deg' stores the elevation angle of the projectile in degrees
theta = elev_deg * pi / 180
# The variable 'theta' stores the elevation angle converted to radians
# Used the multiplication * and division / operators

x = 0.5
# The variable 'x' stores the horizontal distance travelled by the projectile
y0 = 1
# The variable 'y0' stores the height of the barrel from which the projectile is launched in meters

a = g * x**2
# Used **2 to square a numeric value
b = 2 * (v0 * cos(theta))**2
# The cos() function returns the cosine of the angle 'theta'
c = x * tan(theta)
# The tan() function returns the tangent of the angle 'theta'
# The a, b and c variables store immediate results for simplifying the final calculation


proj_height = y0 + c - (a / b)
# The variable 'proj_height' stores the calculated height of the projectile

print('The height of the projectile is', round(proj_height, 2), 'meters.')
# Outputs a string and the rounded float value of 'proj_height'
# The function round() rounds a number to a specified number of decimal places
# Rounds 'proj_height' to two decimal places