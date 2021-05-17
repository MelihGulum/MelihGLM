---
layout: post
title: Mask, Cigarette, Smartphone and Sunglasses Detection. All in ONE!
date: 2012-05-28
excerpt: "This project I did for car insurance companies was intended to be used in in-car cameras."
comments: true
---
    
<center><b>Semih GULUM</b>    Mechatronic Engineer </center>

Detection

## List of libraries used
* openCV
* matplotlib
* numpy
* math
* os
* time
* darknet
* ctypes


## Explanation the Project

Since I did not have a data set, I had to create it first. Therefore, I collected photos from social media platforms such as instagram, twitter and linkedin with the help of tags. As a result, I was able to create a dataset consisting of labeled 7462 data. This data set includes 1936 sunglasses, 3731 cigarettes, 450 smartphones and 2856 mask images.

<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118526861-5c104d80-b749-11eb-9fe2-dbc4c4535819.png
	https://user-images.githubusercontent.com/56072259/118526868-5dda1100-b749-11eb-9e16-7c4d80951715.png
	https://user-images.githubusercontent.com/56072259/118526851-59155d00-b749-11eb-855b-b1ab658b51a6.png
{% endcapture %}
{% include gallery images=images cols=3 caption="Figure 1 - mask photos from every angle "%}
<b>

But it is not that easy. We have a test! Lets see if it say mask or not.

<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118527257-c9bc7980-b749-11eb-9684-9d343ae76d9a.png
{% endcapture %}
{% include gallery images=images caption="Figure 2 - Simple Test For Mask Detection "%}
<b>


Yeah! We pass the test :D Now let's look at the others. 

<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118527765-43ecfe00-b74a-11eb-8724-0f7a076b38eb.png
	https://user-images.githubusercontent.com/56072259/118527730-3d5e8680-b74a-11eb-91d6-ecb2d36340bc.png
	https://user-images.githubusercontent.com/56072259/118527754-418aa400-b74a-11eb-9ae9-6461d4df99fe.png
{% endcapture %}
{% include gallery images=images cols=3 caption="Figure 2 - Sunglasses Detect with Cool Matrix Sunglasses "%}
<b>

Lol, if you can stop laughing, we can look at our next object, smartphones.
<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118528304-d8eff700-b74a-11eb-8c68-86b0e26a2811.png
	https://user-images.githubusercontent.com/56072259/118528329-dee5d800-b74a-11eb-8fb8-4520fff07200.png
	https://user-images.githubusercontent.com/56072259/118528343-e2795f00-b74a-11eb-96bc-94c07439e56a.png
{% endcapture %}
{% include gallery images=images cols=3 caption="Figure 3 - Smartphone Detection "%}
<b>

Our next object is a cigarette. However, I do not use smoking, this time I will ask my model to predict the images I found on the internet.

<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118529094-cb873c80-b74b-11eb-950d-9dd44369803a.png
	https://user-images.githubusercontent.com/56072259/118529078-c7f3b580-b74b-11eb-954e-e13c1ef6dd70.png
	https://user-images.githubusercontent.com/56072259/118529081-c924e280-b74b-11eb-905d-6fb96e574952.png
	https://user-images.githubusercontent.com/56072259/118529088-ca560f80-b74b-11eb-8438-4a1c42b54e73.png
{% endcapture %}
{% include gallery images=images cols=2 rows=2 caption="Figure 3 - Output"%}
<b>



Also, if you want to watch the video prepared by our project group, [you can click here](https://www.youtube.com/watch?v=0Dsjd2Zoi54). 

## Thanks for reading my project!