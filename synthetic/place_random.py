import os.path
from PIL import Image
import sys
# import torchvision.transforms as transforms
import json
import cv2
import numpy as np
import random
from poisson import *

def cut_image(image, patch_num):
    width, height = 1024, 1024 
    item_width = int(width / patch_num)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0 ,patch_num)  :  
        for j in range(0 ,patch_num):
            center = (j *item_width + 32 , i *item_width + 32)
            # box = ( j *item_width , i *item_width ,( j +1 ) *item_width ,( i +1 ) *item_width)
            box_list.append(center)

    return box_list




if __name__ == '__main__':
    candidate = os.listdir('single/')
    total = 0
    lengths = 0
    for i in range(5):
        index = str(i)
        with open('images/' + index+'.json') as f:
            centers = []
            count_list = [0] * 256
            data = json.load(f)
            # os.mkdir(index)
            image = Image.open('images/' + index + '.png')
            box_list = cut_image(image, patch_num=16)
            roilist = data['roilist']
            roilist_replace = roilist


            for item in roilist:
                path = item['path']
                idx = item['id']
                x = path['x'][0]
                y = path['y'][0]
            
                row = y // 64
                col = x // 64
                pos = row * 16 + col
                pos = int(pos)
                count_list[pos] += 1
        
            for i in range(256):
                if count_list[i] == 1:

                    # print(count_list[i])
                    # centers.append(box_list[i])
                    list = range(box_list[i][0]-22, box_list[i][0]+22)
                    px = random.sample(list, 4)
                    list = range(box_list[i][1]-22, box_list[i][1]+22)
                    py = random.sample(list, 4)
                    for j in range(len(px)):
                        centers.append((px[j], py[j]))
                         
            nums = len(centers)
            
            obj_list = random.sample(candidate, nums)
            tmp = cv2.imread('images/' + index + '.png')
            for i in range(nums):
                item_replace = {}
                item_replace['method'] = 'spot'
                item_replace['radius'] = 2.546473134708429
                item_replace['path'] = {}
                item_replace['id'] = str(random.randint(100000, 1000000000))
                item_replace['path']['x'] = [centers[i][0]]
                item_replace['path']['y'] = [centers[i][1]]
                roilist_replace.append(item_replace)
                
                # print('center:', centers[i])
                im = tmp
                obj = cv2.imread('single/' + obj_list[i])
                obj = cv2.resize(obj, (18, 18))
                mask = 255 * np.ones(obj.shape, obj.dtype)
                width, height, channels = im.shape
                
                # tmp = cv2.seamlessClone(obj, im, mask, centers[i], cv2.MIXED_CLONE)   # possion blending
                
                offset = [centers[i][0]-9, centers[i][1]-9]
                poissonOperator = Poisson(offset, obj, mask, im)
                tmp, naive_output = poissonOperator.process("merge33")   # improving possion blending
   
                
            # print(roilist_replace)
            data['roilist'] = roilist_replace
            with open( "single_random_4/" + str(index) + "_" + str(nums) + ".json", "w") as f:
                json.dump(data, f)
            cv2.imwrite("single_random_4/" + str(index) + "_" + str(nums) + ".png", tmp)
