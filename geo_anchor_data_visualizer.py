import json
import os
import matplotlib.pyplot as plt
import numpy as np

# in order to update folder with json files from firebase, run 
# (gsutil -m rsync gs://clew-sandbox.appspot.com/GeoAnchorTest .) or modifications
# to such link based on which bucket data is stored in (first argument) and
# desired destination for files (second argument)

directoryPath = "."
jsonFiles = ["secondTest.json"]

# for file in os.listdir(directoryPath):
#     if file[-5:] == '.json':
#         jsonFiles.append(file)
for filename in jsonFiles:
    file = open(filename)
    jsonData = json.load(file)
    anchorCoords = np.array(jsonData['GeoAnchors'])
    cameraCoords = np.array(jsonData['CameraPositions'])
    plt.plot(anchorCoords[:,1], anchorCoords[:,0], '.')
    plt.plot(cameraCoords[:,1], cameraCoords[:,0], '.')
    plt.legend(['Anchor Positions', 'Camera Positions'])
    plt.axis('equal')
    plt.title('Center Anchors and Left Navigation')
    plt.savefig('centerLeft')
    plt.show()