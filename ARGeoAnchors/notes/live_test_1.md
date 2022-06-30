Insert: steps for what the users should do. Be methodical!

# Test Plan 
Project: Outdoor to Indoor Navigation with ARGeoAnchors

Description: Trying to stress test the beta version of Clew that uses ARGeoAnchors instead of ARAnchors to navigate

Assumptions & Preconditions
- The user will be at the NECO//somewhere in Boston
- Either Ayush, Paul, or Richard will be present to help dictate/observe testing
- The user will have a device on which they can run Clew

Test Cases / Steps
NOTE:  Create a test for each function of the application (login, register, navigate, etc) listing the steps and expected results.  Testers follow the steps and record their results.  Include enough detail to ensure a person who is not familiar with the application can perform the function.

Test 1: Testing navigation on a pre-recorded route without any suggestions/tampering
- Record the route for the user. 
- Have the user navigate the route themselves

Quantities to evaluate:
- Did the user get to the right place? Did they wander off during the route?
- Was the snap disorienting?
- Did the snap make the route better?
- How intuitive is the app's workflow/decision-making regarding when to snap?

Test 2: Testing recording of routes + then having them navigate from the start
- Have the user record a route for themselves (with sighted guide?)
- Pretend like it's the next time they have to visit, have them navigate from the beginning.

Quantities to evalaute:
- Is recording a route easy?
- Do they understand roughly how long the app needs to see the surroundings in order to localize


SUM: 

Looking for natural tendencies in navigation, things we may have missed regarding our implementation of our code. Additionally trying to test ICP in a non-controlled, non-pre-recorded setting in a more robust way. 