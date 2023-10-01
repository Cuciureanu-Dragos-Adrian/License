import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


#utility function for adding 2 points on the elliptic curve on finite fields
def gcd_extended(a, b):
     if a == 0:
          return b, 0, 1
     gcd, px, py = gcd_extended(b % a, a)
     x = py - (b // a) * px
     y = px
     return gcd, x, y


#utility function for adding 2 points on the elliptic curve on finite fields
def gcd_extended_generalized(a, b):
    gcd, px, py = gcd_extended(abs(a), b)
    return gcd, (np.sign(a) * px) % b, py % b


#function for adding 2 points on the elliptic curve
def add_points_f(a, p, q, prime):
	px, py = p[0], p[1]
	qx, qy = q[0], q[1]

	#case 1: P or Q == O('inf', 'inf')
	if px == 'inf':
		return (qx, qy, 1, 0, 0, 0)
	if qx == 'inf':
		return (px, py, 1 ,0, 0, 0)

	#case 2: P == -Q
	if py == prime - qy:
		return ('inf', 'inf', 2, 0, 0, 0)

	#case 3: P == Q
	if px == qx and py == qy:
		t1 = int(3 * px ** 2 + a)
		t2 = pow(int(2 * py), -1, prime)
        
		#slope
		s = (t1 * t2) % prime

		#new point
		rx = (s ** 2 - 2 * px) % prime
		ry = (s * (px - rx) - py) % prime

		return (rx, ry, 3, s, t1, t2)

	#case 4: P != Q
	t1 = int(qy - py)
	t2 = pow(int(qx - px), -1, prime)
        
	#slope
	s = (t1 * t2) % prime

	#new point
	rx = (s ** 2 - px - qx) % prime
	ry = (s * (px - rx) - py) % prime

	return (rx, ry, 4, int(s), t1, t2)


#function for loading the data for the table
def load_data_addition_f(p, q, r):
	#data for the table 
	points_name = ['P', 'Q', 'R']
	points_value = [p, q, r]

	#adding the data to the table
	data = {}
	for i in range(len(points_name)):
		if points_value[i][0] != 'inf':
			data[points_name[i]] = (int(points_value[i][0]), int(points_value[i][1]))
		else:
			data[points_name[i]] = points_value[i]

	return data


#function for drawing the image for the result and saving it
def draw_image_addition_f_fin(a, b, px, py, qx, qy, rx, ry, prime):
	#we set the scale as being the prime number in the finite fields multiplied by 1.2
    scale = prime * 1.2
    
    #drawing the curve
    y, x = np.ogrid[0:scale:100j, 0:scale:100j]
    plt.contour(x.ravel(), y.ravel(), y**2 - x**3 - x * a - b, [0], colors='white')

    #draw the initial points
    plt.plot(px, py, 'bo')
    plt.text(px, py, f'  P')

    #determine if the points are different
    if (px, py) != (qx, qy):
        plt.plot(qx, qy, 'bo')
        plt.text(qx, qy, f'  Q')

    #draw the sum of the points
    plt.plot(rx, ry, 'bo')
    plt.text(rx, ry, f'  R')

    plt.grid()

    sign_a = ''
    if a >= 0:
        sign_a = '+'
    
    sign_b = ''
    if b >= 0:
        sign_b = '+'

    plt.title(f'Elliptic Curve  Y^2 = X^3 {sign_a}{int(a)}X {sign_b}{int(b)} mod {int(prime)}')
    plt.savefig('static/images/elliptic_curve_addition_f.png')
    




