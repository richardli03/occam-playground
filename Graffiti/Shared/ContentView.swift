//
//  ContentView.swift
//  Shared
//
//  Created by Richard Li on 12/27/21.
//


import SwiftUI
import AVKit



struct ContentView: View {
    
    switch AVCaptureDevice.authorizationStatus(for: .video) {
        case .authorized: // The user has previously granted access to the camera.
            self.setupCaptureSession()
        
        case .notDetermined: // The user has not yet been asked for camera access.
            AVCaptureDevice.requestAccess(for: .video) { granted in
                if granted {
                    self.setupCaptureSession()
                }
            }
        
        case .denied: // The user has previously denied access.
            return

        case .restricted: // The user can't grant access due to restrictions.
            return
    }

    
    @ObservedObject var arDelegate = ARDelegate()
    
    var body: some View {
        ZStack {
            ARViewRepresentable(arDelegate: arDelegate)
            VStack {
                Spacer()
                Text(arDelegate.message)
                    .foregroundColor(Color.primary)
                    .frame(maxWidth: .infinity)
                    .padding(.bottom, 20)
                    .background(Color.secondary)
            }
        }.edgesIgnoringSafeArea(.all)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
