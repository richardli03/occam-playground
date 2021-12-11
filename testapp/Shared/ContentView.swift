//
//  ContentView.swift
//  Shared
//
//  Created by Richard Li on 12/11/21.
//

import SwiftUI


struct ContentView : View {
    // call the function defined in the other file.
    @ObservedObject var compassHeading = CompassHeading()
    var body: some View {
        Text(String(compassHeading.degrees))
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
