---
layout: post
title: Simple WordCloud Project
date: 2012-05-22
excerpt: "You're a wizard Harry!"
comments: true
---
    
<center><b>Semih GULUM</b>    Mechatronic Engineer </center>

Threshold and Specisific Object Detection

## List of libraries used
* os
* pandas 
* re
* wordcloud
* matplotlib
* PIL
* numpy
* matplotlib
* OpenCV
* google.colab.patches (If you use code in colab)

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118397560-4291d780-b65d-11eb-8d26-c2b5c3d49ad3.gif
{% endcapture %}
{% include gallery images=images caption="Figure 1 - Mini gif about project "%}

## Explanation the Project

In this project, i tried to track my water bottle. As you can see above i didn't use any deep learning library. It's easy and funny project. But if you don't find the right threshold value, it can turn into an annoying situation. I used trackbars to avoid this. So let's see the code!

```colab
import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
	pass

cv2.namedWindow("resim")

cv2.createTrackbar("H1", "resim", 0, 359, nothing)
cv2.createTrackbar("H2", "resim", 0, 359, nothing)
cv2.createTrackbar("S1", "resim", 0, 255, nothing)
cv2.createTrackbar("S2", "resim", 0, 255, nothing)
cv2.createTrackbar("V1", "resim", 0, 255, nothing)
cv2.createTrackbar("V2", "resim", 0, 255, nothing)

while cap.isOpened() :
	_,frame = cap.read()
	rectangled_frame = frame.copy()

	#changing bgr to rgb
	frame = frame[:, :, ::-1]

	pt1x = frame.shape[0]-400
	pt1y = frame.shape[1]-400
	pt2x = frame.shape[0]-200
	pt2y = frame.shape[1]-200
	pt1 = (pt1x, pt1y)
	pt2 = (pt2x, pt2y)
	cropped_frame = frame[pt1y:pt2y, pt1x:pt2x]

	cv2.rectangle(rectangled_frame, pt1, pt2, (0,255,255), 2)
	rectangled_frame = rectangled_frame[:, :, ::-1]

	hsv_frame = cv2.cvtColor(cropped_frame, cv2.COLOR_RGB2HSV)
	cv2.imshow("resim", hsv_frame)


	H1 = int(cv2.getTrackbarPos("H1","resim")/2)
	H2 = int(cv2.getTrackbarPos("H2","resim")/2)
	S1 = cv2.getTrackbarPos("S1","resim")
	S2 = cv2.getTrackbarPos("S2","resim")
	V1 = cv2.getTrackbarPos("V1","resim")
	V2 = cv2.getTrackbarPos("V2","resim")
	lower = (H1, S1, V1)
	upper = (H2, S2, V2)
	#For BGR to RGB or RGB to BGR
	new_frame = frame[:, :, ::-1]
	mask = cv2.inRange(frame, lower, upper)
	res = cv2.bitwise_and(frame, frame, mask=mask)
	res = res[:, :, ::-1]

	
	cv2.imshow("mask", mask)
	cv2.imshow("res", res)
	cv2.imshow("original",frame[:, :, ::-1])
	if cv2.waitKey(1) & 0xFF==ord("q"):
		break 
			
cv2.destroyAllWindows()
```

Also, if you want to watch the video prepared by our project group, [you can click here](https://www.youtube.com/watch?v=0Dsjd2Zoi54). 

## Thanks for reading my project!