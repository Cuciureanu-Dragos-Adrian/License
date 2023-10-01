import math
from utilities.utility_addition_f import *
from utilities.utility_multiplication_f import *

#baby step giant step algorithm to determine the order of point
def order_point_baby_step_giant_step(a, prime, p):
    m = int(math.sqrt(math.sqrt(prime))) + 1
    order = 0
    real_order = 0
    steps = 0
    found_order = False

    #baby steps
    for j in range(0, m + 1):
        jp = multiply_points_f_double_and_add(a, p, j, prime)[0][1]

        #giant steps
        for k in range(-m, m + 1):
            multiplier = k*2*m + prime + 1
            check = multiply_points_f_double_and_add(a, p, multiplier, prime)[0][1]

            #collision found
            if check[0] == jp[0]:
                order = prime + 1 + k*2*m

                #determine multiple of order
                if multiply_points_f_double_and_add(a, p, order - j, prime)[0][1] == ('inf', 'inf'):
                    order -= j
                    steps = (j - 1) * (2*m + 1) + (m + 1 + k)
                    found_order = True
                    break

                #determine multiple of order
                elif multiply_points_f_double_and_add(a, p, order + j, prime)[0][1] == ('inf', 'inf'):
                    order += j
                    found_order = True
                    steps = (j - 1) * (2*m + 1) + (m + 1 + k)
                    break

        if found_order == True:
            break

    #determine real order
    for i in get_divisors(order):
        if multiply_points_f_double_and_add(a, p, i, prime)[0][1] == ('inf', 'inf'):
            real_order = i
            break

    return (real_order, order, steps)


#function that returns the divisors based on the number's factors
def get_divisors(n):
    divisors = [1]
    cn = n
    i = 2

    while i * i <= n:
        if n % i == 0:
            count = 0

            while n % i == 0:
                n = n // i
                count += 1

            factors = []

            for j in range(1, count + 1):
                factors.append(i ** j)
                
            divs = []
            for d in divisors:
                for f in factors:
                    divs.append(f * d)

            divisors.extend(divs)
            
        i += 1
        
    divs = []
    if n != 1:
        for d in divisors:
            divs.append(n * d)

        divisors.extend(divs)

    divisors.sort()
    return divisors