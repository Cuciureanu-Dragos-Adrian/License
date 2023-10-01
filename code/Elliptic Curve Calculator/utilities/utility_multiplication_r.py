from utilities.utility_addition_r import *

#function for multipling a points by a positive number on the elliptic curve
def multiply_points_r(a, p, n):
    #the list that will contain all the multiplication (P, 2P, 3P, ..., NP)
    points = []

    px, py = p[0], p[1]
    rx, ry = px, py

    points.append((rx, ry))

    while n > 1:
        #add to the current xP another P (xP + P) 
        rx, ry, _, _ = add_points_r(a, (px, py), (rx, ry))

        #and add it to the list of restuls
        points.append((rx, ry))

        #decrement the number
        n -= 1

    return points


#function for multipling a points by a positive number on the elliptic curve
def multiply_points_r_double_and_add(a, p, n):
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
            rx, ry, _, _ = add_points_r(a, r, q)
            r = (round(rx, 4), round(ry, 4))

            additions += 1

        qx, qy, _, _ = add_points_r(a, q, q)
        q = (round(qx, 4), round(qy, 4))
        
        n //= 2

        multiplication_steps.append((step, n, q, r))

    multiplications = len(multiplication_steps) - 1

    return ((p, r), multiplication_steps, additions, multiplications)


def load_data_multiplication_r(points):
    #data for the table 
    points_names = ['P', 'R']

	#adding the data to the table
    data = {}
    for i in range(len(points_names)):
        data[points_names[i]] = points[i]
        
    return data


def draw_image_multiplication_r(a, b, points, n):
    #data for the table 
    points_names = ['P', 'R = ' + str(n) + 'P']

    #list of all coordinates
    coordinates = []
    
    for point in points:
        coordinates.append(point[0])
        coordinates.append(point[1])

    minimum = min(coordinates)

    if minimum < 0:
        minimum = abs(minimum)

    maximum = max(coordinates)

    #we determine the scale of the graph based on the max abs point
    scale = max(minimum, maximum) * 1.5

    #drawing the curve
    y, x = np.ogrid[-scale:scale:100j, -scale:scale:100j]
    plt.contour(x.ravel(), y.ravel(), y**2 - x**3 - x * a - b, [0], colors='black')

    #drawing the points
    point = points[0]
    plt.plot(point[0], point[1], 'bo')
    plt.text(point[0], point[1], '  ' + points_names[0])

    result = points[-1]
    plt.plot(result[0], result[1], 'bo')
    plt.text(result[0], result[1], '  ' + points_names[1])

    plt.grid()

    sign_a = ''
    if a >= 0:
        sign_a = '+'
		
    sign_b = ''
    if b >= 0:
        sign_b = '+'

    plt.title(f'Elliptic Curve  Y^2 = X^3 {sign_a}{a:.2f}X {sign_b}{b:.2f}')
    plt.savefig('static/images/elliptic_curve_multiplication_r.png')
