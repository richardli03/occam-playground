import json
import os
import matplotlib.pyplot as plt
import numpy as np

# in order to update folder with json files from firebase, run 
# (gsutil -m rsync gs://clew-sandbox.appspot.com/GeoAnchorTest .) or modifications
# to such link based on which bucket data is stored in (first argument) and
# desired destination for files (second argument)

directoryPath = "anchor_data/NECO_TEST_061622"
jsonFiles = []

for file in os.listdir(directoryPath):
    if file[-5:] == '.json':
        jsonFiles.append(file)
for filename in jsonFiles:
    file = open(f'{directoryPath}/{filename}')
    jsonData = json.load(file)
    anchorCoords = np.array(jsonData['GeoAnchors'])
    cameraCoords = np.array(jsonData['CameraPositions'])
    plt.plot(anchorCoords[:,1], anchorCoords[:,0], '-')
    plt.plot(cameraCoords[:,1], cameraCoords[:,0], '-')
    plt.legend(['Keypoint Positions', 'Camera Positions'])
    plt.axis('equal')
    # plt.title('Left Camera Stairs and Right Anchor Ramp Snap')
    print(filename)
    plt.savefig(f'result_imgs/NECO_test_061622/{filename.split(".")[0]}')
    plt.show()