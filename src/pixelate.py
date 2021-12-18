from PIL import Image, ImageDraw
from typing import Tuple, List
from random import  randint
from math import gcd, floor
from statistics import mean

WIDTH = 1920
HEIGHT = 1080

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PATH_IN = 'in.jpg'
PATH_OUT = 'pixelate.jpg'

def main():
    print('Hello World!')

    new_image = Image.open(PATH_IN)

    sized_image: Image = transform_size(new_image)

    canvas = ImageDraw.Draw(sized_image)

    mesh: List[Tuple[int, int, int]] = generate_mesh()

    for poly in mesh:
        canvas.polygon(poly, fill=average_color(sized_image, poly, 2))

    sized_image.save(PATH_OUT)

def generate_mesh(detail: int = 5) -> List[Tuple[int, int, int]]:
    poly_list: List[Tuple[int]] = []

    x: float = 0.0
    y: float = 0.0
    max_size: float = gcd(WIDTH, HEIGHT)
    size: float = max_size / detail

    while y < HEIGHT:
        y_next: float = y+size
        while x < WIDTH:
            x_next: float = x+size
            poly_list.append((
                (x, y),
                (x_next, y),
                (x_next, y_next),
                (x, y_next)
            ))
            x += size
        x = 0
        y += size

    return poly_list


def transform_size(image, new_width: int=WIDTH, new_height: int=HEIGHT) -> Image:
    new_size: Tuple = (new_width, new_height)

    return image.resize(new_size)

def randomColor() -> Tuple[int, int, int]:
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def average_color(img: Image, square: Tuple, step: int=1) -> Tuple[int, int, int]:
    rgb_img = img.convert('RGB')
    R: List[int] = []
    G: List[int] = []
    B: List[int] = []
    x_start: int = floor(square[0][0])
    x_end: int = floor(square[2][0])
    y_start: int = floor(square[0][1])
    y_end: int = floor(square[2][1])

    for y in range(y_start, y_end, step):
        for x in range(x_start, x_end, step):
            rp, gp, bp = rgb_img.getpixel((x, y))
            R.append(rp)
            G.append(gp)
            B.append(bp)

    return floor(mean(R)), floor(mean(G)), floor(mean(B))

if __name__ == '__main__':
    main()