
import sys
sys.path.append("..")
from PIL import Image
import numpy as np
from bilateral.main import bilateral_filter

img = Image.open('../data/lena.png').convert('L')
img = np.array(img)

noise = np.random.normal(0, 10, size=img.shape)
noisy_img = (img + noise).astype(np.uint8)

denoised_img = bilateral_filter(noisy_img, 2, 5)
res = np.hstack([noisy_img, denoised_img, img])

Image.fromarray(res).save('test.png')
