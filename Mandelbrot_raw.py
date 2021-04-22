import numpy as np
MAX_ITERATION = 100

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITERATION:
        z = z**2 + c
        n+=1
    return n

if __name__ == "__main__":
    for x in np.arange(-2, 2, 0.35):
        for y in np.arange(-2, 2, 0.4):
            c = complex(x/10 , y/10 )

            print(c, mandelbrot(c))