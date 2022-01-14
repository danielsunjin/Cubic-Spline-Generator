# Cubic Spline Generator
This repository contains my custom code for generating [cubic splines](https://mathworld.wolfram.com/CubicSpline.html#:~:text=A%20cubic%20spline%20is%20a,equations.) in Python. Cubic spline interpolation is used to approximate curves by connecting a finite set of points on the curve with cubic polynomials. The code example in this repository uses 11 evenly spaced points along the curve of the function *f(x) = cos(x)* within the range -4 to 4 to approximate the curve in that range. This code was utilized in the Qiskit Community Summer Jam 2020 - North Carolina hakathon that I participated in as a part of the [NCSSM Unicorns](https://github.com/code1word/nc-qc-hackathon-summer-2020) team while at the North Carolina School of Science and Mathematics. 

Python libraries required to run the code:
- numpy
- matplotlib

![Curve to Approximate (f(x) = cos(x))](https://github.com/danielsunjin/Cubic-Spline-Generator/blob/main/curve_to_approximate.png)

![Cubic Spline Approximation](https://github.com/danielsunjin/Cubic-Spline-Generator/blob/main/cubic_spline_approximation.png)

![Approximation Error](https://github.com/danielsunjin/Cubic-Spline-Generator/blob/main/approximation_error.png)
