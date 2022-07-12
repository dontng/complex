'''
@Author: djology.w
@Date: 2022/7/12 1:14
@Desc: 
'''

from numpy import *
import matplotlib.pyplot as plt

r = 1
Y = [r * exp(1j * theta) for theta in linspace(0, 2 * pi, 200)]
Y = array(Y)
plt.plot(real(Y), imag(Y), 'r')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')


def argand(complex_number):
    y = complex_number
    x1, y1 = [0, real(y)], [0, imag(y)]
    x2, y2 = [real(y), real(y)], [0, imag(y)]

    plt.plot(x1, y1, 'r')
    plt.plot(x2, y2, 'r')

    plt.plot(real(y), imag(y), 'bo')


[argand(r * exp(1j * theta)) for theta in linspace(0, 2 * pi, 100)]
plt.show()
