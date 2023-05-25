import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os



def max_filtering(N, I_temp):
    wall = np.full((I_temp.shape[0]+(N//2)*2, I_temp.shape[1]+(N//2)*2), -1)
    wall[(N//2):wall.shape[0]-(N//2), (N//2):wall.shape[1]-(N//2)] = I_temp.copy()
    temp = np.full((I_temp.shape[0]+(N//2)*2, I_temp.shape[1]+(N//2)*2), -1)
    for y in range(0,wall.shape[0]):
        for x in range(0,wall.shape[1]):
            if wall[y,x]!=-1:
                window = wall[y-(N//2):y+(N//2)+1,x-(N//2):x+(N//2)+1]
                num = np.amax(window)
                temp[y,x] = num
    A = temp[(N//2):wall.shape[0]-(N//2), (N//2):wall.shape[1]-(N//2)].copy()
    return A


def min_filtering(N, A):
    wall_min = np.full((A.shape[0]+(N//2)*2, A.shape[1]+(N//2)*2), 300)
    wall_min[(N//2):wall_min.shape[0]-(N//2), (N//2):wall_min.shape[1]-(N//2)] = A.copy()
    temp_min = np.full((A.shape[0]+(N//2)*2, A.shape[1]+(N//2)*2), 300)
    for y in range(0,wall_min.shape[0]):
        for x in range(0,wall_min.shape[1]):
            if wall_min[y,x]!=300:
                window_min = wall_min[y-(N//2):y+(N//2)+1,x-(N//2):x+(N//2)+1]
                num_min = np.amin(window_min)
                temp_min[y,x] = num_min
    B = temp_min[(N//2):wall_min.shape[0]-(N//2), (N//2):wall_min.shape[1]-(N//2)].copy()
    return B


#B is the filtered image and I is the original image
def background_subtraction(I, B):
    O = I - B
    norm_img = cv2.normalize(O, None, 0,255, norm_type=cv2.NORM_MINMAX)
    return norm_img

def min_max_filtering(M, N, I):
    if M == 0:
        #max_filtering
        A = max_filtering(N, I)
        #min_filtering
        B = min_filtering(N, A)
        #subtraction
        normalised_img = background_subtraction(I, B)
    elif M == 1:
        #min_filtering
        A = min_filtering(N, I)
        #max_filtering
        B = max_filtering(N, A)
        #subtraction
        normalised_img = background_subtraction(I, B)
    return normalised_img



if __name__ == '__main__':
    path = 'size64/6_10/'
    file_name_list = os.listdir(path)

    for img_path in file_name_list:
        P = cv2.imread(path+img_path, 1)
        b, g, r = cv2.split(P)
        b_O_P = min_max_filtering(M=0, N=20, I=b)
        g_O_P = min_max_filtering(M=0, N=20, I=g)
        r_O_P = min_max_filtering(M=0, N=20, I=r)

        O_P = cv2.merge([b_O_P, g_O_P, r_O_P])
        # O_P = min_max_filtering(M=0, N=3, I=P)
        cv2.imwrite('out.png', O_P)


        # #替换颜色
        img = Image.open('out.png')
        ori_img = Image.open(path + img_path)
        width, height = 64, 64
        for i in range(0, width):  # 遍历所有长度的点
            for j in range(0, height):  # 遍历所有宽度的点
                data = (img.getpixel((i, j)))  # 打印该图片的所有点
                # print(data)  # 打印每个像素点的颜色RGBA的值(r,g,b,alpha)
                # print(data[0])  # 打印RGBA的r值
                if data[0] >= 150 and data[1] >= 150 and data[2] >= 150:  # RGBA的r值大于170，并且g值大于170,并且b值大于170
                    # img.putpixel((i, j), (255, 255, 255, 1))  # 则这些像素点的颜色改成透明色
                    ori_img.putpixel((i, j), (255, 255, 255, 0))
        # img = img.convert("RGB")  # 把图片强制转成RGB
        # img.save('clear.jpg')  # 保存修改像素点后的图片
        ori_img.save('size64_clear/6_10/clear_' + img_path)

    