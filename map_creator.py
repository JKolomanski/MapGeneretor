import random
from PIL import Image


# noinspection PyUnresolvedReferences
def create_map_from_noise(input_bytes, height, width):
    input_image = Image.frombytes(data=input_bytes, mode='L', size=(height, width))
    input_image = input_image.convert("RGB")
    pixel = input_image.load()

    # Assign correct color values to each pixel
    offset = random.randint(0, 3)

    for row in range(input_image.size[0]):
        for column in range(input_image.size[1]):

            if pixel[row, column][0] >= 100:
                pixel[row, column] = (0 + random.randint(-offset, offset)
                                      , 148 + random.randint(-offset, offset)
                                      , 256 + random.randint(-offset, offset))
            elif pixel[row, column][0] < 90:
                pixel[row, column] = (61 + random.randint(-offset, offset)
                                      , 147 + random.randint(-offset, offset)
                                      , 25 + random.randint(-offset, offset))
            else:
                pixel[row, column] = (214 + random.randint(-offset, offset)
                                      , 190 + random.randint(-offset, offset)
                                      , 83 + random.randint(-offset, offset))

    return input_image