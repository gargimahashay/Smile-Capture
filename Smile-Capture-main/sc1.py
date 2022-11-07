# opencv-python and opencv-contrib-python used for computer vision, machine learning, and image processing
import cv2
# to work with date and time
import datetime
# used to playsound in our program
import playsound
# import wavfile
# here we use videocapture and give parameter 0 that is for to turn on our pc camera to record
cap = cv2.VideoCapture(0)
# here we give a access to our cascade file by giving location
face_cascade = cv2.CascadeClassifier('C:\\Users\\HP\\Desktop\\Aksh\\Extra\\New folder\\my_practice_one\\Smile_capturer\\mineprpr\\haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('C:\\Users\\HP\\Desktop\\Aksh\\Extra\\New folder\\my_practice_one\\Smile_capturer\\mineprpr\\haarcascade_smile.xml')

# here we check the conditions
while True:
    # here we divide the video into multiple frames

    # as we all know video is a set of multiples frames
    _, frame = cap.read()
    if frame is None:
        break
    original_frame = frame.copy()
    # cvtColor used for changing the colour
    # COLOR_BGR2GRAY used for changing the colorful into grey(black and white)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    # this function used for recognising the face and smile
    for x, y, w, h in face:
        # it create the rectangle on face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        face_roi = frame[y:y+h, x:x+w]
        gray_roi = gray[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
        # this is used to save the smile selfies in specific area with a specific name with a specific format that
        # we here enter like according to date and time.

        for x1, y1, w1, h1 in smile:
            cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            file_name = f'selfie-{time_stamp}.png'
            # playsound('camera_click.mp3')
            cv2.imwrite(file_name, original_frame)
    cv2.imshow('cam star', frame)
    # after performing this we end the program
    if cv2.waitKey(10) == ord('q'):
        break