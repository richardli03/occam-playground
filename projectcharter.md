# Project Charter
Project Title: Outdoor to Indoor 

Navigation Project Team: Richard Li / Ayush Chakraborty

Kick-off Date: 2/1/22

Project Description: Oftentimes a tricky situation for those who are B/VI is navigating in an outdoor environment and trying to transition indoors. After all, finding a specific ramp or door isn't always that easy, especially in city settings. 

In an attempt to remedy that problem, we're using ARGeoAnchors to accurately navigate B/VI users from outdoor to indoor settings. 

[ARGeoAnchors](https://developer.apple.com/documentation/arkit/argeoanchor) are a new technology released by Apple designed to help "identify a geographic location using latitude, longitude, and altitude data." It additionally utilizes "imagery" to localize the user. All this to say, it uses the phone's camera and its GPS to express the phone's location in a way that is far more accurate that most other systems.

Unfortunately it's only active in a [few locations](https://developer.apple.com/documentation/arkit/argeotrackingconfiguration) -- thankfully, **Boston** is one of them, so we  were able to test a configuration of the Clew app that integrates ARGeoAnchors into its navigation instead of the currently used ARAnchors.

Project Objectives:
- Create a proof-of-concept version of Clew Maps that uses ARGeoAnchors as its primary tool of navigation.
- Apply whatever algorithms are necessary to ensure alignment accuracy while indoors. 

Assumptions:
- ARGeoAnchors will be able to accurately give us an initial location from any outdoor place in its coverage area. 

Constraints:
- While there is a considerable amount of documentation on ARGeoAnchors, they still are a black box. It's impossible to mess with the mechanics of how they are created. 
- 

Time
DONE


Budget
Our project will use <$500 dollars. Any money spent on this project will only be transportation to the NECO for testing. 


Scope In
Creating extremely effective outdoor to indoor navigation where ARGeoAnchors are currently supported


Scope Out
Outdoor to indoor navigation where ARGeoAnchors are not supported.


Milestones
Date
Milestone Description
#1 - Testing whether ARGeoAnchors can accurately provide a location outside + navigate us indoors using Apple's default test-app


#2 - Testing whether ARGeoANchors can be successful integrated into the current ARAnchors that Clew Maps uses. Specifically, testing to see if the behavior we see in the test app released by apple tracks to the behavior we implement in Clew Maps.


#3 - Testing whether ARGeoAnchors can maintain accuracy after moving indoors + implmenting any necessary algorithms to correct for errors we see.


Project Risks:
The main risk that we have to face is that this could all just be a huge waste of time. There's not really a money sink or anything going into this. 

Project Resourcing Requirements
- Time
- ~$500


Brainstorming Tasks / Timeframe
NOTE: Work as a team to identify your task to complete the project.  Once you have them organized I will put them in the timeline chart.  If you know who will do the work, when it will start / end you can add that, but we can also add that later once it is known.

1. Test initial behavior of ARGeoAnchors. Testing specifically for accuracy of initial localization + accuracy of navigation as you go further into the building. 
2. Integration into Clew Maps
3. Fixing any alignment issues we see

