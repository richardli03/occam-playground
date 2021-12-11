//
//  Compass.swift
//  testapp
//
//  Created by Richard Li on 12/11/21.
//

import Foundation
import Combine
import CoreLocation


// This gets the orientation angle of the user.

// Creating a class called "CompassHeading" that has three subclasses
class CompassHeading: NSObject, ObservableObject, CLLocationManagerDelegate {
    
    //creating a variable "objectWillChange" whose output is "void" and "never" if it fails????
    //https://developer.apple.com/documentation/combine/passthroughsubject ???
    var objectWillChange = PassthroughSubject<Void, Never>()
    
    //creating the degrees variable as a double, initializing it as a zero
    var degrees: Double = .zero {
        //as soon as the value changes the value you see is different // realtime???
        didSet {
            objectWillChange.send()
        }
    }
    
    //defining a locationManager variable (that we don't expect to change) type: CLLocationManager (defined in CoreLocation)
    private let locationManager: CLLocationManager
    
    //overrides normal initialization procedure from the parent class
    override init() {
        self.locationManager = CLLocationManager()
        //"super" calls the parent constructor
        super.init()
        
        //not too sure what delegates are, but... :D
        self.locationManager.delegate = self
        //calls the set up function
        self.setup()
    }
    
    private func setup() {
        // requesting access to the user's position? maybe?
        self.locationManager.requestWhenInUseAuthorization()
        
        //start doing the thing!
        if CLLocationManager.headingAvailable() {
            self.locationManager.startUpdatingLocation()
            self.locationManager.startUpdatingHeading()
        }
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateHeading newHeading: CLHeading) {
        // random 20 degree error fixed by hardcoding
        self.degrees = 1 * newHeading.magneticHeading - 20
        // have to do this so it doesn't go negative
        // bad coding practice, yes, but it works :)
        if self.degrees < 0
        {
            self.degrees = self.degrees + 360
        }
    }
}
