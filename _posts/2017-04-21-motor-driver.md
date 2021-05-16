---
layout: post
title: "3 Phase Asynchronous Motor Driver Project"
date: 2012-05-25
excerpt: "Motor Drivers."
tags: [sample post, readability, test]
comments: true
---

<center><b>Semih GULUM</b>    Mechatronic Engineer </center>

## List of Materials
* Transformer 24VAC 4W
* Button x4
* 1K Ω Potentiometer
* LED Diode
* MOC3021 Optocoupler
* BTA12-6008 Triac
* DF10 Bridge Diode Rectifier
* 2N3904 Transistor
* 12V Bulb
* Various Values of Resistors (100 Ω, 220 Ω, 330 Ω x4, 10k Ω, 22k Ω, 220k Ω x2, 1k Ω)


## Explanation the Project

One of the 3-phase asynchronous motor starting methods widely used in the industry is the soft-starter method.

In the soft start method, voltage control is performed with two different approaches: phase angle control and zero crossing control.

Figure 1 below shows the waveforms observed at the output when AC supply voltage alternations are transferred to the output at 25%, 50%, 75% and 100% rates. The areas that work in the instruments are filled with blue color. In areas not filled with blue, the output voltage is 0V.

<b>

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118392206-0fd9e600-b641-11eb-9f05-9264298d9c2a.png
{% endcapture %}
{% include gallery images=images caption="Figure 1 - Phase Angle Control"%}

<b>

Zero crossing control, which is another soft starting approach, is also called "burst fire control" in the literature. For example, as shown in the figure below, when the rate of 25% is selected, only 1 of every 4 full sine waves coming from the AC power line is sent to the output. A kind of batch model is applied. As a result, the engine runs with 25% power. In Figure 2 below, the waveforms obtained at the output in the zero-crossing control approach with 25%, 50%, 75% and 100% ratios are shown.

<b>

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118392451-79a6bf80-b642-11eb-8fe4-d612cf80a10d.png
{% endcapture %}
{% include gallery images=images caption="Figure 2 - Burst Fire Control"%}

<b>

That's enough theoretical enough, now we can go into practice and set up our circuit. First, let's draw our circuit using the program called proteus. We will observe the frequency changes here on an LED. For this, we will have 4 buttons that will perform start, stop, phase age control and burst fire control functions.

<b>

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118392627-326cfe80-b643-11eb-98e1-19f21689db27.jpg
{% endcapture %}
{% include gallery images=images caption="Figure 3 - Proteus Simulation"%}

<b>

## Parts of the Circuit Stated in the Simulation

** &#8594; Zero Cross Control Circuit:** It is the circuit used to detect every decline of the signal coming from the AC signal source to zero. A bridge, 4 resistors of various values ​​and a transistor are used in the circuit. The circuit changes the output level (0-1) at each zero crossing. This output is connected to the microcontroller as an interrupt to detect zero crossings.

** &#8594; Motor Driver Circuit:** It is the circuit in which the motor (the lamp in the established circuit) is driven. An optocoupler, 3 resistors of various values ​​and a triac are used in the circuit. By using triac instead of thyristor, it is ensured that both alternans of the AC signal pass.

** &#8594; Microcontroller:** It is the element that provides control of the circuit. The stop button is taken as interrupt from the buttons and it has been detected on its rising edge. The zero-cross control circuit from the inputs is also taken as an interrupt.

** &#8594; AC Signal and Transformer:** It is the part where the AC signal is taken from the source and drawn to usable levels in the circuit.
Oscilloscope: It is the element used to monitor the signals passing through various parts of the circuit.

**&#8594; Buttons:** 4 pieces as start, stop, phase angle control and zero crossing control. While the start-stop circuit starts and stops, the other two buttons determine which control method the lamp will be driven by.

**&#8594; Potentiometer: ** The potentiometer, which is the element in which the change time of the brightness levels of the lamp is adjusted, is connected to the analog input of the microcontroller.

**&#8594; Mode LED:** It is the output element used to observe the modes in which the lamp is driven. It operates as 1 in phase angle control mode and 0 in zero crossing control mode.

While the circuit is set up, since there is no earth connection in the simulation, the negative alternans at the bridge output are also rectified. Therefore, since the transistor cannot be triggered at each alternans transition, it remains in the cut and goes to the microcontroller 5V. Thus, a signal is formed at the alternans transitions, ie at the zero points. This is how it works in real circuit, so instead of the "CHANGE" mode in the code, the "RISING" mode is used to detect the edge.

The signals for the mentioned situation are given below.

<b>

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118393427-c5a83300-b647-11eb-97cc-7a82b6269947.png
{% endcapture %}
{% include gallery images=images caption="Figure 4 - Waves"%}

<b>

One of the Arduino's digital outputs is used to turn the lamp on. The optocoupler is triggered by pulses generated from here. The reason for using optocouplers is to aim to provide isolation in the circuit. In this way, malfunctions of the circuit elements due to possible overvoltages are prevented. The triggered optocoupler also conducts the triac connected at its output. Here, by using a triac instead of a thyristor, the negative alternans coming from the AC source is also provided to pass through the lamp. When triggering the optocoupler, the required switching time for the phase shift mode and the number of waves required for the zero crossing mode are considered for both modes.

<b>

{% capture images %}
	https://user-images.githubusercontent.com/56072259/118393517-46ffc580-b648-11eb-8bfa-e591add8ba4d.jpg
{% endcapture %}
{% include gallery images=images caption="Figure 5 - Circuit"%}

<b>

## Arduino Code:
```arduino

//Interrupt fonksiyonları:
void interrupt();
void stopfunc();

//Inputlar ve pinleri:
const byte startbutton = 4; // start butonu
const byte fazbutton = 5; // faz kaydırma modu butonu
const byte sifirbutton = 6; // sıfır geçiş modu butonu
const int potpin = A0; //potansiyometre için analog giriş pini tanımlanır

//Outputlar ve pinleri:
const byte ledPin = 8; //sıfır geçiş = 0, faz kaydırma = 1
const byte lamp = 12; //lamba sürme için çıkış pini

//Değişkenler:
int pottime =0; //potansiyometreden okunan değere göre mapping işlemi için
int count =0; //sıfır geçişlerin sayılması için değişken
int potcount=0; //her sıfır geçişi için counter (potansiyometre süre hesabında kullanılır)
int offtime = 10; //faz kaydırma modu için sıfırda kalma süresi 
int ref=0;  //sıfır kontrol modunda geçen dalga sayısı için
float potval; // potansiyometreden okunan değer
int motorrun = 0; // motor start/stop durumu
int mod=2; // sürme modu için değişken
int led = 0; //mod ledi başta sönük
int startstate = 0; // start buton durumu
int fazstate = 0;  // faz kontrol modu buton durumu
int sifirstate = 0; // sıfır geçiş kontrol modu buton durumu

//Interruptlar:
const byte interruptPin = 2; // sıfırların sayılması için interrupt pini ataması
const byte stopbutton = 3; // stop butonu için interrupt pini ataması

void setup() {

  //pinlerin giriş/çıkış özellikleri tanımlanır:
pinMode(potpin, INPUT); 
pinMode(stopbutton, INPUT); 
pinMode(startbutton, INPUT);
pinMode(fazbutton, INPUT);
pinMode(sifirbutton, INPUT);
pinMode(ledPin, OUTPUT);
pinMode(lamp, OUTPUT);

//sıfır geçiş için her yükselen kenarda tetiklenen interrupt tanımlanır:
attachInterrupt(digitalPinToInterrupt(interruptPin), interrupt, RISING);

//stop butonu için yükselen kenarda tetiklenen interrupt tanımlanır:
attachInterrupt(digitalPinToInterrupt(stopbutton), stopfunc, RISING);
}

void loop() {

//dijital inputların okunması:
startstate = digitalRead(startbutton);
fazstate = digitalRead(fazbutton);
sifirstate = digitalRead(sifirbutton);

//dijital çıkışların sıfırlanması:
digitalWrite(lamp, LOW);
digitalWrite(ledPin, LOW);
  
if(startstate == HIGH){ //start butonuna basılmışsa
motorrun = 1; //motor durumu değişimi (on)
}

if (motorrun==1){ //start butonuna basılmışsa

if (fazstate == HIGH){ // faz kaydırma modu seçilmişse
led = 1; //mod durum ledi
mod = 1; 
}

else if(sifirstate == HIGH){ // sıfır geçiş modu seçilmişse
led = 0; //mod durum ledi
mod =0;
}

digitalWrite(ledPin, led); // sürme modu için led durumu
potval = analogRead(potpin); //potansiyometreden okunan değer
pottime = map(potval, 0, 1023, 10, 1000); //potansiyometreden okunan değerin süre 
//değeri (ms) olarak map edilmesi
}

else if(motorrun==0){ //stop butonuna basılmışsa
digitalWrite(ledPin, led); //led durumu güncellenmesi
}
}
void interrupt() { //sıfır geçişlerin algılanması için interrupt fonksiyonu

//pottime değerinin en yakın 10 tabanlı sayıya yuvarlanması (10’ar 10’ar artış için):
pottime = (pottime + 5)/10;
pottime = 10*pottime;

if(motorrun==1& (mod==1| mod==0)){ //motor çalışıyorsa ve mod seçilmişse
potcount++; // her sıfır geçişinde counter 1 arttırılsın
if (potcount*10==pottime){ //potansiyometreden okunan zaman ile counter 
//karşılaştırması
if (offtime!=0) {offtime-=1;} //offtime değerinin azaltılması
if (ref!=0) {ref+=2;} // ref (dalga sayısı) değerinin arttırılması
potcount=0; //counter sıfırlanması
}
}

else if(motorrun==0 & (mod==1 | mod==0)){ //stop butonuna basılmışsa ve mod 
//seçilmişse
potcount++; // her sıfırda counter 1 arttırılsın
if (potcount*10==pottime){ //potansiyometreden okunan zaman ile counter 
//karşılaştırması
if (offtime!=10) {offtime+=1;} //offtime değerinin arttırılması

if (ref!=20) {ref-=2;} // ref (dalga sayısı) değerinin azaltılması

if (offtime==10 | ref == 20){ //çıkışı sıfır yapacak değerlerden birine ulaşılmışsa
mod=2; // mod değeri resetlensin
led =0; // led kapatılsın
}

potcount=0; // counter sıfırlansın
}
}

if(mod==1){ // faz kaydırma modu için

if (offtime > 0 & offtime < 10) {
delayMicroseconds(offtime * 1000); // offtime kadar erteleme
digitalWrite(lamp, HIGH); //çıkış pini tetikleme
delayMicroseconds(250);
digitalWrite(lamp, LOW); //çıkış pini 0'a çekiliş  
}


else if (offtime == 0) {
digitalWrite(lamp, HIGH); //çıkış pini tetikleme
delayMicroseconds(500);
digitalWrite(lamp, LOW); //çıkış pini 0'a çekiliş
} 
}

if(mod==0){  // sıfır geçiş modu için
count++; //sıfır geçiş için sayıcı değişkeni

if (count==21){ //10 tam dalga sayılmışsa
count = 1; //sayıcı=1 olarak kabul edilip (sıfırlanıp) işleme devam edilir
}

if(count <= ref){ // counter o anki dalga sayısından küçük ve eşitse
digitalWrite(lamp, HIGH); // çıkış pini tetikleme
delayMicroseconds(600);
digitalWrite(lamp, LOW); //çıkış pini 0'a çekiliş   
}
}
}
void stopfunc(){ // stop butonuna basılmışsa kesme yaratacak interrupt fonksiyonu
  motorrun = 0; // durum değişimi
}


```

Also, if you want to watch the video prepared by our project group, [you can click here](https://www.youtube.com/watch?v=0Dsjd2Zoi54). 

## Thanks for reading my project!