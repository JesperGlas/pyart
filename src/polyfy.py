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
PATH_OUT = 'polyfy.jpg'

def main():
    print('Hello World!')

    new_image = Image.open(PATH_IN)

    sized_image: Image = transform_size(new_image)

    canvas = ImageDraw.Draw(sized_image)

    points: List[List[Point]] = generate_points()

    print(f'{points[0][0]}, {points[0][1]}, {points[1][0]}, {points[1][1]}')

    p: Tuple = (points[0][0], points[0][1], points[1][0], points[1][1])

    s = Square(p)

    print(s.get())

    canvas.polygon(s.get(), fill=average_color(sized_image, s.get(), 2))

    #mesh: List[Tuple[int, int, int]] = generate_mesh()

    #for poly in mesh:
    #    canvas.polygon(poly, fill=average_color(sized_image, poly, 2))

    sized_image.save(PATH_OUT)

def generate_points(detail: int = 2) -> List[List]:
    mtr: List[Point] = []
    x: int = 0
    y: int = 0
    max_size: float = gcd(WIDTH, HEIGHT)
    size: float = max_size // detail

    while y <= HEIGHT:
        row = []
        while x <= WIDTH:
            row.append(Point(x, y))
            x += size
        mtr.append(row)
        x = 0
        y += size

    return mtr

def generate_square_mesh() -> List[List]:
    return None


def generate_mesh(detail: int = 2) -> List[Tuple[int, int, int]]:
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
    R: List[int] = [0]
    G: List[int] = [0]
    B: List[int] = [0]

    return floor(mean(R)), floor(mean(G)), floor(mean(B))

class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def set(self, xy: Tuple[int, int]) -> None:
        self.x, self.y = xy

    def get(self) -> Tuple[int, int]:
        return self.x, self.y

    def set_x(self, x: int) -> None:
        self.x = x

    def set_y(self, y: int) -> None:
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def __repr__(self):
        return f'{self.y, self.x}'

class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1: Point = p1
        self.p2: Point = p2
        self.p3: Point = p3

    def get(self) -> Tuple[Point, Point, Point]:
        return self.p1, self.p2, self.p3

class Square:
    def __init__(self, corners: Tuple[Point, Point, Point, Point]):
        self.tr, self.tl, self.bl, self.br = corners

    def get(self) -> Tuple[Point, Point, Point, Point]:
        return self.tr.get(), self.br.get(), self.tl.get(), self.bl.get()

    def split(self) -> List[Triangle]:
        return None

if __name__ == '__main__':
    main()