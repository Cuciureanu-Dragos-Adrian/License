from sympy import *


#def verify data for R
def verify_data_r(a, b, p, q):
     discriminant = 4*a**3 + 27*b**2

     if discriminant == 0:
          return True, "The provided curve has the discriminant 0."
     
     py_square = 'inf'
     p_polinom = 'inf'

     if p[1] != 'inf':
          py_square = p[1] ** 2
          p_polinom = (p[0] ** 3 + a * p[0] + b)

     if py_square != p_polinom: 
          return (True, f"The point P is not on the provided elliptic curve because {(py_square)} != {(p_polinom)}")

     qy_square = 'inf'
     q_polinom = 'inf'

     if q[1] != 'inf':
          qy_square = q[1] ** 2
          q_polinom = (q[0] ** 3 + a * q[0] + b)
     
     if qy_square != q_polinom: 
          return (True, f"The point Q is not on the provided elliptic curve because {(qy_square)} != {(p_polinom)}")
     
     return (False, "No error")


#def verify data for R
def verify_data_one_point_r(a, b, p):
     discriminant = 4*a**3 + 27*b**2

     if discriminant == 0:
          return True, "The provided curve has the discriminant 0."
     
     py_square = 'inf'
     p_polinom = 'inf'

     if p[1] != 'inf':
          py_square = p[1] ** 2
          p_polinom = (p[0] ** 3 + a * p[0] + b)

     if py_square != p_polinom: 
          return (True, f"The point P is not on the provided elliptic curve because {(py_square)} != {(p_polinom)}")
     
     return (False, "No error")


#def verify data for finite fields
def verify_data_fp(a, b, prime, p, q):
     prime_flag = isprime(prime)

     if prime_flag == False:
          return (True, f"The provided number {prime} is not prime.")
     
     discriminant = 4*a**3 + 27*b**2 % prime

     if discriminant == 0:
          return (True, "The provided curve has the discriminant 0.")
     
     py_square = 'inf'
     p_polinom = 'inf'

     if p[1] != 'inf':
          py_square = p[1] ** 2 % prime
          p_polinom = (p[0] ** 3 + a * p[0] + b) % prime

     if py_square != p_polinom: 
          return (True, f"The point P is not on the provided elliptic curve because {(py_square)} != {(p_polinom)}")

     qy_square = 'inf'
     q_polinom = 'inf'

     if q[1] != 'inf':
          qy_square = q[1] ** 2 % prime
          q_polinom = (q[0] ** 3 + a * q[0] + b) % prime
     
     if qy_square != q_polinom: 
          return (True, f"The point Q is not on the provided elliptic curve because {(qy_square)} != {(p_polinom)}")
     
     return (False, "No error")


#def verify data for finite fields for only one point
def verify_data_one_point_fp(a, b, prime, p):
     prime_flag = isprime(prime)

     if prime_flag == False:
          return (True, f"The provided number {prime} is not prime.")
     
     discriminant = 4*a**3 + 27*b**2 % prime

     if discriminant == 0:
          return (True, "The provided curve has the discriminant 0.")
     
     py_square = 'inf'
     p_polinom = 'inf'

     if p[1] != 'inf':
          py_square = p[1] ** 2 % prime
          p_polinom = (p[0] ** 3 + a * p[0] + b) % prime

     if py_square != p_polinom: 
          return (True, f"The point P is not on the provided elliptic curve because {(py_square)} != {(p_polinom)}")
     
     return (False, "No error")


#def verify data for finite fields for no point
def verify_data_no_point_fp(a, b, prime):
     prime_flag = isprime(prime)

     if prime_flag == False:
          return (True, f"The provided number {prime} is not prime.")
     
     discriminant = 4*a**3 + 27*b**2 % prime

     if discriminant == 0:
          return (True, "The provided curve has the discriminant 0.")
     
     return (False, "No error")


#def verify the prime number
def verify_data_prime_fp(prime):
     prime_flag = isprime(prime)

     if prime_flag == False:
          return (True, f"The provided number {prime} is not prime.")
     
     return (False, "No error")