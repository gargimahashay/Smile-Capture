# Smile-Capture

## Discription
I create an automatic smile capture selfie. Here we used the system webcam, and our picture gets captured when we smile.

##  Library used

**OpenCV-Python**: OpenCV is an excellent tool for image processing and computer vision tasks. It is an open-source library that performs functions like face detection, objection tracking, landmark detection, and much more.
OpenCV-python used for computer vision, machine learning, and image processing.

**Datetime**: For work with date and time.

**Playsound**: For playsound in our program.

## Execution Steps:

1.	Import libraries.
2.	Then we record the video using our system camera(here, laptop front webcam) and VideoCapture(0). Here 0 is used to turn on our system webcam to record.
3.	Here, we provide the location to access our cascade file(face_cascade, smile_cascade). (Haarcascade is an Object Detection Algorithm used to identify faces in an image or a real-time video. The algorithm uses edge or line detection features. )
4.	We run a loop to read video (as we know, video is a set of collections of frames) and for performing functions.
5.	We use cvtColor to convert colour to greyscale to increase accuracy and use detectMultiScale to detect the faces. This function will return a rectangle with coordinates (x, y, w, h) around the detected face, and scaleFactor specifies the image size reduced with each scale.
6.	Then we run a for a loop; this function recognizes the face and smile.
7.	We use the rectangle function to draw a rectangle over a face that is detected and again use detectMultiScale.
8.	We use a nested for loop to put a rectangle on the smile(i.e., lips when in the smiling position).
9.	For saving the image with time and date in a specific format, we use datetime.datetime.now().strftime() and enter such a particular date and time format.
10.	Finally, the image (.png format) is stored in the working directory.

</br>
</br>
</br>
</br>

<p align="center"><img width="480" alt="image" src="https://user-images.githubusercontent.com/72460920/186567356-848ff4d2-3352-4730-a3a4-c4c6c90a39c2.png"></p>
<p align="center"><img width="481" alt="image" src="https://user-images.githubusercontent.com/72460920/186567395-cd2a5159-5147-48fd-aa6a-a729e73c424d.png"></p>
<p align="center"><img width="474" alt="image" src="https://user-images.githubusercontent.com/72460920/186567436-fdd7d9da-ad04-442c-826a-8b22fb3dde9c.png"></p>
<p align="center"><img width="481" alt="image" src="https://user-images.githubusercontent.com/72460920/186567477-b2c0c2f2-c749-4eeb-aca1-307366f71a3c.png"></p>
<p align="center"><img width="479" alt="image" src="https://user-images.githubusercontent.com/72460920/186567508-46d886b3-d2ef-4810-a997-e144accc376c.png"></p>
<p align="center"><img width="480" alt="image" src="https://user-images.githubusercontent.com/72460920/186567541-b3142f87-85bf-4556-8e8c-fff30b9b1e2f.png"></p>



</br>
</br>


## Result

https://user-images.githubusercontent.com/72460920/197562086-b476550f-6e68-441e-8776-8740d768a8a1.mp4




