from PIL import Image

user_input = input("Which photo do you want to convert?: ")
im = Image.open(user_input)
im.save(user_input[:-4]+"_compressed.jpg")
