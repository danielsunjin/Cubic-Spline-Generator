import numpy as np
import matplotlib.pyplot as plt
import random
import time

#curve to be approximated
def curve(x):
    return np.cos(x)

#conditions for approximation
bounds = (-4,4)
pts = 11 #number of points on the curve to be used for approximation

#calculate step size & generate interpolating points
step = (bounds[1] - bounds[0])/(pts-1)
points = [(bounds[0]+i*step,curve(bounds[0]+i*step)) for i in range(pts)]

#start time
t = time.time()

#process of creating cubic spline
#connect each subsequent pair of points with a cubic polynomial, ensuring that
#the first and second derivatives of the polynomials on either side of a point
#at the point are equal to each other to create a smooth interpolation curve.
#Set the derivatives to 0 for the polynomials at the end points. 
points.sort()

N = 4*(len(points)-1)

A = []
b = []

for i in range(1,len(points)):
    n = i-1
    x1,y1 = points[i-1][0],points[i-1][1]
    A.append((n*4)*[0] + [x1**3,x1**2,x1,1] + (N-4-n*4)*[0])
    b.append(y1)
    x2,y2 = points[i][0],points[i][1]
    A.append((n*4)*[0] + [x2**3,x2**2,x2,1] + (N-4-n*4)*[0])
    b.append(y2)

for i in range(1,len(points)-1):
    n = i-1
    x = points[i][0]
    A.append((n*4)*[0] + [3*x**2,2*x,1,0] + [-3*x**2,-2*x,-1,0] + (N-8-n*4)*[0])
    b.append(0)
    A.append((n*4)*[0] + [6*x,2,0,0] + [-6*x,-2,0,0] + (N-8-n*4)*[0])
    b.append(0)

xi = points[0][0]
A.append([6*xi,2,0,0] + (N-4)*[0])
b.append(0)

xf = points[-1][0]
A.append((N-4)*[0] + [6*xf,2,0,0])
b.append(0)

A = np.asarray(A, dtype=np.float32)
b = np.asarray(b, dtype=np.float32)

vars = np.linalg.solve(A, b)

x_list = [i[0] for i in points]
y_list = [i[1] for i in points]

x_inter = []
y_inter = []

for i in range(0,N,4):
    p = i//4
    numb = int(np.ceil(abs(x_list[p+1] - x_list[p])))
    x_points = np.linspace(x_list[p], x_list[p+1], num = numb*50).tolist()
    def f(x):
        return vars[i]*x**3 + vars[i+1]*x**2 + vars[i+2]*x + vars[i+3]
    y_points = [f(i) for i in x_points]
    x_inter += x_points
    y_inter += y_points

#end time
print(time.time() - t)

#graph curve
y_curve = [curve(i) for i in x_inter]
plt.plot(x_inter,y_curve,'g')
plt.title('Curve to be Approximated')
plt.show()

#graph actual curve with interpolating points and spline cuve
plt.scatter(x_list,y_list, label = 'Interpolating Points')
plt.plot(x_inter,y_curve,'g', label = 'Curve')
plt.plot(x_inter,y_inter,'r', label = 'Cubic Spline')
plt.title('Interpolating Points, Curve to be Approximated, and Cubic Spline')
plt.legend()
plt.show()

#graph error
error = [y_curve[i] - y_inter[i] for i in range(len(x_inter))]
plt.plot(x_inter,error,'c')
plt.title('Residuals of Cubic Spline Approximation (Error)')
plt.show()
