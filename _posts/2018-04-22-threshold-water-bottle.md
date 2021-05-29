---
layout: post
title: Threshold and Specisific Object Detection
date: 2012-05-22
excerpt: "Threshold the water bottle!."
comments: true
---
    
<center><b>Semih GULUM</b>    Mechatronic Engineer </center>

Threshold and Specisific Object Detection

## List of libraries used
* OpenCV
* Matplotlib
* Numpy

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118397560-4291d780-b65d-11eb-8d26-c2b5c3d49ad3.gif
{% endcapture %}
{% include gallery images=images caption="Figure 1 - Mini gif about project "%}

## Explanation the Project

In this project, i tried to track my water bottle. As you can see above i didn't use any deep learning library. It's easy and funny project. But if you don't find the right threshold value, it can turn into an annoying situation. I used trackbars to avoid this. So let's see the code!

```python
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

And the output will be:

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118394615-6b5ea080-b64e-11eb-92d3-91f6ec0c61c0.png
{% endcapture %}
{% include gallery images=images caption="Figure 2 - Output"%}


However, instead of leaving the project like this, let's calculate the areas in the image by using the threshold values we have obtained. While doing this, let's try to determine if there is a water bottle on a specific area, not the whole area:

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened() :
	_,frame = cap.read()
	rectangled_frame = frame.copy()

	#changing bgr to rgb
	frame_rgb = frame[:, :, ::-1]

	pt1x = frame_rgb.shape[0]-400
	pt1y = frame_rgb.shape[1]-400
	pt2x = frame_rgb.shape[0]-200
	pt2y = frame_rgb.shape[1]-200
	pt1 = (pt1x, pt1y)
	pt2 = (pt2x, pt2y)

	cropped_frame = frame_rgb[pt1y:pt2y, pt1x:pt2x]

	cv2.rectangle(rectangled_frame, pt1, pt2, (0,255,255), 2)

	hsv_frame = cv2.cvtColor(cropped_frame, cv2.COLOR_RGB2HSV)

	lower = np.array([int(175/2), 47, 77])
	upper = np.array([int(334/2), 255, 255])


	mask = cv2.inRange(hsv_frame, lower, upper)
	res = cv2.bitwise_and(cropped_frame, cropped_frame, mask=mask)	

	mean = np.mean(mask)
	[x, y] = np.where(mask==255)
	mask_x = np.mean(x).astype(np.uint8)
	mask_y = np.mean(y).astype(np.uint8)
	max_mask_x = np.max(x).astype(np.uint8)
	min_mask_x = np.min(x).astype(np.uint8)
	max_mask_y = np.max(y).astype(np.uint8)
	min_mask_y = np.min(y).astype(np.uint8) 
	coord1 = (min_mask_y, min_mask_x)
	coord2 = (max_mask_y, max_mask_x)

	if mean<30 :
		message = 'Mavi renk tespit edilemedi.'
		cv2.putText(rectangled_frame, message, (pt1x-20, pt1y-20), 1,1, (255,255,255), 3)

	elif mean >30 and mean <100: 
		message = 'Acik mavi renk tespit edildi.'
		cv2.putText(rectangled_frame, message, (pt1x-20, pt1y-20), 1,1, (255,255,255), 3)
		cv2.putText(res, str(mean), (mask_y, mask_x), 1,1, (255,255,255), 3)
		cv2.rectangle(res, coord1, coord2, (255,255,255), 2)
	elif mean >100: 
		message = 'Belirtilen alanda bir sise olabilir.'
		cv2.putText(rectangled_frame, message, (pt1x-20, pt1y-20), 1,1, (255,255,255), 3)
		cv2.putText(res, str(mean), (mask_y, mask_x), 1,1, (255,255,255), 3)
		cv2.rectangle(res, coord1, coord2, (255,255,255), 2)
	
	#Değiskenlerimizi matplotlib üzerinde gösterebilmek için bgr'dan rgb'ye döndürüyoruz.
	mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
	rectangled_frame = rectangled_frame[:, :, ::-1]
	
	plt.subplots_adjust(wspace=0.4, hspace=0.5, left=0.4, bottom=0, top=0.95)
	plt.subplot(231)
	plt.imshow(frame_rgb)
	plt.title("Orjinal hali")
	plt.subplot(232)
	plt.imshow(rectangled_frame)
	plt.title("Dikdörtgen çizilmiş hali")
	plt.subplot(233)
	plt.imshow(cropped_frame)
	plt.title("Kırpılmış hali")
	plt.subplot(234)
	plt.imshow(hsv_frame)
	plt.title("HSV Renk uzayındaki hali")
	plt.subplot(235)
	plt.imshow(res)
	plt.title("Bitwise yardımıyla olan hali")
	plt.subplot(236)
	plt.imshow(mask)
	plt.title("Maskeli Hali")

	plt.show()

	if cv2.waitKey(1) & 0xFF==ord("q"):
			break 

cv2.destroyAllWindows()
```

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118398039-82f25500-b65f-11eb-833b-f30bd4c8e436.png
{% endcapture %}
{% include gallery images=images caption="Figure 3 - Output"%}



From now on, I will assign these values(most optimized max and min value ranges I found from the trackbar) to a list variable instead of setting the values every time again and again.

lower = np.array ([int (175/2), 47, 77])
upper = np.array ([int (334/2), 255, 255])



## Thanks for reading my project!