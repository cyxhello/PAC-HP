import os.path
from PIL import Image
import sys
import torchvision.transforms as transforms
import json
import cv2

def cut_image(image, patch_num):
    width, height = 1024, 1024 
    item_width = int(width / patch_num)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0 ,patch_num)  :  
        for j in range(0 ,patch_num):
            box = ( j *item_width , i *item_width ,( j +1 ) *item_width ,( i +1 ) *item_width)
            box_list.append(box)
    # print(box_list)
    return box_list




def save_images(image_list, save_path):
    index = 1
    for image in image_list:
        image.save(save_path + '_' + str(index) + '.png')
        index += 1

if __name__ == '__main__':

    
    for i in range(500):
        index = str(i)
        with open('images/'+index+'.json') as f:
            crop_list = []
            count_list = [0] * 256
            data = json.load(f)
            # os.mkdir(index)
            image = Image.open('images/'+index+'.png')
            box_list = cut_image(image, patch_num=16)
            roilist = data['roilist']
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
                if count_list[i] >= 2 and count_list[i] <= 5:
                    # print(count_list[i])
                    crop_list.append(box_list[i])
                
            # print(crop_list)
            image_list = [image.crop(box) for box in crop_list]  #Image.crop(left, up, right, below)
            save_path = 'size64/1/' + index
            save_images(image_list,save_path)
    