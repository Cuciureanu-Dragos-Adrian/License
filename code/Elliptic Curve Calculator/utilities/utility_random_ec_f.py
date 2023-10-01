import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sympy.ntheory.elliptic_curve import EllipticCurve
from sympy import randprime
import random


def generate_coefficients(prime):
    a = random.randint(0, prime - 1)
    b = random.randint(0, prime - 1)

    while (4*a**3 + 27*b**2) % prime == 0:
        a = random.randint(0, prime - 1)
        b = random.randint(0, prime - 1)

    return a, b


def generate_random_elliptic_curve_with_order(prime, order):
    a, b = generate_coefficients(prime)
    e = EllipticCurve(a, b, modulus = prime)

    order_ec = 0

    generating = False
    while generating == False:
        try:
            order_ec = e.order
            generating = True
        except:
            a, b = generate_coefficients(prime)
            e = EllipticCurve(a, b, modulus = prime)

        print(a, b, order_ec)

    while order_ec != order:
        generating = False
        while generating == False:
            try:
                order_ec = e.order
                generating = True
            except:
                a, b = generate_coefficients(prime)
                e = EllipticCurve(a, b, modulus = prime)

            print(a, b, order_ec)

    return (a, b, e + 1)


def generate_random_elliptic_curve(prime):
    a, b = generate_coefficients(prime)
    e = EllipticCurve(a, b, modulus = prime)

    order_ec = 0

    generating = False
    while generating == False:
        try:
            order_ec = e.order
            generating = True
        except:
            a, b = generate_coefficients(prime)
            e = EllipticCurve(a, b, modulus = prime)

    return (a, b, order_ec + 1)


def draw_image_random_f(a, b, prime):
    #we set the scale as being the prime number in the finite fields multiplied by 1.2
    scale = prime * 1.2

    #drawing the curve
    y, x = np.ogrid[-scale:scale:100j, -scale:scale:100j]
    plt.contour(x.ravel(), y.ravel(), ((y**2 - (x**3 - x * a - b))), [0], colors = 'black')

    sign_a = ''
    if a >= 0:
        sign_a = '+'
		
    sign_b = ''
    if b >= 0:
        sign_b = '+'

    plt.title(f'Elliptic Curve  Y^2 = X^3 {sign_a} {a:.2f}X {sign_b} {b:.2f} mod {prime}')
    plt.savefig('static/images/elliptic_curve_random_f.png')