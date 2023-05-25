import torch

# PSNR
from piqa import PSNR

x = torch.rand(5, 3, 256, 256)
y = torch.rand(5, 3, 256, 256)

psnr = PSNR()
l = psnr(x, y)

# SSIM
from piqa import SSIM

x = torch.rand(5, 3, 256, 256, requires_grad=True).cuda()
y = torch.rand(5, 3, 256, 256).cuda()

ssim = SSIM().cuda()
l = 1 - ssim(x, y)
l.backward()
