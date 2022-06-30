import opensimplex
from PIL import Image
import opensimplex as simplex


def generate_noise(width, height, feature_size, seed):
    if seed == "":
        opensimplex.random_seed()
    else:
        opensimplex.seed(int(seed))

    im = Image.new('L', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            value = simplex.noise3(x / feature_size, y / feature_size, 0.0)
            color = int((value + 1) * 128)
            im.putpixel((x, y), color)
    return im