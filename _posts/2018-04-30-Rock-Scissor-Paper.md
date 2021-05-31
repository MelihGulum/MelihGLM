---
layout: post
title: Robot Hand, Rock Scissors Paper!
date: 2012-05-31
excerpt: "Magical Glove!"
comments: true
---
    
<center><b>Semih GULUM</b>    Mechatronic Engineer </center>

## List of Materials
* Servo motors
* Flat board
* Sleeve length pipe
* Parachute rope
* Foam suitable for hand color
* Silicone gun
* 1.5-2m pipe with a blind finger diameter
* Snap BladeKknife
* An old t-shirt
* Switch
* Conductor wire
* Board

## Materials needed to make our own sensor (cause its too expensive):
* Soldering iron machine
* Scissors
* Ruler
* Macarons
* Copper plate
* Velostat
* Conductor wire
* Lighter

{% capture images %}
	https://user-images.githubusercontent.com/56072259/120176890-7994eb00-c210-11eb-8476-8403fb5c3bb1.jpeg
	https://user-images.githubusercontent.com/56072259/120176894-7ac61800-c210-11eb-947f-00554663f6c3.jpeg
{% endcapture %}
{% include gallery images=images cols=2 caption="Figure 1"%}
<b>

https://user-images.githubusercontent.com/56072259/120176901-7bf74500-c210-11eb-909a-038dcca510d2.jpeg
## Explanation the Project

As a microcontroller project, I developed a robot arm that can play rock paper scissors. This arm can perform the necessary hand functions with the help of servo motors and ropes. It can also be controlled with a glove. I glued it with a sponge to add a more human-like feel to the robot hand.

{% capture images %}
	https://user-images.githubusercontent.com/56072259/120194839-cd123380-c226-11eb-8b9f-addc2b733340.jpeg
{% endcapture %}
{% include gallery images=images caption="Figure 2 - Robot Hand "%}
<b>

I can move the fingers with the help of the black parachute rope and the servo motor. When the servo motor rotates 90 degrees and 180 degrees, the rope turns with it and the fingers are closed.

{% capture images %}
	https://user-images.githubusercontent.com/56072259/120194842-cdaaca00-c226-11eb-8e35-4c5b3a85ef2c.jpeg
{% endcapture %}
{% include gallery images=images caption="Figure 3 - Servo Motors "%}
<b>

It has two modes and can be controlled with a switch. In the first mode, the glove repeats what it does. In the second mode, it counts down with the help of the led screen and at the end of the countdown, it rotates a random rock paper scissors. At the same time, it reads the data from the glove and adds it to the led score as a point for whoever wins.

{% capture images %}
	https://user-images.githubusercontent.com/56072259/120176909-7c8fdb80-c210-11eb-90c5-5b5c9aeff357.jpeg
	https://user-images.githubusercontent.com/56072259/120176850-700b8300-c210-11eb-8246-2b99bb37a413.jpeg
{% endcapture %}
{% include gallery images=images cols=2 caption="Figure 4 "%}
<b>

We get such a view.

{% capture images %}
	https://user-images.githubusercontent.com/56072259/120176854-713cb000-c210-11eb-99ed-caf577cb8b85.jpeg
{% endcapture %}
{% include gallery images=images cols=1 caption="Figure 5 "%}
<b>


In the glove, I used a sensor whose resistance changes in proportion to bending. Therefore, when I close my finger, the microcontroller know what I am doing with resistance value.

{% capture images %}
	https://user-images.githubusercontent.com/56072259/120176859-71d54680-c210-11eb-8229-9c93f60f1193.jpeg
	https://user-images.githubusercontent.com/56072259/120176863-726ddd00-c210-11eb-9926-48cc3ae2dd18.jpeg
{% endcapture %}
{% include gallery images=images cols=2 caption="Figure 6 "%}
<b>

Finally, I sewed a sleeve from my old t-shirt to get rid of the ugly look of the cables and give it a humanoid look.

{% capture images %}
	https://user-images.githubusercontent.com/56072259/120193913-a4d60500-c225-11eb-9ffb-579a865695b5.png
{% endcapture %}
{% include gallery images=images cols=1 caption="Figure 7 "%}
<b>

If you wanna talk to me about the project or the code, [you can reach me here].(https://www.linkedin.com/in/semih-gulum/).

## Thanks for reading my project!