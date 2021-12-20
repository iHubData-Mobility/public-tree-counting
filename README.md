# public-tree-counting
Soure code for the paper: 

Arpit Bahety, Rohit Saluja, Ravi Kiran Sarvadevabhatla, Anbumani Subramanian and C.V. Jawahar "Automatic Quantification and Visualization of Street Trees." In Proceedings of 12th Indian Conference on Computer Vision, Graphics and Image Processing (ICVGIP’21), Chetan Arora, Parag Chaudhuri,and Subhransu Maji (Eds.). ACM, New York, NY, USA, Article 90. [https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2021/Automatic_tree.pdf]

## Presentation

| ![Presentation](https://media.githubusercontent.com/media/iHubData-Mobility/public-tree-counting/main/demo/Presentation.mp4) |

## Demo videos of tree detection and counting results

| ![Demo 1](https://github.com/iHubData-Mobility/public-tree-counting/blob/main/demo/demo1.gif) |  ![Demo 2](https://github.com/iHubData-Mobility/public-tree-counting/blob/main/demo/demo2.gif) |
|---|---|

## How to run the code (With visualization) 
#### Input videos will need a GPS metadata file i.e. corresponding .gpx file. Please put the video and its .gpx file in the same folder

1. Clone the repo. cd into the repo
2. Create a virtual environement and run requirements.txt
3. `python preprocess.py  --video-path {path of your video file} --gpx-filename {gpx filename} --segment-duration {duration of video segments in seconds}`\
Example: `python preprocess.py --video-path ~/Desktop/GH017798.mp4 --gpx-filename GH017798.gpx --segment-duration 180` \
The output of this command will be: 

![alt text](https://github.com/CVIT-Mobility/tree-counting/blob/main/readme-images/1.png?raw=true)

4. `python run_inference.py --path {path of the folder created in step 3}` \
Example: `python run_inference.py --path ~/Desktop/GH017798/` 
5. `python create_gps_points.py --path {path of the folder created in step 3}` \
Example: `python create_gps_points.py --path ~/Desktop/GH017798/` 
6. To generate the Category Map: `python create_map.py`

#### To generate the Kernel Density Ranking map (Density Map)
Here we don't need to divide the full video into smaller segments as we don't care about color coding every segment, but we just need to store the counted tree's GPS locations. (As of now we need to separately perform the Density Map generation due to inefficient implementation. This can be improved later). To Note: you need the "points.txt" file for this step which is generated in step 3 in the previous section. 

1. Comment out the following line in detect.py: print(text, file=open('tree_count.txt', "a+"))
2. `python detect.py --source {path of your video file} --weights runs/train/exp7/weights/best.pt` \
Example: `python preprocess.py --source ~/Desktop/GH017798.mp4 --weights runs/train/exp7/weights/best.pt` \
This will give a file as an output - "tree_gps.txt". Copy and paste this file in the folder (for our example): ~/Desktop/GH017798/ 
3. `python preprocess_kdr.py --path {path to the folder}` \
Example: `python preprocess_kdr.py --path ~/Desktop/GH017798/` \ 
This will give a file as an output - "tree_density.txt"
4. Open R studio and run DR_demo.R

## Tree detection results

#### The final model used by us is YOLOv5l

| Model | AP@50 | 
| ------------- | ------------- | 
| YOLOv5s  | 79.29%  | 
| Faster RCNN  | 81.09%  |
| YOLOv4 | 82.50%  |
| **YOLOv5l**  | **83.74%**  |


## Category map

![alt text](https://github.com/CVIT-Mobility/tree-counting/blob/main/readme-images/category_map_results.png?raw=true)

## Density map

![alt text](https://github.com/CVIT-Mobility/tree-counting/blob/main/readme-images/density_map_results.png?raw=true)
