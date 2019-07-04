from PIL import Image

user_input = input("Which photo do you want to downsize?: ")
im = Image.open(user_input)
width, height = im.size
scaledown = 0.5
new_width = int(round(width*scaledown))
new_height = int(round(height*scaledown))
im = im.resize((new_width, new_height), Image.ANTIALIAS)
im.save(user_input[:-4]+"_half_compressed.jpg")
