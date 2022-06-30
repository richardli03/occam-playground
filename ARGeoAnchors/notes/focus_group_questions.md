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
- say "snap" or some other auditory cue
- cue is so that it can be a failsafe if there is a false snap
- very important to know when its doing something
- google maps sometimes won't tell you when you're going in the wrong direction, don't follow that approach
- needs to be communicated that the app is relying on your motion and that your going the right way to resync the path
- probably need to add override compatibility
- don't want to have to take gloves off when dealing with it
- seems very personal, maybe have settings options for how the snap will work
- user will know if the app is screwed up
---
Scanning your location involves waving your camera back and forth in front of you and giving Apple visuals of your surroundings. Apple doesn't have a built in system for notifying the user when localization is highly accurate, but we can add something to do that. 

2. Do you think it'd be difficult to scan your location? What kind of feedback would you want about your status of localization? What should we tell you if your localization isn't good?

---
3. When was the last time you reversed a route on Clew/ have you ever had a difficult time making your way out of a building after going in?
    - Return navigation? How hard is it to make your way out of a building using tree anchors/etc.
    - Navigation is fine going outdoor-to-indoor, but the other way around is currently impossible (can't scan surroundings)
    - If people can easily and regularly get help making their way out of a building, then it's not a problem we have to solve
- quite useful to tie indoor and outdoor navigation together
- win to have it all in one app
- would also love a transition from inside to outside
- less of an issue because the bottleneck is the door, once you find the door you're okay
- far easier to find the door from inside
- depends on what it is
- if it is a doctor's office, there's normally someone to help like a reciptionist to help once you are inside
- but a restaurant, no, there is limited help for going out
- seems like the ideal is a seemless transition between indoor and outdoor navigation
- also very difficult in conventions to find your way out
---
4. How common is this use case? Can you give us more details about situations where you've ubered to unfamiliar/less-than-familiar locations?
- totally, this is the number one problem wanting to be solved
- last ten meters from the uber door to inside
- everyday thing
- this is definitely a common use case, but would probably rely on people if they are around
- baseline should be so people can be completely independent without assistance from other people
---
5. Would you be confident in an app to guide you in these kinds of scenarios?
    - Which of these things would you still use during app use?
        - Cane
        - Dog
        - Sighted guide
        - Other assistive tech?
        - Other apps
- do a mixture of everything
- number one is still to ask a sighted person because it's fastest
- would use technology secondary to asking a person
- get AI first so you don't have to resort to IRA and worry about minutes left
- order typically goes person -> AI -> IRA
- based on the experience and accuracy of the app
- if a technology has been consistently useful, david would go back to it (wouldn't if it consistently has failed him)
- never, under any circumstance, trust a technology 100%, always have a cane to support
- trust, but verify - want to trust the technology but verify it with other things
- safety is priority so always have cane, rely on technology but cane is also important
---
6. Tell us about moments where Clew Maps/your other navigation techniques have failed. What triggered that failure? 
- blindsquare is go to gps app
- failed not because it can't report gps positioning, but in area with lots of big buildings, signal gets obstructed
- randomly changed directions, so constantly getting turned around
- Clew fails in hotel hallway with undistinguishable feature
- STR is helpful because knows the route to go, can snap to him knowing where he's going
- tall buildings give you bad cell signal, also very little cell coverage in rural Vermont
---

7. Outdoor-only navigation? When you get out of a car and you need to find a building, what is the farthest away that a car has dropped you from a building? What happened?

---
8. Is there anything we're failing to consider?
- should do more testing in Boston, like ice cream place because it's better than NECO
- in settings, give the user the option to snap - warning and what to snap based on
- don't need constant beeps, have option to mute and unmute audio



[NOTE: talking about features will probably make them like it]