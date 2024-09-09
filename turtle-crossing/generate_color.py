from random import randint


def generate_color():
    min_shade = 0
    max_shade = 255

    r = randint(min_shade, max_shade)
    g = randint(min_shade, max_shade)
    b = randint(min_shade, max_shade)

    return (r, g, b)
