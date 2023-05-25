import json
import os 
import cv2

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import os
 
def dbscan(coords):
    # columns=['lon','lat']
    # in_df = pd.read_csv(input_file, sep='\t', header=None, names=columns)
    # #print(in_df.head(10))
 
    # #represent GPS points as (lon, lat)
    # coords = in_df.as_matrix(columns=['lon','lat'])
 
    #earth's radius in km
    # kms_per_radian = 6371.0086
    #define epsilon as 0.5 kilometers, converted to radians for use by haversine
    #This uses the 'haversine' formula to calculate the great-circle distance between two points
    # that is, the shortest distance over the earth's surface
    # http://www.movable-type.co.uk/scripts/latlong.html
    epsilon = 16
 
    # radians() Convert angles from degrees to radians
    db = DBSCAN(eps=epsilon, min_samples=5, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    cluster_labels = db.labels_
 
    # get the number of clusters (ignore noisy samples which are given the label -1)
    num_clusters = len(set(cluster_labels) - set([-1]))
 
    print( 'Clustered ' + str(len(coords)) + ' points to ' + str(num_clusters) + ' clusters')
 
 
    # turn the clusters in to a pandas series
    #clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
    #print(clusters)
 
    for n in range(num_clusters):
        #print('Cluster ', n, ' all samples:')
        one_cluster = coords[cluster_labels == n]
        print(one_cluster[:1])
        #clist = one_cluster.tolist()
        #print(clist[0])
 
# def main():
#     path = './datas'
#     filelist = os.listdir(path)
#     for f in filelist:
#         datafile = os.path.join(path,f)
#         print(datafile)
#         dbscan(datafile)
 
 
# if __name__ == '__main__':
#     main()
 

def crop(image, filename, x, y):
    img = cv2.imread('images/'+index+'.png')
    x = int(x)
    y = int(y)
    x0 = x - 10 if x-10 >0 else 0
    x1 = x + 10 if x+10 < 1024 else 1024
    y0 = y - 10 if y-10 >0 else 0
    y1 = y + 10 if y+10 < 1024 else 1024
    
    crop_img = image[y0:y1, x0:x1]
    cv2.imwrite(filename, crop_img)
    

for i in range(859):
    index = str(i)
    with open('images/'+index+'.json') as f:
        data = json.load(f)
        # os.mkdir(index)
        img = cv2.imread('images/'+index+'.png')
        roilist = data['roilist']
        # coordinate = []
        
        for item in roilist:
            path = item['path']
            idx = item['id']
            x = path['x'][0]
            y = path['y'][0]
            # coordinate.append([x,y])
            
            filename = 'crop_images_20/' + index + '_' + str(idx) + '.png'
            # filepath = 
            crop(img, filename, x, y)
        # dbscan(coordinate) 
            
            
            
        
