# message = "\nHello World!\n"
# print(message)

# import numpy as np

# # Define two numbers
# number1 = 5
# number2 = 10

# # Sum the two numbers using numpy
# result = np.sum([number1, number2])

# # Print the result
# print("The sum of {} and {} is: {}".format(number1, number2, result))

import os

vehicle_name = os.environ['VEHICLE_NAME']
message = f"\nHello from {vehicle_name}!\n"
print(message)