---
layout: post
title: Teeth numbering and Disease Detection
date: 2012-05-29
excerpt: "This project is my and my friend's graduation project!"
comments: true
---
    
<center><b>Semih GULUM</b>    Mechatronic Engineer </center>

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

<p>In 2021 Autumn me and my dear project friend <a href="https://www.linkedin.com/in/se%C3%A7ilay-kutal-111b27154/"> Seçilay Kutal </a> did the project. Since the dental topic is a subject outside of our field, we explained our project to the dentists who are the best in their field and we asked them for help to realize this project. 
and as a result, we decided to realize a project together. Since the dental topic is a subject outside of our field, we explained our project to the dentists who are the best in their field and we asked them for help to realize this project. They also liked our idea and as a result we decided to do a project together.We even applied to Tübitak, which holds the most important R&D competitions of our country. Throughout the project, reports were delivered to the juries by keeping in touch with the juries, and at the end of the project, we became a Tübitak approved project. </p>

We have two models. One is numbering and the other is disease diagnosis. There are 32 classes in the numbering in this project for the adult mouth. In diagnosis, we carried out our training with 12 classes. 5000 x-rays were used for both training. We used the labelimg program to label it. Now, let's try to see what the tooth numbering is done according to what and which diagnoses look like what:

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
{% include gallery images=images caption="Figure 4 - Logic of intersections "%}
<b>

It isnt finish yer either lol. In order to make this a user-friendly project, we designed an interface with the help of Flask and with this interface we made an interactive site with the user. In our site we run in local, there is a survey page where we can get feedback from the user, and a page where we can get x-rays from the user and return estimates. As a classic website, there is a homepage, about and thanks section. I guess it will be best to show the screenshots.

**&#8594; Homepage**

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118706901-939ef880-b822-11eb-8dda-9a526570fa7f.png
	https://user-images.githubusercontent.com/56072259/118706902-94d02580-b822-11eb-9de7-0a99e120454a.png
	https://user-images.githubusercontent.com/56072259/118706906-96015280-b822-11eb-8b27-ded3b289bf4c.png
{% endcapture %}
{% include gallery images=images cols=3 caption="Figure 5 - Homepage "%}
<b>

**&#8594; How it Works?**

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118706910-9699e900-b822-11eb-8bb7-6437139e5161.png
	https://user-images.githubusercontent.com/56072259/118706913-97327f80-b822-11eb-9016-4f0d6c6eed54.png
	https://user-images.githubusercontent.com/56072259/118706919-9863ac80-b822-11eb-93fe-06ec16b686ea.png
{% endcapture %}
{% include gallery images=images cols=3 caption="Figure 6 - How it Works? "%}
<b>


**&#8594; Survey Page**

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118706922-98fc4300-b822-11eb-8336-160bf7f6cba2.png
	https://user-images.githubusercontent.com/56072259/118706923-9994d980-b822-11eb-8ebb-51039acac3c3.png
{% endcapture %}
{% include gallery images=images cols=2 caption="Figure 7 - Survey Page "%}
<b>

**&#8594; Thanks Page**

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118706926-9994d980-b822-11eb-8b3b-4c11a60bf0f9.png
{% endcapture %}
{% include gallery images=images caption="Figure 8 - Thanks Page "%}
<b>

**&#8594; Predict Page**

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118706896-93066200-b822-11eb-8d4b-6d122cf0f8fb.png
{% endcapture %}
{% include gallery images=images caption="Figure 8 - Thanks Page "%}
<b>

I am aware that I cannot give much information about the code but I cannot share them yet because the incorporation has taken place in line with this project. However, if you have any questions, I would be happy to help. You can [contact me here](https://www.linkedin.com/in/semih-gulum/).



## Thanks for reading my project!