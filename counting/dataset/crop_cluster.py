import json
import os 
import cv2
# import kmeans
import numpy as np
# import matplotlib.pyplot as plt
from math import sqrt

def crop(image, filename, x, y):
    img = cv2.imread('images/'+index+'.png')
    x = int(x)
    y = int(y)
    x0 = x - 32 if x-32 >0 else 0
    x1 = x + 32 if x+32 < 1024 else 1024
    y0 = y - 32 if y-32 >0 else 0
    y1 = y + 32 if y+32 < 1024 else 1024
    
    crop_img = image[y0:y1, x0:x1]
    cv2.imwrite(filename, crop_img)
    

# def crop_cluster(x, y):
#     dataSet=[]
#     # fileIn=open('testSet.txt')
#     for i in range(len(x)):    
#         # lineArr=line.strip().split('\t')
#         dataSet.append([float(x[i]),float(y[i])])
#     dataSet=np.mat(dataSet)
#     k=4
#     centroids,clusterAssment=kmeanss(dataSet,k)


        # crop_cluster(data)
            
            # filename = index + '_' + idx + '.png'
            # filepath = 
            # crop(img, filename, x, y)
            
        
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

size = 30 ##取值范围

##计算欧式距离
def distEuclid(x,y):
    # sqrt(sum(pow(vec2-vec1,2)))
    # return np.sqrt(np.sum((x-y)**2))
    return sqrt(sum(pow(x-y,2)))

##随机产生n个dim维度的数据 (这里为了展示结果 dim取2或者3)
def genDataset(n,dim):
    data = []
    while len(data)<n:
        p = np.around(np.random.rand(dim)*size,decimals=2)
        data.append(p)
    return data

## 初始化簇中心点 一开始随机从样本中选择k个 当做各类簇的中心
def initCentroid(data,k):
    num,dim = data.shape
    centpoint = np.zeros((k,dim))
    l = [x for x in range(num)]
    np.random.shuffle(l)
    for i in range(k):
        index = int(l[i])
        centpoint[i] = data[index]
    return centpoint

##进行KMeans分类
def KMeans(data,k):
    ##样本个数
    num = np.shape(data)[0]
    
    ##记录各样本 簇信息 0:属于哪个簇 1:距离该簇中心点距离 
    cluster = np.zeros((num,2))
    cluster[:,0]=-1
    
    ##记录是否有样本改变簇分类
    change = True
    ##初始化各簇中心点
    cp = initCentroid(data,k)

    while change:
        change = False
        
        ##遍历每一个样本
        for i in range(num):
            minDist = 9999.9
            minIndex = -1
            
            ##计算该样本距离每一个簇中心点的距离 找到距离最近的中心点
            for j in range(k):
                # print('cp[j]', cp[j])
                # print('data[i]', data[i])
                
                dis = distEuclid(cp[j],data[i])
                if dis < minDist:
                    minDist = dis
                    minIndex = j
            
            ##如果找到的簇中心点非当前簇 则改变该样本的簇分类
            if cluster[i,0]!=minIndex:
                change = True
                cluster[i,:] = minIndex,minDist
        
        ## 根据样本重新分类  计算新的簇中心点
        for j in range(k):
            pointincluster = data[[x for x in range(num) if cluster[x,0]==j]]
            cp[j] = np.mean(pointincluster,axis=0)
    
    print("finish!")
    return cp,cluster

##展示结果  各类簇使用不同的颜色  中心点使用X表示
def Show(data,k,cp,cluster):
    num,dim = data.shape
    color = ['r','g','b','c','y','m','k']
    ##二维图
    if dim==2:
        for i in range(num):
            mark = int(cluster[i,0])
            plt.plot(data[i,0],data[i,1],color[mark]+'o')
            
        for i in range(k):
            plt.plot(cp[i,0],cp[i,1],color[i]+'x')
    ##三维图
    elif dim==3:
        ax = plt.subplot(111,projection ='3d')
        for i in range(num):
            mark = int(cluster[i,0])
            ax.scatter(data[i,0],data[i,1],data[i,2],c=color[mark])
            
        for i in range(k):
            ax.scatter(cp[i,0],cp[i,1],cp[i,2],c=color[i],marker='x')
        
    plt.show()


num = 10 ##点个数    
k=5 ##分类个数
# data = np.array(genDataset(num,2))
# print(data)
# cp,cluster = KMeans(data,k)
# print('cp',cp)
# print('cluster',cluster)

# Show(data,k,cp,cluster)
for i in range(1,2):
    index = str(i)
    with open('images/'+index+'.json') as f:
        data = json.load(f)
        # os.mkdir(index)
        img = cv2.imread('images/'+index+'.png')
        roilist = data['roilist']
        # x_list = []
        # y_list = []
        data = []
        for item in roilist:
            path = item['path']
            idx = item['id']
            x = path['x'][0]
            y = path['y'][0]
            data.append([x,y])
        data = np.array(data)
        print(len(data))
        cp,cluster = KMeans(data,k)
        Show(data,k,cp,cluster)
        print('cp',cp)
        for i in range(k):
            filename = index + '_' + str(i) + '.png'
            crop(img, filename, data[i][0], data[i][1])
        
