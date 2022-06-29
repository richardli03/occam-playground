# odo_POSE_dict = dict.fromkeys(["ODO_ID","X","Y","Z","Q_X","Q_Y","Q_Z","Q_W"])
odo_POSE_dict = {"ODO_ID":[],"POSE":[]}

def get_key(val,dictionary):
    for key, value in dictionary.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def tag_pose_averager(tag_POSE,tag_ID):
    """
    Averages the pose 

    Args:
        tag_POSE (dictionary): a dictionary containing all of the tag_POSE data
        tag_ID (string): the tag ID in question.

    Returns:
        _type_: _description_
    """
    
    for i in range(len(tag_POSE["TAG_ID"])):
        if tag_POSE["TAG_ID"][i] == tag_ID:
            tag_value = tag_POSE
            odo_number = tag_POSE["ODO_ID"][i]
            odo_value = odo_POSE_dict["POSE"][odo_POSE_dict["ODO_ID"].index(odo_number)]
            tag_pose_calculator(odo_value,)
    # First we want to add the translation vectors together
    tag_POSE["TAG_ID"].index(tag_ID)
    
    pass

def tag_pose_calculator(ODO_POSE,TAG_POSE):
    """
    Returns the combined POSE information from the odometry node and the tag position.
    The odometry node's POSE contains information from the theoretical "origin," but tag
    POSE data comes relative to the node that observed it. Therefore, to put the tags in
    the same world reference frame, we have to combine the two transformations.

    Args:
        ODO_POSE (list): a list of the 7 numbers defining the odometry node POSE
        TAG_POSE (list): a list of the 7 numbers defining the tag POSE relative to the odometry node
    """
    
    