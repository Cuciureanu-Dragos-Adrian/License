import matplotlib.pyplot as plt
import numpy as np

#determines the y^2 based on the equation and the x
def result_equation_ec(a, b, prime, x):
	result = (x**3 + a * x + b) % prime

	return int(result)


#determines the y based on the x
def determine_y(prime, x):
	power = int((prime + 1) / 4)
	
	result = pow(int(x), power, prime)

	return (int(result), power)