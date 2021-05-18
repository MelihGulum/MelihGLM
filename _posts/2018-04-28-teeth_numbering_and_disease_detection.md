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
{% include gallery images=images cols=2 caption="Figure 1 - Teeth Numbering and Diseases "%}
<b>

While it took about 6 months to get approval from Tubitak, we are still working on improving the project and presenting it to the customer. Estimates reaching 84% in teeh numbering and 91% in diagnosis were made. But I can show you the findings on how our graduation project turned out.

## &#8594; For Teeth Numbering

Like i said, we have 32 class(cause adults have 32 teeth). These are some examples:

<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118635531-60d21180-b7dc-11eb-854c-ec8d1cdf6708.jpg
	https://user-images.githubusercontent.com/56072259/118635538-629bd500-b7dc-11eb-8fbf-a82a17b84e0d.jpg
{% endcapture %}
{% include gallery images=images cols=2 %}
<b>

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118635550-64659880-b7dc-11eb-88b6-e12fda50fc7c.jpg
	https://user-images.githubusercontent.com/56072259/118635551-64fe2f00-b7dc-11eb-9103-29dafb7b0e76.jpg
{% endcapture %}
{% include gallery images=images cols=2 %}
<b>

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118635556-64fe2f00-b7dc-11eb-84fd-04019c8a124b.jpg
	https://user-images.githubusercontent.com/56072259/118635525-60397b00-b7dc-11eb-879d-c48da9ede669.jpg
{% endcapture %}
{% include gallery images=images cols=2 caption="Figure 2 - Dentist vs Machine vol 1"%}
<b>

## &#8594; For Detecting Disease

We have 12 classes for disease detection. While choosing these diseases, we discussed with our dentist teachers and selected the diseases that we think the machine can find.

<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118688397-b2938f80-b80e-11eb-961c-bf9d1f3bd519.jpg
	https://user-images.githubusercontent.com/56072259/118688404-b3c4bc80-b80e-11eb-9074-4361732ca04a.jpg
{% endcapture %}
{% include gallery images=images cols=2 %}
<b>

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118688415-b58e8000-b80e-11eb-8f5c-e9f4c7cb5c5d.jpg
	https://user-images.githubusercontent.com/56072259/118688419-b6271680-b80e-11eb-8d83-281b22a3d1e8.jpg
{% endcapture %}
{% include gallery images=images cols=2 %}
<b>

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118688421-b6bfad00-b80e-11eb-8109-52b800fb31dd.jpg
	https://user-images.githubusercontent.com/56072259/118688425-b7584380-b80e-11eb-9fd4-f807add6397e.jpg
{% endcapture %}
{% include gallery images=images cols=2 caption="Figure 3 - Dentist vs Machine vol 2"%}
<b>

But it isn't enough! We want to be able to say "this tooth has this disease". Therefore, we can make this interpretation by looking at the areas of intersections of the coordinate information we have. If the intersection area is larger than the threshold value we have determined, we can take it as an intersection.

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118702332-79aee700-b81d-11eb-9824-e0b2e6940510.png
{% endcapture %}
{% include gallery images=images caption="Figure 3 - Dentist vs Machine vol 2"%}
<b>


## Thanks for reading my project!