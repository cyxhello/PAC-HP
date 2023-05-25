import cv2
import numpy as np

from poisson import *

if __name__ == '__main__':
    offset = [350, 780]
#    offset = [140, 150]
    # offset = [150, 150]
    srcimg = cv2.imread("154_1.png")
    srcmask = cv2.imread("white.png")
    dstimg = cv2.imread("1.png")
    # dstimg = None
    poissonOperator = Poisson(offset, srcimg, srcmask, dstimg)
    output, naive_output = poissonOperator.process("merge33")
    
    # output = poissonOperator.single_pic_process("illu")
    cv2.imwrite("result.jpg", output)
    # cv2.imwrite("result1.jpg", output1)
    
    mixed_clone = cv2.seamlessClone(srcimg, dstimg, srcmask, (812, 382), cv2.MIXED_CLONE)
    normal_clone = cv2.seamlessClone(srcimg, dstimg, srcmask, (812, 382), cv2.NORMAL_CLONE)
    
    
    cv2.imwrite("clone.png", mixed_clone)
    cv2.imwrite("normal_clone.png", normal_clone)
    
