# Using ARGeoAnchors to navigate indoor + outdoor routes #
*written by: Richard Li and Ayush Chakraborty*

# Project Overview
[ARGeoAnchors](https://developer.apple.com/documentation/arkit/argeoanchor) are a new technology released by Apple designed to help "identify a geographic location using latitude, longitude, and altitude data." It additionally utilizes "imagery" to localize the user. All this to say, it uses the phone's camera and its GPS to express the phone's location in a way that is far more accurate that most other systems.

Unfortunately it's only active in a [few locations](https://developer.apple.com/documentation/arkit/argeotrackingconfiguration) -- thankfully, **Boston** is one of them, so we  were able to test a configuration of the Clew app that integrates ARGeoAnchors into its navigation instead of the currently used ARAnchors.

# Methodology
Clew currently localizes the user by directing the user to put their phone against a wall at the same place they put their phone when recording the route. This aligns the phone's current position with the previous map, localizing the phone and enabling navigation to occur.

Our branch, instead, localizes the user using Apple's ARGeoAnchor technology and attempts to navigate by having Apple compute where the recording location started and where the user is now. Thus, we don't have to do any localization, other than directing the user to scan the surroundings for a few seconds (enabling the "imagery localization" of an ARGeoAnchor)

As we can see: this


# To include:
Visualizations:
1. Unsnapped
2. Snapped
3. Snapped with recency bias

Timeline:

Limitations:

Miro board:

User interviews + user testing:
1. List of potential users
2. List of failcases


Credits: 

Resources:

Further exploration: