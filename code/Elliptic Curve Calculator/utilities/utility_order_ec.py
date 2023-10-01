import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sympy.ntheory.elliptic_curve import EllipticCurve


def determine_elliptic_curve_order(a, b, p):
    #instantiate the elliptic curve
    e = EllipticCurve(a, b, modulus = p)

    #determine the order of the elliptic curve
    order = e.order + 1

    return order


def draw_image_order_f(a, b, prime):
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

    plt.title(f'Elliptic Curve  Y^2 = X^3 {sign_a}{a:.2f}X {sign_b}{b:.2f}')
    plt.savefig('static/images/elliptic_curve_order_f.png')