import numpy as np
from PIL import Image, ImageDraw

img = Image.open('../data/town.png').convert('RGB')
np_img = np.array(img)
h, w, _ = np_img.shape

canvas = Image.new('RGB', img.size)
draw = ImageDraw.Draw(canvas)

r = 5

for y in range(h):
    for x in range(w):
        box = (x-r, y-r, x+r, y+r)
        draw.ellipse(box, fill=tuple(np_img[y, x, :]))
canvas.save('test.jpg')