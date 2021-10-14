import pandas as pd
import pickle
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, help='path of the folder created in step 3')
opt = parser.parse_args()
#path = '/users/arpit.bahety/trees_test_videos/GH017796/'
path = opt.path

if os.path.exists('gps_points.txt'):
    with open('gps_points.txt', 'rb') as file:
        gps_list = pickle.load(file)
        print("Loaded: ", len(gps_list))
        os.remove('gps_points.txt')
else:
    gps_list = []
    print("Creating new list")

with open(path + 'dict.txt', 'rb') as file:
    filename_points_dict = pickle.load(file)
    print(filename_points_dict.keys())
    file1 = open('tree_count.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        filename, tree_count = line.split()
        filename = filename + '.mp4'
        print(filename, tree_count)
        if filename in filename_points_dict.keys():
            points = filename_points_dict[filename]
            gps_list.append((tree_count, points))
    with open('gps_points.txt', 'wb') as file:
        pickle.dump(gps_list, file)
