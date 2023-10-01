import math
from utilities.utility_addition_f import *
from utilities.utility_multiplication_f import *
from utilities.utility_order_point import *

#baby step giant step algorithm to determine the n for Q = nP
def meet_in_the_middle_baby_step_giant_step(a, prime, order, p, q):
    m = int(math.sqrt(order)) + 1
    pk = 0
    steps = 0
    found_pk = False

    #baby steps
    for j in range(1, m):
        jp = multiply_points_f_double_and_add(a, p, j, prime)[0][1]

        #giant steps
        for k in range(1, m + 1):
            multiplier = k*m
            kmp = multiply_points_f_double_and_add(a, p, multiplier, prime)[0][1]
            check = add_points_f(a, q, (kmp[0], prime - kmp[1]), prime)[:2]

            #collision found
            if check == jp:
                order_point = order_point_baby_step_giant_step(a, prime, p)[0]
                pk = (j + k*m)
                real_pk = (j + k*m) % order_point
                steps = (j - 1) * m + k
                found_pk = True

        if found_pk == True:
            break

    return (pk, real_pk, steps, order_point)