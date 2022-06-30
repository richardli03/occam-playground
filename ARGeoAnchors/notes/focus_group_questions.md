Questions:
Explanation of the project before all this.


ARGeoAnchors are a new technology released by Apple that use GPS and imagery of your surroundings to give a *very* accurate idea of where you are. We can use these geoanchors to navigate you, similar to Clew.

This technology alone has great potential for outdoor-to-outdoor navigation, like getting from your house to an outdoor bus stop // from your car to the door of a restaurant, etc. 

We're trying to expand the possibilities of the app by giving it outdoor-to-indoor navigation potential. However, the problem we see is that the navgiation quality deteriorates as you get indoors, because Apple can no longer use the surrounding imagery to make your position more clear. 

---
Our solution to that is "Snap-to-route," an algorithm that rotates the planned path onto the path you're currently walking, realigning the future directions with your path. There's a lot of complicated math that goes on behind it, but essentially we can adjust your instructions and move the anchors when we detect that Apple's localization is failing. 

- benefits over GPS? - far more accurate, GPS is only accurate to 5 meters
- lots of backlash against limited coverage area
- uses google maps for outdoor navigation, main challenge is starting point (not always accurate) need to walk x feet for it to be accurate, also can't tell what direction to walk at first, need to use a compass
- Integrate other apps into this: Apple is adding door detection
- last 50 feet is what really makes the difference

1. Explanation of snap-to-route ... Would the anchor moving mid-route confuse you? Do you need an explanation for why it moves? Information.

---
Scanning your location involves waving your camera back and forth in front of you and giving Apple visuals of your surroundings. Apple doesn't have a built in system for notifying the user when localization is highly accurate, but we can add something to do that. 

2. Do you think it'd be difficult to scan your location? What kind of feedback would you want about your status of localization? What should we tell you if your localization isn't good?

---
3. When was the last time you reversed a route on Clew/ have you ever had a difficult time making your way out of a building after going in?
    - Return navigation? How hard is it to make your way out of a building using tree anchors/etc.
    - Navigation is fine going outdoor-to-indoor, but the other way around is currently impossible (can't scan surroundings)
    - If people can easily and regularly get help making their way out of a building, then it's not a problem we have to solve

---
4. How common is this use case? Can you give us more details about situations where you've ubered to unfamiliar/less-than-familiar locations?

---
5. Would you be confident in an app to guide you in these kinds of scenarios?
    - Which of these things would you still use during app use?
        - Cane
        - Dog
        - Sighted guide
        - Other assistive tech?
        - Other apps

---
6. Tell us about moments where Clew Maps/your other navigation techniques have failed. What triggered that failure? 

---

7. Outdoor-only navigation? When you get out of a car and you need to find a building, what is the farthest away that a car has dropped you from a building? What happened?

---

[NOTE: talking about features will probably make them like it]