import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#function for adding 2 points on the elliptic curve
def add_points_r(a, p, q):
	px, py = p[0], p[1]
	qx, qy = q[0], q[1]

	#case 1: P or Q == O('inf', 'inf')
	if px == 'inf':
		return (qx, qy, 1, 0)
	if qx == 'inf':
		return (px, py, 1, 0)

	#case 2: P == -Q
	if py == -qy:
		return ('inf', 'inf', 2, 0)

	#case 3: P == Q
	if px == qx and py == qy:
		#slope
		s = (3 * px ** 2 + a) / (2 * py)

		#new point
		rx = s ** 2 - 2 * px
		ry = s * (px - rx) - py

		return (round(rx, 4), round(ry, 4), 3, s)

	#case 4: P != Q
	#slope
	s = (qy - py) / (qx - px)

	#new point
	rx = s ** 2 - px - qx
	ry = s * (px - rx) - py

	return (round(rx, 4), round(ry, 4), 4, s)


#function for loading the data for the table
def load_data_addition_r(p, q, r):
	#data for the table 
	points_name = ['P', 'Q', 'R']
	points_value = [p, q, r]

	#adding the data to the table
	data = {}
	for i in range(len(points_name)):
		data[points_name[i]] = points_value[i]

	return data


#function for drawing the image for a finite result and saving it
def draw_image_addition_r_fin(a, b, px, py, qx, qy, rx, ry, rpx, rpy):
	#we determine the scale of the graph based on the max abs point or 10
	points = [abs(px), abs(py), abs(qx), abs(qy), abs(rx), abs(ry), abs(rpx), abs(rpy), 10]
	scale = max(points) * 1.2

	#divide the list of points into xs and ys for the lines that we want to draw
	#line1 - line that intersect P and Q
	#line2 - line for the reverse R'
	line1_x = [px, qx, rpx]
	line1_y = [py, qy, rpy]
	line2_x = [rx, rpx]
	line2_y = [ry, rpy]
	
	#drawing the curve
	y, x = np.ogrid[-scale:scale:100j, -scale:scale:100j]
	plt.contour(x.ravel(), y.ravel(), y**2 - x**3 - x * a - b, [0], colors='black')

	#draw the initial points
	plt.plot(px, py, 'bo')
	plt.text(px, py, f'  P')

	#determine if the points are different
	if (px, py) != (qx, qy):
		plt.plot(qx, qy, 'bo')
		plt.text(qx, qy, f'  Q')

	#draw the sum of the points
	plt.plot(rpx, rpy, 'bo')
	plt.text(rpx, rpy, f'  R\'')
	plt.plot(rx, ry, 'bo')
	plt.text(rx, ry, f'  R')

	#draw the lines
	plt.plot(line1_x, line1_y, color='yellow')
	plt.plot(line2_x, line2_y, color='red', linestyle='dashed')

	plt.grid()

	sign_a = ''
	if a >= 0:
		sign_a = '+'
	
	sign_b = ''
	if b >= 0:
		sign_b = '+'

	plt.title(f'Elliptic Curve  Y^2 = X^3 {sign_a}{a:.2f}X {sign_b}{b:.2f}')
	plt.savefig('static/images/elliptic_curve_addition_r.png')


#function for drawing the image for an infinite result and saving it
def draw_image_addition_r_inf(a, b, px, py, qx, qy):
	#we determine the scale of the graph based on the max abs point or 10
	points = [abs(px), abs(py), abs(qx), abs(qy), 10]
	scale = max(points) * 1.2

	#divide the list of points into xs and ys for the lines that we want to draw
	#line1 - line that intersect P and Q
	#line2 - line for the reverse R'
	line1_x = [px, qx]
	line1_y = [-scale, scale]
	
	#drawing the curve
	y, x = np.ogrid[-scale:scale:100j, -scale:scale:100j]
	plt.contour(x.ravel(), y.ravel(), y**2 - x**3 - x * a - b, [0], colors='black')

	#draw the initial points
	plt.plot(px, py, 'bo')
	plt.text(px, py, f'  P')
	plt.plot(qx, qy, 'bo')
	plt.text(qx, qy, f'  Q')

	#draw the lines
	plt.plot(line1_x, line1_y, color='yellow')

	plt.grid()

	sign_a = ''
	if a >= 0:
		sign_a = '+'
	
	sign_b = ''
	if b >= 0:
		sign_b = '+'

	plt.title(f'Elliptic Curve  Y^2 = X^3 {sign_a}{a:.2f}X {sign_b}{b:.2f}')
	plt.savefig('static/images/elliptic_curve_addition_r.png')


#function for drawing the image in the case of X + O = X
def draw_image_addition_r_id(a, b, rx, ry):
	#we determine the scale of the graph based on the max abs point or 10
	points = [abs(rx), abs(ry), 10]
	scale = max(points) * 1.2

	#divide the list of points into xs and ys for the lines that we want to draw
	#line1 - line that intersect P and Q
	#line2 - line for the reverse R'
	line1_x = [rx, rx]
	line1_y = [scale, -ry]
	line2_x = [rx, rx]
	line2_y = [ry, -ry]
	
	#drawing the curve
	y, x = np.ogrid[-scale:scale:100j, -scale:scale:100j]
	plt.contour(x.ravel(), y.ravel(), y**2 - x**3 - x * a - b, [0], colors='black')

	#draw the initial points
	plt.plot(rx, ry, 'bo')
	plt.text(rx, ry, f'  Original Point and Result')

	#draw the sum of the points
	plt.plot(rx, -ry, 'bo')
	plt.text(rx, -ry, f'  R\'')

	#draw the lines
	plt.plot(line1_x, line1_y, color='yellow')
	plt.plot(line2_x, line2_y, color='red', linestyle='dashed')

	plt.grid()

	sign_a = ''
	if a >= 0:
		sign_a = '+'
	
	sign_b = ''
	if b >= 0:
		sign_b = '+'

	plt.title(f'Elliptic Curve  Y^2 = X^3 {sign_a}{a:.2f}X {sign_b}{b:.2f}')
	plt.savefig('static/images/elliptic_curve_addition_r.png')