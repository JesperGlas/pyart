from PIL import Image, ImageDraw
from typing import Tuple
from random import  randint

WIDTH = 1920
HEIGHT = 1080

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PATH_OUT = 'polyart.png'

def main():
    print('Hello World!')

    new_image = genereate()

    new_image.save(PATH_OUT)


def genereate(size: Tuple=(WIDTH, HEIGHT)) -> Image:
    image = Image.new('RGB', size=size, color=randomColor())

    canvas = ImageDraw.Draw(image)

    multyRandPoly(canvas, min=3, max=10)

    return image

def multyRandPoly(canvas: ImageDraw.ImageDraw, min: int=1, max: int=3) -> None:
    for n in range(min, max):
        randPoly(canvas, corners=randint(3, randint(3, 8)))

def randPoly(canvas: ImageDraw.ImageDraw, corners: int=3) -> None:
    xy = [randxy() for n in range(0, corners)]
    canvas.polygon(xy, fill=randomColor())

def randomColor() -> Tuple[int, int, int]:
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def randxy(bounds: Tuple=(WIDTH, HEIGHT)) -> Tuple[int, int]:
    x_bound = bounds[0]
    y_bound = bounds[1]
    return (randint(0, x_bound), randint(0, y_bound))

if __name__ == '__main__':
    main()