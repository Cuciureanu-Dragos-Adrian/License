from utilities.utility_addition_f import *

#function for multipling a points by a positive number on the elliptic curve
def multiply_points_f(a, p, n, prime):
    #the list that will contain all the multiplication (P, 2P, 3P, ..., NP)
    points = []

    px, py = p[0], p[1]
    rx, ry = px, py

    points.append((rx, ry))

    while n > 1:
        #add to the current xP another P (xP + P) 
        rx, ry, _, _, _ = add_points_f(a, (px, py), (rx, ry), prime)

        #and add it to the list of restuls
        points.append((rx, ry))

        #decrement the number
        n -= 1

    return points


#function for multipling a points by a positive number on the elliptic curve
def multiply_points_f_double_and_add(a, p, n, prime):
    #the list that will contain all the steps for the double and add algorithm
    multiplication_steps = []

    if p[0] != 'inf':
        q = (int(p[0]), int(p[1]))
    else:
        q = (p[0], p[1])
    r = ('inf', 'inf')
    step = 0
    additions = 0

    multiplication_steps.append((step, n, q, r))

    #double and add algorithm
    while n > 0:
        step += 1

        if n % 2 == 1:
            rx, ry, _, _, _, _ = add_points_f(a, r, q, prime)
            if rx != 'inf':
                r = (int(rx), int(ry))
            else:
                r = (rx, ry)

            additions += 1

        qx, qy, _, _, _, _ = add_points_f(a, q, q, prime)
        if qx != 'inf':
            q = (int(qx), int(qy))
        else:
            q = (qx, qy)
        
        n //= 2

        multiplication_steps.append((step, n, q, r))

    multiplications = len(multiplication_steps) - 1

    return ((p, r), multiplication_steps, additions, multiplications)


def load_data_multiplication_f(points):
    #data for the table 
    points_names = ['P', 'R']

	#adding the data to the table
    data = {}
    for i in range(len(points_names)):
        if points[i][0] != 'inf':
            data[points_names[i]] = (int(points[i][0]), int(points[i][1]))
        else:
            data[points_names[i]] = points[i]
        
    return data


def draw_image_multiplication_f(a, b, points, prime, n):
    #data for the table 
    points_names = ['P', 'R = ' + str(n) + 'P']

    #we set the scale as being the prime number in the finite fields multiplied by 1.2
    scale = prime * 1.2

    #drawing the curve
    y, x = np.ogrid[0:scale:100j, 0:scale:100j]
    plt.contour(x.ravel(), y.ravel(), (y**2 - (x**3 - x * a - b)), [0], colors = 'white')

    #drawing the points
    point = points[0]
    plt.plot(point[0], point[1], 'bo')
    plt.text(point[0], point[1], '  ' + points_names[0])

    result = points[-1]
    if result[0] == 'inf':
        result = (scale, scale) 
        
    plt.plot(result[0], result[1], 'bo')
    plt.text(result[0], result[1], '  ' + points_names[1])

    plt.grid()

    sign_a = ''
    if a >= 0:
        sign_a = '+'
		
    sign_b = ''
    if b >= 0:
        sign_b = '+'

    plt.title(f'Elliptic Curve  Y^2 = X^3 {sign_a}{int(a)}X {sign_b}{int(b)} mod {int(prime)}')
    plt.savefig('static/images/elliptic_curve_multiplication_f.png')
