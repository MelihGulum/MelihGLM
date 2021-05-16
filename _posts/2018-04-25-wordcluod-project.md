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


## Explanation the Project

In this project, i tried to track my water bottle. As you can see above i didn't use any deep learning library. It's easy and funny project. But if you don't find the right threshold value, it can turn into an annoying situation. I used trackbars to avoid this. So let's see the code!

```python
import os
import pandas as pd
import re
import wordcloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
from matplotlib.pyplot import figure
import cv2
from google.colab.patches import cv2_imshow

books_path ="/content/drive/MyDrive/Colab Notebooks/dosyalar/harrypotter" 
books_folder = os.listdir(books_path)

#[f(x) for x in sequence if condition]
books = [books for books in books_folder if books.endswith(".txt") ]

long_string = []
for book in books:
  path = books_path + "/" + str(book)
  with open(path,'r') as f:
    for line in f:
       long_string.append("".join(line))

#Clean the data
def cleanText(input_sentence):
  tmp= [word.replace('A','a') for word in input_sentence.split(' ')]
  tmp= [word.lower() for word in tmp]
  tmp= [word.replace('i̇','i') for word in tmp]
  tmp = [re.sub('[^A-Za-z0-9ğüşıçöiâî]+', ' ', word) for word in tmp]
  tmp = [word.strip(' ') for word in tmp]
  tmp1 =' '.join(tmp)

  return tmp1

def listToString(s): 
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

long_string = cleanText(long_string)

plt.imshow(wordcloud_example, interpolation='bilinear')
plt.axis("off")
plt.show()
```
<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118406706-a8925500-b685-11eb-94ac-dc603614f89f.png
{% endcapture %}
{% include gallery images=images caption="Figure 1 - First Wordluod Sample"%}
<b>
But it isnt give us a good plot. We have words like "said, ve, take, got, re". These words don't mean anything to us. So we gotta throw these. Let's drop both the meaningless words and the words we dont want to show up.

```python
stopwords = set(wordcloud.STOPWORDS)
stopwords.add("page")
stopwords.add("said")
stopwords.add("ve")
stopwords.add("on")
stopwords.add("take")
stopwords.add("re")
stopwords.add("got")
wordcloud_example = wordcloud.WordCloud().generate(long_string)

wordcloud_example = wordcloud.WordCloud(stopwords=stopwords).generate(long_string)

plt.imshow(wordcloud_example, interpolation='bilinear')
plt.axis("off")
plt.show()
```
<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118406707-a8925500-b685-11eb-9367-1dec8e8a051f.png
{% endcapture %}
{% include gallery images=images caption="Figure 2 - With Remove the Stop Words"%}
<b>

## Let's try with an image!
```python
harry_img_path = books_path + "/hp.jpg"
mask = np.array(Image.open(harry_img_path))

wordcloud_example = wordcloud.WordCloud(stopwords=stopwords, mask=mask, background_color="white").generate(long_string)

figure(dpi=200)
plt.imshow(wordcloud_example)
plt.axis("off")
plt.show()

#For save the plot img 
#wordcloud_example.to_file("wordcloud.png")
```

<b>
{% capture images %}
	https://user-images.githubusercontent.com/56072259/118406708-a9c38200-b685-11eb-8bfe-92b5ad7234d7.png
	https://user-images.githubusercontent.com/56072259/118406705-a62ffb00-b685-11eb-86c3-6bd23664eea5.png
{% endcapture %}
{% include gallery images=images cols=2 caption="Figure 3 - With a random black and white image"%}
<b>

Also, if you want to watch the video prepared by our project group, [you can click here](https://www.youtube.com/watch?v=0Dsjd2Zoi54). 

## Thanks for reading my project!