"""
python script to clean data coming from RTABmaps regarding tag locations. Trying to test
if it could be viable as ground truth data.
"""

import json
import os

RTABMAP_DATA_PATH = "poses6.g2o"
OUTPUTED_JSON_PATH = "groundtruth.json"


# initialize empty list of tag poses
tag_poses =[]
error = False

# Data comes in as a g2o file, change to .txt
base = os.path.splitext(RTABMAP_DATA_PATH)[0]
os.rename(RTABMAP_DATA_PATH, base + ".txt")
RTABMAP_DATA_PATH = RTABMAP_DATA_PATH[:-4] + ".txt"

with open(RTABMAP_DATA_PATH,"r") as f:
    for line in f.readlines():
        new_data_entry = line.split()
        if new_data_entry[0] == "MARKER":
            
            # ignoring bad data
            if len(new_data_entry) != 9:
                print(f"ERROR in {new_data_entry}")
                error = True
            
            # odometry nodes are saved as markers as well, but with a negative ID.
            if float(new_data_entry[1]) < 0:
                print(f"Negative marker {new_data_entry[1]} detected and thrown")
                error = True
            
            if error == False:
                tag_poses.append({"tag_id": int(new_data_entry[1]), "pose": [float(blah) for blah in new_data_entry[2:]]})
            
        else:   
            print(f"I don't have any way to handle {new_data_entry}")

# dump it to a json file
with open(OUTPUTED_JSON_PATH,"w") as f:
    data = {
        "poses":
            tag_poses
    }
    
    json.dump(data,f,indent = 2)
