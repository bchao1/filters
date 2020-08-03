from PIL import Image
from PIL.ImageFilter import GaussianBlur
import numpy as np

img = Image.open('../data/town.png').convert('L')
blurred = img.filter(GaussianBlur(2))


img = np.array(img).astype(np.float64)
blurred = np.array(blurred).astype(np.float64)
residual = img - blurred

residual = np.clip(residual, 0, 255).astype(np.uint8)
print(residual)
Image.fromarray(residual).save('test.png')