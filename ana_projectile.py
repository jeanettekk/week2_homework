# week 2 homework part 3

# Importing math library
import math

# Assigning given barrel height to variable and printing it
yb = 1
print("\n barrel height, yb = 1m")

# Assigning given horizontal_distance to variable and printing it
x = 0.5
print("\n horizontal distance, x = 0.5m")

#  Assigning given elevation in degree to variable and printing it
deg = 80
print("\n elevation in degree = 80")

# Calculating elevation in radian and printing it by converting into string and concatenating to message
theta = deg * 22 / (7 * 180)
print("\n elevation in radian, theta = " + str(theta))

# Assigning to variable and printing acceleration due to gravity
g = 9.81
print("\n acceleration due to gravity, g = 9.81 m/s sq")

# Assigning to variable and printing initial velocity
vi = 44
print("\n initial velocity, vi = 44 m/s")

# Calculating tangent and cosine of theta using math methods and printing them
# by converting into string and concatenating to message
print("\n tan(theta) =" + str(math.tan(theta)))
print("\n cos(theta) =" + str(math.cos(theta)))

# Printing formula for the height of projectile
print("\n Formula: Height of Projectile, yp = "
      "yb + (x * tan(theta)) - ((g * x * x)/(2 * (vi * cos(theta)) * (vi * cos(theta))))")

# Calculating height of projectile using given formula and values
yp = yb + (x * math.tan(theta)) - ((g * x * x)/(2 * (vi * math.cos(theta)) * (vi * math.cos(theta))))

# Printing the result after converting into string to join with left hand side string
print("\n Therefore, height of projectile, yp = " + str(yp))
