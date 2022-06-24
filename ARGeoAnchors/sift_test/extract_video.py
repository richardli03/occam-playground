import cv2

video_path = 'videos/right_ramp_occam_phone.mov'

video = cv2.VideoCapture(video_path)

frame_counter = 60*30

while True:
    flag, frame = video.read()
    cv2.imshow('video', frame)
    cv2.waitKey(1)
    frame_counter -= 1
    if frame_counter == 0:
        cv2.imwrite('images/right.png', frame)
        break