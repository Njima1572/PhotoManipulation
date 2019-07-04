# PhotoManipulation
Useful photo manipulation for posting somewhere e.g. blog

1. `downsizeFile.py`
  - run `python3 downsizeFile.py` in a directory with photos that you want to downsize
  - After the run, it will make a folder called "Compressed" and this folder should have all the pictures with quarter of the original size.
  - As of now, this only works for jpg

2. `pixelonly.py`
  - This removes all the unnecessary metadata of the picture. Should bring down the file size at a reasonable


3. `compresssize.py`
  - It does a same thing as `downsizeFile`, but only applies to a single file that you chose.

4. `photosToJpg.py`
  - Asks you to choose a photo to convert to jpg. When the jpg is generated, you would probably be able to run the other programs in here.

