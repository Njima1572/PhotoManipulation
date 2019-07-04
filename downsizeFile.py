from PIL import Image
import os

PATH = "./Compressed"
if not os.path.exists(PATH):
    os.mkdir(PATH)

for filename in os.listdir("."):
    if filename.endswith("jpg") or filename.endswith("JPG"):

        im = Image.open(filename)
        width, height = im.size
        scaledown = 0.5
        new_width = int(round(width*scaledown))
        new_height = int(round(height*scaledown))
        im = im.resize((new_width, new_height), Image.ANTIALIAS)
        im.save(PATH + "/" + filename[:-4]+"_half_compressed.jpg")
        print(filename + " compressed!")
    else:
        continue

print("Done!! Look for a file called \"Compressed\"")
