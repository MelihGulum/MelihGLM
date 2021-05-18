---
layout: post
title: Teeth numbering and Disease Detection
date: 2012-05-29
excerpt: "This project is my and my friend's graduation project!"
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
* flask


## Explanation the Project

In 2021 Autumn me and my dear project friend (Seçilay Kutal)[] did the project. Since the dental topic is a subject outside of our field, we explained our project to the dentists who are the best in their field and we asked them for help to realize this project. 
and as a result, we decided to realize a project together. Since the dental topic is a subject outside of our field, we explained our project to the dentists who are the best in their field and we asked them for help to realize this project. They also liked our idea and as a result we decided to do a project together.We even applied to Tübitak, which holds the most important R&D competitions of our country. Throughout the project, reports were delivered to the juries by keeping in touch with the juries, and at the end of the project, we became a Tübitak approved project.

We have two models. One is numbering and the other is disease diagnosis. There are 32 classes in the numbering in this project for the adult mouth. In diagnosis, we carried out our training with 12 classes. 5000 x-rays were used for both training.
Now, let's try to see what the tooth numbering is done according to what and which diagnoses look like what:

<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118599343-0a52dc00-b7b8-11eb-91eb-53f68b58a773.png
	https://user-images.githubusercontent.com/56072259/118599352-0d4dcc80-b7b8-11eb-90e9-f125e41b0091.png
{% endcapture %}
{% include gallery images=images cols=2 caption="Figure 2 - Teeth Numbering and Diseases "%}
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
{% include gallery images=images cols=3 caption="Figure 3 - Sunglasses Detect with Cool Matrix Sunglasses "%}
<b>

Lol, if you can stop laughing, we can look at our next object, smartphones.
<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118528304-d8eff700-b74a-11eb-8c68-86b0e26a2811.png
	https://user-images.githubusercontent.com/56072259/118528329-dee5d800-b74a-11eb-8fb8-4520fff07200.png
	https://user-images.githubusercontent.com/56072259/118528343-e2795f00-b74a-11eb-96bc-94c07439e56a.png
{% endcapture %}
{% include gallery images=images cols=3 caption="Figure 4 - Smartphone Detection "%}
<b>

Our next object is a cigarette. However, I do not use smoking, this time I will ask my model to predict the images I found on the internet.

<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118529094-cb873c80-b74b-11eb-950d-9dd44369803a.png
	https://user-images.githubusercontent.com/56072259/118529078-c7f3b580-b74b-11eb-954e-e13c1ef6dd70.png
	https://user-images.githubusercontent.com/56072259/118529081-c924e280-b74b-11eb-905d-6fb96e574952.png
	https://user-images.githubusercontent.com/56072259/118531356-6b45ca00-b74e-11eb-8bc8-d1c54a4ded4e.png
{% endcapture %}
{% include gallery images=images cols=2 rows=2 caption="Figure 5 - Cigarette Detection "%}
<b>




## Thanks for reading my project!