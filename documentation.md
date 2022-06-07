# Syntax:
Anchor --> refers to the ARGeoAnchors loaded in while performing navigation
Camera --> refers to the camera POSE of the phone currently navigating
STR --> snap-to-route

# 6/6/22 Benchmarking
The goal today is to identify the source of errors on our pathing. We can clearly see that the anchors drift into the wall. Does it appear to be an error in localization? (i.e. a single angle that can be fixed )

Noteworthy visualizations detailed below:
## Center Anchor Right Camera
This looks weird, almost like 2 different angles going on? The final stretch of the path looks like it has a different angle than the ramp part at the beginning. 

## Left Anchor Right Camera (1 + 2)
Same thing. Why is the end this awful? Maybe it's the tricky hallway in addition to low localization quality? Ran this twice to make sure it wasn't a fluke.

## Right Anchor Left Camera:
Again, we see a dramatic difference in the end of the route.

## Right Anchor Center Camera:
This somehow looks worse than the left camera one, even though R+L is objectively farther apart.

# 6/7/22 STR Testing:
Still trying to implement snap-to-route, finding a lot of difficulties determining what to snap. Ordered the geoanchors so that our visualizations could be a thinner line instead of massive points. 

Currently facing the following problem:
1. STR visually drags the keypoint to Narnia
2. The actual keypoint doesn't change. We still pass it normally, even though the keypoint gets dragged somewhere we can't see. 
3. STR's "optimal transform" has a *very large* translation component, even when that component shouldn't exist at all. 

**NOTE:** *After reverting to the commit at the end of yesterday, that translation component of the optimal transform is gone. No idea what we did there.*

Further understanding of how keypoints are rendered/what they're rendered from is necessary.

Testing the a route against its own anchors. Snap to route seems to visually change the keypoints, but it doesn't appear to change the underlying object telling us where to go. As soon as we cross the (now invisible) keypoint, it just places the original "next-keypoint", sans STR.
