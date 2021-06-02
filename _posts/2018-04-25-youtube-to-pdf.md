---
layout: post
title: Youtube to PDF
date: 2012-05-22
excerpt: Simple PDF Creator
comments: true
---
    
<center><b>Semih GULUM</b>    Mechatronic Engineer </center>

## List of libraries used
* pytube
* imagehash
* os
* time
* re
* PIL
* numpy
* OpenCV


## Explanation the Project

At AdresGezgini, we would set our own topics and have theoretical discussions on these topics at the weekends. Our topics were on machine learning and deep learning. Emre Taşar, who was responsible for us during our internship, was our moderator. Usually, he would tell us about it and we would try to find the places that stuck in our minds by discussing.
However, since our weeks were very busy, we did not have a pdf to discuss and take notes on some weekends. I made such a project to automate this.

The first step is to download the video from youtube. Then handle the video frame by frame. The point we need to pay attention to in this project is not every frame, but only frames that are different from the previous one. We set a threshold value to indicate the difference. After that, we can convert the remaining frames into pdf.

I leave an example from the youtube channel "StatQuest with Josh Starmer" so that you can see the output.

[The Video](https://www.youtube.com/watch?v=fHLhBnmwUM0)


* <p><a href="http://docs.google.com/gview?url=https://github.com/semihstp/semihstp.github.io/files/6582144/StatQuest_.Boxplots.Clearly.Explained.5.pdf" target="_blank">And the Output</a></p>

If you wanna jump the awesome intro you can simply delete firstly frames before converting the pdf. 
You can find the codes in my [github repo](https://github.com/semihstp).

## Thanks for reading my project!