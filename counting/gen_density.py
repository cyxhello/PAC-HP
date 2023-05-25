import json
import h5py
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter 
import numpy as np
from matplotlib import cm as CM
import os


def gen_density(img_path):
    

    json_path = img_path.replace(".png", ".json")
    gt_data = json.load(open(json_path, 'r'))["roilist"]

    img = plt.imread(img_path)
    k = np.zeros((img.shape[0], img.shape[1]))

    
    for node in gt_data:
        x = node["path"]["x"]
        y = node["path"]["y"]

        if len(x) > 1:
            real_x = sum(x) / len(x)
            real_y = sum(y) / len(y)
            k[int(real_y), int(real_x)] = 1
        else:
            k[int(y[0]), int(x[0])] = 1

        
    # print(len(k))
    k = gaussian_filter(k, 15)  
    # print(len(k))
    
    with h5py.File(img_path.replace(".png", ".h5").replace("images", "ground_truth"), "w") as fh:
        fh['density'] = k
    
    plt.clf()
    plt.imshow(k, cmap=CM.jet)
    plt.savefig(img_path.replace("images", "density"))
    



if __name__ == "__main__":
    filepath = os.listdir("dataset/images/")
    for p in filepath:
        if p.find(".png") != -1 :
            gen_density("dataset/images/" + p)

    