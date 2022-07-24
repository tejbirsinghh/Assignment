# Example 9

class Vehicle:
 	def __del__(self):
 	    print("Vehicle object destroyed")
 	    print(10/0)
v = Vehicle()
del v
# Output
# Vehicle object destroyed
# Exception ignored in: <function Vehicle.__del__ at 0x000001B0E716ED40>
# Traceback (most recent call last):
# File "d:\vs codd\training\assignment\assignment no.4\4 (9).py", line 6, in __del__
# print(10/0)
# ZeroDivisionError: division by zero