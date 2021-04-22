import lpips
from PIL import Image
import os
import torch
import numpy as np

loss_fn_alex = lpips.LPIPS(net='alex') # best forward scores
#loss_fn_vgg = lpips.LPIPS(net='vgg') # closer to "traditional" perceptual loss, when used for optimization

fake = Image.open('imgs/airplanes/n02691156_5181-4_fake_B.png')
real = Image.open('imgs/airplanes/n02691156_5181-4_real_B.png')

fake = 2 * (np.asarray(fake) / 255 - 1)
fake_t = torch.from_numpy(fake)

real = 2 * (np.asarray(real) / 255 - 1)
real_t = torch.from_numpy(real)
print(fake_t)
print(real_t)

#d = loss_fn_alex(fake, real)
#print(d)
