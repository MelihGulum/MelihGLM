from PIL import Image
import os
import PIL

paths = os.listdir()
current_path = os.getcwd()


for path in paths: 
	if path.endswith(".png"):
		image = Image.open(path)
		print(image.size)
		
		
		saved_path = str(current_path) +"/" + str(path)
		print(saved_path)
	
		resized_image = image.resize((1600,770))
		resized_image.save(saved_path)
