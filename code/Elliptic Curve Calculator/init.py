import matplotlib
import matplotlib.pyplot as plt

from hashlib import sha256

from flask import Flask, render_template
from flask import request

from utilities.utility_addition_r import *
from utilities.utility_multiplication_r import *
from utilities.utility_addition_f import *
from utilities.utility_multiplication_f import *
from utilities.utility_improved_ecdh import *
from utilities.utility_time_ecdlp import *
from utilities.utility_atack_ecdlp import *
from utilities.utility_order_point import *
from utilities.utility_order_ec import *
from utilities.utility_random_ec_f import *
from utilities.utility import *


matplotlib.use('Agg')

app = Flask(__name__)


@app.route('/')
def start():
	#clear the buffer
	plt.clf()
	return render_template('home.html', get_plot = False)


@app.route('/addition_r', methods=['GET', 'POST'])
def addition_r():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		coefficients = (a, b)

		#point P
		px = request.form['coordinate_p_x']
		py = request.form['coordinate_p_y']

		# determine if P == O('inf', 'inf')
		if px != 'inf':
			px = float(px)
			py = float(py)

		#point Q
		qx = request.form['coordinate_q_x']
		qy = request.form['coordinate_q_y']

		# determine if Q == O('inf', 'inf')
		if qx != 'inf':
			qx = float(qx)
			qy = float(qy)

		#verify that data is correct
		p = (px, py)
		q = (qx, qy)

		error_flag, error_message = verify_data_r(a, b, p, q)

		if error_flag == True:
			return render_template('addition_r.html', error_flag = error_flag, error_message = error_message)

		#point R = P + Q
		rx, ry, case, slope = add_points_r(a, (px, py), (qx, qy))

		#load the data for the table
		data = load_data_addition_r((px, py), (qx, qy), (rx, ry))
			
		#determine the nature of the result and the draw
		if ry == 'inf':
			#draw the image for an infinite result and save it
			draw_image_addition_r_inf(a, b, px, py, qx, qy)

		elif (px, py) != (rx, ry) and (qx, qy) != (rx, ry):
			rpx, rpy = rx, -ry

			#draw the image for a finite result and save it
			draw_image_addition_r_fin(a, b, px, py, qx, qy, rx, ry, rpx, rpy)

		else:
			rpx, rpy = rx, -ry

			#draw the image in the case of X + O = X
			draw_image_addition_r_id(a, b, rx, ry)

		return render_template('addition_r.html', get_plot = True, plot_url = 'static/images/elliptic_curve_addition_r.png', 
			 data = data, case = case, slope = slope, coefficients = coefficients)
	else:
		return render_template('addition_r.html')


@app.route('/multiplication_r', methods=['GET', 'POST'])
def multiplication_r():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		#point P
		px = request.form['coordinate_p_x']
		py = request.form['coordinate_p_y']

		# determine if P == O('inf', 'inf')
		if px != 'inf':
			px = float(px)
			py = float(py)

		#number N
		n = int(request.form['multiply_number'])

		#verify that data is correct
		p = (px, py)

		error_flag, error_message = verify_data_one_point_r(a, b, p)

		if error_flag == True:
			return render_template('multiplication_r.html', error_flag = error_flag, error_message = error_message)
		
		#the list that will contain the multiplication points (P, R)
		points = []

		#call the multimplication method
		#points = multiply_points_r(a, (px, py), n)

		#call the multimplication method with double and add algorithm
		points, multiplication_steps, additions, multiplications = multiply_points_r_double_and_add(a, (px, py), n)

		#load the data for the table
		data = load_data_multiplication_r(points)

		#draw the image for the result
		draw_image_multiplication_r(a, b, points, n)
		
		return render_template('multiplication_r.html', get_plot = True, plot_url = 'static/images/elliptic_curve_multiplication_r.png', 
			 data = data, multiplication_steps = multiplication_steps, additions = additions, multiplications = multiplications, n = n)
	else:
		return render_template('multiplication_r.html')
	

@app.route('/addition_f', methods=['GET', 'POST'])
def addition_f():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		coefficients = (int(a), int(b))

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#point P
		px = request.form['coordinate_p_x']
		py = request.form['coordinate_p_y']

		# determine if P == O('inf', 'inf')
		if px != 'inf':
			px = float(px)
			py = float(py)

		#point Q
		qx = request.form['coordinate_q_x']
		qy = request.form['coordinate_q_y']

		# determine if Q == O('inf', 'inf')
		if qx != 'inf':
			qx = float(qx)
			qy = float(qy)

		#verify that data is correct
		p = (px, py)
		q = (qx, qy)

		error_flag, error_message = verify_data_fp(a, b, prime, p, q)

		if error_flag == True:
			return render_template('addition_f.html', error_flag = error_flag, error_message = error_message)

		#point R = P + Q
		#rx, ry = add_points_f(a, (px, py), (qx, qy), prime)
		rx, ry, case, slope, t1, t2 = add_points_f(a, (px, py), (qx, qy), prime)

		#termens of the fraction
		t = (t1, t2)

		#load the data for the table
		data = load_data_addition_f((px, py), (qx, qy), (rx, ry))
		
		#draw the image for a finite result and save it
		draw_image_addition_f_fin(a, b, px, py, qx, qy, rx, ry, prime)

		return render_template('addition_f.html', get_plot = True, plot_url = 'static/images/elliptic_curve_addition_f.png', 
			 data = data, case = case, slope = slope, coefficients = coefficients, t = t, prime = prime)
	else:
		return render_template('addition_f.html')


@app.route('/multiplication_f', methods=['GET', 'POST'])
def multiplication_f():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#point P
		px = request.form['coordinate_p_x']
		py = request.form['coordinate_p_y']

		# determine if P == O('inf', 'inf')
		if px != 'inf':
			px = float(px)
			py = float(py)

		#verify that data is correct
		p = (px, py)

		error_flag, error_message = verify_data_one_point_fp(a, b, prime, p)

		if error_flag == True:
			return render_template('multiplication_f.html', error_flag = error_flag, error_message = error_message)

		#number N
		n = int(request.form['multiply_number'])
		
		#the list that will contain the multiplication points (P, R)
		points = []

		#call the multimplication method
		#points = multiply_points_f(a, (px, py), n, prime)

		#call the multimplication method with double and add algorithm
		points, multiplication_steps, additions, multiplications = multiply_points_f_double_and_add(a, (px, py), n, prime)

		#load the data for the table
		data = load_data_multiplication_f(points)

		#draw the image for the result
		draw_image_multiplication_f(a, b, points, prime, n)
		
		return render_template('multiplication_f.html', get_plot = True, plot_url = 'static/images/elliptic_curve_multiplication_f.png', 
			data = data, multiplication_steps = multiplication_steps, additions = additions, multiplications = multiplications, n = n)
	else:
		return render_template('multiplication_f.html')
	

@app.route('/normal_ecdh', methods=['GET', 'POST'])
def normal_ecdh():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#details of the elliptic curve
		ec = (int(a), int(b), prime)

		#point P
		px = request.form['coordinate_p_x']
		py = request.form['coordinate_p_y']

		# determine if P == O('inf', 'inf')
		if px != 'inf':
			px = float(px)
			py = float(py)

		p = (int(px), int(py))

		#verify that data is correct
		error_flag, error_message = verify_data_one_point_fp(a, b, prime, p)

		if error_flag == True:
			return render_template('normal_ecdh.html', error_flag = error_flag, error_message = error_message)

		#Alice's secret number
		na = int(request.form['secret_n_a'])

		#Bob's secret number
		nb = int(request.form['secret_n_b'])

		secret_numbers = (na, nb)

		#step 2: secret keys
		public_key_a = multiply_points_f_double_and_add(a, p, na, prime)[0][1]
		public_key_b = multiply_points_f_double_and_add(a, p, nb, prime)[0][1]

		public_keys = (public_key_a, public_key_b)

		#step 3: shared keys
		shared_key_a = multiply_points_f_double_and_add(a, public_key_b, na, prime)[0][1]
		shared_key_b = multiply_points_f_double_and_add(a, public_key_a, nb, prime)[0][1]

		shared_keys = (shared_key_a, shared_key_b)
		
		return render_template('normal_ecdh.html', get_plot = True, plot_url = 'static/theory/ECDH.png',
			ec = ec, p = p, secret_numbers = secret_numbers, public_keys = public_keys, shared_keys = shared_keys)
	else:
		return render_template('normal_ecdh.html')
	

@app.route('/improved_ecdh', methods=['GET', 'POST'])
def improved_ecdh():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#details of the elliptic curve
		ec = (int(a), int(b), prime)

		#point P
		px = request.form['coordinate_p_x']
		py = request.form['coordinate_p_y']

		# determine if P == O('inf', 'inf')
		if px != 'inf':
			px = float(px)
			py = float(py)

		p = (int(px), int(py))

		#verify that data is correct
		error_flag, error_message = verify_data_one_point_fp(a, b, prime, p)

		if error_flag == True:
			return render_template('improved_ecdh.html', error_flag = error_flag, error_message = error_message)

		#Alice's secret number
		na = int(request.form['secret_n_a'])

		#Bob's secret number
		nb = int(request.form['secret_n_b'])

		secret_numbers = (na, nb)

		#step 2: secret keys
		public_key_a = multiply_points_f_double_and_add(a, p, na, prime)[0][1]
		public_key_b = multiply_points_f_double_and_add(a, p, nb, prime)[0][1]

		#step 3:
		#determine square ys
		square_ya = result_equation_ec(a, b, prime, public_key_a[0])
		square_yb = result_equation_ec(a, b, prime, public_key_b[0])

		square_ys = (square_ya, square_yb)

		#determine ys
		ya, power_ya = determine_y(prime, square_ya)
		yb, power_yb = determine_y(prime, square_yb)

		public_keys = (public_key_a, public_key_b)
		ys = (ya, yb)
		power_ys = (power_ya, power_yb)

		# shared keys
		shared_key_a = multiply_points_f_double_and_add(a, (public_keys[1][0], ys[1]), na, prime)[0][1]
		shared_key_b = multiply_points_f_double_and_add(a, (public_keys[0][0], ys[0]), nb, prime)[0][1]

		shared_keys = (shared_key_a, shared_key_b)
		
		return render_template('improved_ecdh.html', get_plot = True, plot_url = 'static/theory/ECDH.png',
			ec = ec, p = p, secret_numbers = secret_numbers, public_keys = public_keys, square_ys = square_ys, ys = ys,
			power_ys = power_ys, shared_keys = shared_keys)
	else:
		return render_template('improved_ecdh.html')
	

@app.route('/normal_eceg', methods=['GET', 'POST'])
def normal_eceg():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#details of the elliptic curve
		ec = (int(a), int(b), prime)

		#point P
		px = request.form['coordinate_p_x']
		py = request.form['coordinate_p_y']

		p = (int(px), int(py))

		#verify that data is correct
		error_flag, error_message = verify_data_one_point_fp(a, b, prime, p)

		if error_flag == True:
			return render_template('normal_eceg.html', error_flag = error_flag, error_message = error_message)

		#Alice's secret number
		na = int(request.form['secret_n_a'])

		#message point M
		mx = request.form['coordinate_m_x']
		my = request.form['coordinate_m_y']

		m = (int(mx), int(my))

		#Bob's temporal number
		k = int(request.form['temporal_key_k'])

		#step 2: public key creation
		qa = multiply_points_f_double_and_add(a, p, na, prime)[0][1]

		#step 3: encryption
		c1 = multiply_points_f_double_and_add(a, p, k, prime)[0][1]

		k_qa = multiply_points_f_double_and_add(a, qa, k, prime)[0][1]
		c2 = add_points_f(a, m, k_qa, prime)[:2]

		#step 4: decryption
		na_c1 = multiply_points_f_double_and_add(a, c1, na, prime)[0][1]
		reverse_na_c1 = (na_c1[0], prime - na_c1[1])

		final_m = add_points_f(a, c2, reverse_na_c1, prime)[:2]
		
		return render_template('normal_eceg.html', get_plot = True, plot_url = 'static/theory/ECEG.png',
			ec = ec, p = p, na = na, m = m, k = k, qa = qa, c1 = c1, k_qa = k_qa, c2 = c2, na_c1 = na_c1, 
			reverse_na_c1 = reverse_na_c1, final_m = final_m)
	else:
		return render_template('normal_eceg.html')
	

@app.route('/improved_eceg', methods=['GET', 'POST'])
def improved_eceg():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#details of the elliptic curve
		ec = (int(a), int(b), prime)

		#point P
		px = request.form['coordinate_p_x']
		py = request.form['coordinate_p_y']

		p = (int(px), int(py))

		#verify that data is correct
		error_flag, error_message = verify_data_one_point_fp(a, b, prime, p)

		if error_flag == True:
			return render_template('improved_eceg.html', error_flag = error_flag, error_message = error_message)

		#Alice's secret number
		na = int(request.form['secret_n_a'])

		#message point M
		mx = request.form['coordinate_m_x']
		my = request.form['coordinate_m_y']

		m = (int(mx), int(my))

		#Bob's temporal number
		k = int(request.form['temporal_key_k'])

		#step 2: public key creation
		qa = multiply_points_f_double_and_add(a, p, na, prime)[0][1]

		#step 3: encryption
		c1 = multiply_points_f_double_and_add(a, p, k, prime)[0][1]

		k_qa = multiply_points_f_double_and_add(a, qa, k, prime)[0][1]
		c2 = add_points_f(a, m, k_qa, prime)[:2]

		bit_c1 = 0
		if c1[1] > prime / 2:
			bit_c1 = 1 

		bit_c2 = 0
		if c2[1] > prime / 2:
			bit_c2 = 1 

		bits = (bit_c1, bit_c2)

		#step 4: decryption

		#determine square ys
		square_yc1 = result_equation_ec(a, b, prime, c1[0])
		square_yc2 = result_equation_ec(a, b, prime, c2[0])

		square_ys = (square_yc1, square_yc2)

		#determine ys
		yc1, power_yc1 = determine_y(prime, square_yc1)
		yc2, power_yc2 = determine_y(prime, square_yc2)

		ys = (yc1, yc2)
		power_ys = (power_yc1, power_yc2)

		#determine real ys
		real_yc1 = yc1
		if (bit_c1 == 0 and yc1 > prime / 2) or (bit_c1 == 1 and yc1 < prime / 2):
			real_yc1 = prime - yc1
		
		real_yc2 = yc2
		if (bit_c2 == 0 and yc2 > prime / 2) or (bit_c2 == 1 and yc2 < prime / 2):
			real_yc2 = prime - yc2

		real_ys = (real_yc1, real_yc2)

		#decrypt process
		na_c1 = multiply_points_f_double_and_add(a, c1, na, prime)[0][1]
		reverse_na_c1 = (na_c1[0], prime - na_c1[1])

		final_m = add_points_f(a, c2, reverse_na_c1, prime)[:2]
		
		return render_template('improved_eceg.html', get_plot = True, plot_url = 'static/theory/ECEG.png',
			ec = ec, p = p, na = na, m = m, k = k, qa = qa, c1 = c1, k_qa = k_qa, c2 = c2, na_c1 = na_c1, bits = bits, ys = ys,
			reverse_na_c1 = reverse_na_c1, final_m = final_m, square_ys = square_ys, power_ys = power_ys, real_ys = real_ys)
	else:
		return render_template('improved_eceg.html')
	

@app.route('/normal_ecdsa', methods=['GET', 'POST'])
def normal_ecdsa():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#details of the elliptic curve
		ec = (int(a), int(b), prime)

		#point G
		gx = request.form['coordinate_g_x']
		gy = request.form['coordinate_g_y']

		g = (int(gx), int(gy))

		#verify that data is correct
		error_flag, error_message = verify_data_one_point_fp(a, b, prime, g)

		if error_flag == True:
			return render_template('normal_ecdsa.html', error_flag = error_flag, error_message = error_message)

		#order of point G
		q = order_point_baby_step_giant_step(a, prime, g)[0]

		#Alice's secret signing key
		s = int(request.form['secret_s'])

		#text message that will be signed
		m = request.form['message_m']

		#hash of the message via SHA-256
		hash_m = sha256(m.encode('utf-8')).hexdigest()

		#the document that will be signed
		int_d = int(hash_m, base=16)
		d = int_d % q

		#Bob's ephemeral number
		e = int(request.form['ephemeral_key_e'])

		#step 2: key creation

		#verification key
		v = multiply_points_f_double_and_add(a, g, s, prime)[0][1]

		#step 3: signing

		#point R
		r = multiply_points_f_double_and_add(a, g, e, prime)[0][1]

		#signatures
		s1 = r[0] % q
		s2 = (d + s * s1) * pow(e, -1, q) % q
		
		#step 4: verification

		#verifications
		v1 = d * pow(s2, -1, q) % q
		v2 = s1 * pow(s2, -1, q) % q

		#the verification point R'
		term1 = multiply_points_f_double_and_add(a, g, v1, prime)[0][1]
		term2 = multiply_points_f_double_and_add(a, v, v2, prime)[0][1]
		r_prime = add_points_f(a, term1, term2, prime)[:2]
		r_prime_x = r_prime[0] % q
		
		return render_template('normal_ecdsa.html', get_plot = True, plot_url = 'static/theory/ECDSA.png', ec = ec, g = g, q = q,
			s = s, m = m, hash_m = hash_m, int_d = int_d, d = d, e = e, v = v, r = r, s1 = s1, s2 = s2, v1 = v1, v2 = v2, 
			term1 = term1, term2 = term2, r_prime = r_prime, r_prime_x = r_prime_x)
	else:
		return render_template('normal_ecdsa.html')
	

@app.route('/time_ecdlp', methods=['GET', 'POST'])
def time_ecdlp():
	if request.method == 'POST':

		#coefficients of the elliptic curve
		o = float(request.form['order_o'])

		#determine orders
		log_order, root_log_order = determine_orders(o)

		orders = (o, log_order, int(log_order), root_log_order)

		#determine time measures
		time_measures = determine_time_measures(root_log_order)
		
		return render_template('time_ecdlp.html', orders = orders, time_measures = time_measures)
	else:
		return render_template('time_ecdlp.html')
	

@app.route('/atack_ecdlp', methods=['GET', 'POST'])
def atack_ecdlp():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#details of the elliptic curve
		ec = (int(a), int(b), prime)

		#point P
		px = request.form['coordinate_p_x']
		py = request.form['coordinate_p_y']

		# determine if P == O('inf', 'inf')
		if px != 'inf':
			px = float(px)
			py = float(py)

		p = (int(px), int(py))

		#point Q
		qx = request.form['coordinate_q_x']
		qy = request.form['coordinate_q_y']

		# determine if Q == O('inf', 'inf')
		if qx != 'inf':
			qx = float(qx)
			qy = float(qy)

		q = (int(qx), int(qy))

		#verify that data is correct
		error_flag, error_message = verify_data_fp(a, b, prime, p, q)

		if error_flag == True:
			return render_template('atack_ecdlp.html', error_flag = error_flag, error_message = error_message)

		#determine the order of the Elliptic Curve
		order = determine_elliptic_curve_order(a, b, prime)

		#determine private key
		pk, real_pk, steps, order_point = meet_in_the_middle_baby_step_giant_step(a, prime, order, p, q)

		return render_template('atack_ecdlp.html', pk = pk, real_pk = real_pk, steps = steps, 
			order_point = order_point, p = p, q = q)
	else:
		return render_template('atack_ecdlp.html')
	
	
@app.route('/order_point', methods=['GET', 'POST'])
def order_point():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#details of the elliptic curve
		ec = (int(a), int(b), prime)

		#point P
		px = request.form['coordinate_p_x']
		py = request.form['coordinate_p_y']

		p = (int(px), int(py))

		#verify that data is correct
		error_flag, error_message = verify_data_one_point_fp(a, b, prime, p)

		if error_flag == True:
			return render_template('order_point.html', error_flag = error_flag, error_message = error_message)

		#determine the order of the Elliptic Curve
		orders = order_point_baby_step_giant_step(a, prime, p)
		
		return render_template('order_point.html', ec = ec, p = p, orders = orders)
	else:
		return render_template('order_point.html')


@app.route('/order_ec', methods=['GET', 'POST'])
def order_ec():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#coefficients of the elliptic curve
		a = float(request.form['coefficient_curve_a'])
		b = float(request.form['coefficient_curve_b'])

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#verify that data is correct
		error_flag, error_message = verify_data_no_point_fp(a, b, prime)

		if error_flag == True:
			return render_template('order_ec.html', error_flag = error_flag, error_message = error_message)

		#details of the elliptic curve
		ec = (int(a), int(b), prime)

		#determine the order of the Elliptic Curve
		order = determine_elliptic_curve_order(a, b, prime)

		return render_template('order_ec.html', ec = ec, order = order)
	else:
		return render_template('order_ec.html')
	

@app.route('/random_ec_f', methods=['GET', 'POST'])
def random_ec_f():
	if request.method == 'POST':
		#clear the buffer
		plt.clf()

		#prime number in Fp
		prime = int(request.form['prime_p'])

		#verify that data is correct
		error_flag, error_message = verify_data_prime_fp(prime)

		if error_flag == True:
			return render_template('random_ec_f.html', error_flag = error_flag, error_message = error_message)

		#determine the coefficients of the random Elliptic Curve
		a, b, order = generate_random_elliptic_curve(prime)

		#draw the image for the result
		draw_image_random_f(a, b, prime)

		ec = (int(a), int(b), prime)
		
		return render_template('random_ec_f.html', ec = ec, order = order)
	else:
		return render_template('random_ec_f.html')


#Run the app on localhost port 5000
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)


