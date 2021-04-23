from PIL import Image as im
import numpy as np
import random

MAX_ITERATION = 100

def mandelbrot_with_dot(c):
    z = 0
    n = 0
    while abs(z) < 2 and n < MAX_ITERATION:
        z = z**2 + c
        n += 1
    return n

HEIGHT = random.randint(100, 1000)          # You can specify as 512 * 512 to get dotted set
WIDTH = random.randint(100, 1000)           # Cut the set into more random pieces
                                            # Sometimes there would be error since its random and incompatible number may throw error.
                                            # Just try again because it's random.

O_HEIGHT = 768   # Replace with your screen resolution
O_WIDTH = 1368

image = im.new('L', (O_WIDTH, O_HEIGHT))  # Change mode to change the color of mandelbrot set
make_image = image.load()

for x in np.arange(-2, 2, 4.0/WIDTH):   # 4.0/WIDTH = 0.002923 = number of steps
    for y in np.arange(-2, 2, 4.0/HEIGHT):
        make_image[O_WIDTH*(x+2)/4.0, O_HEIGHT*(y+2)/4.0] = mandelbrot_with_dot(c = complex(x, y))  # pix[684, 384] = c (Will keep changing depending on iteration)


image.show()
# Optional
image = image.save("Mandelbrot.png", "PNG")

