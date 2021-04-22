from PIL import Image as im
import numpy as np

MAX_ITERATION = 100


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) < 2 and n < MAX_ITERATION:
        z = z**2 + c
        n += 1
    return n


HEIGHT = 768    # Replace with your screen resolution
WIDTH = 1368

image = im.new('RGB', (WIDTH, HEIGHT))  # Change mode to change the color of mandelbrot set
pix = image.load()

for x in np.arange(-2, 2, 4.0/WIDTH):   # 4.0/WIDTH = 0.002923 = number of steps
    for y in np.arange(-2, 2, 4.0/HEIGHT):
        pix[WIDTH*(x+2)/4.0, HEIGHT*(y+2)/4.0] = mandelbrot(c = complex(x, y))  # pix[684, 384] = c (Will keep changing depending on iteration)


image.show()

# Optional
# image = image.save("Mandelbrot.png", "PNG")
