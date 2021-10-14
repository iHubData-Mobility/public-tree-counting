import os, sys
import shutil
import pickle
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, help='path of the folder created in step 3')
opt = parser.parse_args()
path = opt.path

tree_gps_points = []
max_len = 0
with open(path + 'tree_gps.txt', 'rb') as file:
	tree_gps_list = pickle.load(file)

with open(path + 'points.txt', 'rb') as file2:
	gps_points = pickle.load(file2)
	max_len = len(gps_points)
for index in tree_gps_list:
	if index < max_len:
		tree_gps_points.append(gps_points[index])

df = pd.DataFrame(tree_gps_points, columns=['latitude', 'longitude'])
if os.path.exists('tree_density.csv'):
	df.to_csv('tree_density.csv', mode='a', header=False)
else:
	df.to_csv('tree_density.csv', mode='a')

