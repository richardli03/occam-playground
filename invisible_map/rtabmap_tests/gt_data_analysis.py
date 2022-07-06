"""
python script to clean data coming from RTABmaps regarding tag locations. Trying to test
if it could be viable as ground truth data.
"""

import json
import os
from turtle import rt
import numpy as np
from scipy.spatial.transform import Rotation as R
import pyrr
import pdb
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

RTABMAP_DATA_PATH = "test_data/poses27.txt"
OUTPUTED_JSON_PATH = "gt_json/gt_robolab_test.json"
PROCESSED_GRAPH_DATA = "processed_graphs/robolab_test.json"

def q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z

def check_data(new_data_entry):
    """
    The file containing all of the checks to ensure the processed data is useable

    Args:
        new_data_entry (list): A list of all necessary data (ID + Translation + POSE)

    Returns:
        Boolean: True if data is good, False if data is bad.
    """
    if len(new_data_entry) != 9:
        print(f"ERROR in {new_data_entry}")
        return False

    # odometry nodes are saved as markers as well, but with a negative ID.
    if float(new_data_entry[1]) < 0:
        print(f"Negative marker {new_data_entry[1]} detected and thrown")
        return False

    return True

def generate_correct_pose(pose):
    """
    The data we get from RTABmap makes every number a string and is in a right-handed coordinate system, as opposed to the
    left-handed coordinate system that IM asks for. This function fixes both of those problems by negating the X axis + turning every number into a float.

    NOTE that RTABmap pose data appears to give z as the gravity axis, but IM uses y as the gravity axis, hence why our list
    for pose is [x, Z, y , etc.] instead of [x, Y, z, etc.]

    Args:
        pose (list): the 7 numbers composing the pose of an object [x,z,y,qx,qy,qz,qw]
    """

    # convert string to float
    pose = [float(number) for number in pose]
    # print(pose)
    # the first number (X) needs to be flipped
    rtabmap_pose = np.array([pose[0],pose[1],pose[2]])
    rtabmap_quat = np.array([pose[3],pose[4],pose[5],pose[6]])
    alignment_quat = [-0.5,0.5,0.5,0.5]
    final_quat = q_mult(rtabmap_quat,alignment_quat)
    # r_matA = R.from_matrix(np.array([[0,0,-1],[0,1,0],[1,0,0]]))
    # r_matB = R.from_matrix(np.array([[1,0,0],[0,0,-1],[0,1,0]]))
    final_pose = pyrr.quaternion.apply_to_vector(alignment_quat, rtabmap_pose)
    
    # pose = [final_pose, final_quat]
    
    
    # final_pose = r_matB.apply(r_matA.apply(rtabmap_pose))
    
    # final_pose = np.dot(rotation_matfinal,rtabmap_pose)
    # final_pose = r_mat.apply(rtabmap_pose)
    for i in range(7):
        if i < 3:
            pose[i] = final_pose[i]
        elif i == 6:
            pose[i] = -final_quat[3]
        else:
            pose[i] = final_quat[i-3]
    # print("break")

    # print(pose)
    return pose

def parse_IM_GT_data(file_path,tag_poses):
    
    # Invisible Map Data
    IM_processed_poses = []
    with open(file_path,"r") as json_file:
        data = json.load(json_file)
        # print(data)
        for item in data["tag_vertices"]:
            IM_processed_poses.append([item["translation"]["x"],item["translation"]["y"],item["translation"]["z"]])
            
            
    # Ground Truth Data
    GT_processed_poses = []
    for pos in tag_poses:
        GT_processed_poses.append(pos["pose"][0:3])
        
    return np.array(IM_processed_poses),np.array(GT_processed_poses)

def plot_IM_GT_data(im,gt):
    
    
    fig = plt.figure()
    ax = plt.axes(projection = "3d")
    # ax.set_box_aspect([20,20,20])
    # fig.add_subplot((111),aspect = "equal", projection = "3d")
    
    ax.plot3D(im[:,0],im[:,1],im[:,2], "-o", c ="red")   
    ax.plot3D(gt[:,0],gt[:,1],gt[:,2], "-o", c ="green")
    ax.set_xlim(-10,10)
    ax.set_xlabel("x")
    ax.set_ylim(-10,10)
    ax.set_ylabel("y")
    ax.set_zlim(-10,10)
    ax.set_zlabel("z")
    ax.legend(["invisible map","ground truth"])
    plt.show()

    
    
    
# initialize empty list of tag poses
tag_poses = []

# Data comes in as a g2o file, change to .txt
if RTABMAP_DATA_PATH[-4:] == ".g2o":
    base = os.path.splitext(RTABMAP_DATA_PATH)[0]
    os.rename(RTABMAP_DATA_PATH, base + ".txt")

RTABMAP_DATA_PATH = RTABMAP_DATA_PATH[:-4] + ".txt"

# Handling data
with open(RTABMAP_DATA_PATH, "r") as f:
    for line in f.readlines():
        new_data_entry = line.split()

        # Right now we only care about handling tags (aka MARKERs)
        if new_data_entry[0] == "MARKER":

            # Only append if the data is good
            if check_data(new_data_entry):
                pose = generate_correct_pose(new_data_entry[2:])
                tag_poses.append(
                    {"tag_id": int(new_data_entry[1]), "pose": pose})

        else:
            print(f"I don't have any way to handle {new_data_entry}")
            
im,gt = parse_IM_GT_data(PROCESSED_GRAPH_DATA,tag_poses)
plot_IM_GT_data(im,gt)

# dump it to a json file
with open(OUTPUTED_JSON_PATH, "w") as f:
    data = {
        "poses":
            tag_poses
    }

    json.dump(data, f, indent=2)

