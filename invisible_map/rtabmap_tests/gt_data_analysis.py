"""
python script to clean data coming from RTABmaps regarding tag locations. Trying to test
if it could be viable as ground truth data.
"""

import json
import os
import numpy

RTABMAP_DATA_PATH = "test_data/poses7.txt"
OUTPUTED_JSON_PATH = "gt_json/MAC_2_3_reversed_z.json"


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
    rtabmap_pose = numpy.array([pose[0],pose[1],pose[2]])
    rotation_mat = numpy.array([[0,0,-1],[-1,0,0],[0,1,0]])
    final_pose =  numpy.dot(rotation_mat,rtabmap_pose)
    for i in range(3):
        pose[i] = final_pose[i]
    # print("break")

    # print(pose)
    return pose


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

# dump it to a json file
with open(OUTPUTED_JSON_PATH, "w") as f:
    data = {
        "poses":
            tag_poses
    }

    json.dump(data, f, indent=2)
