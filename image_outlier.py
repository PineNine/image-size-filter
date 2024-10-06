# the purpose is to move files depending on image size
# maybe not the best way but...
import os
from PIL import Image

cwd = os.getcwd()
src = os.path.join(cwd, "images")
dest = os.path.join(cwd, "rejects")

def filter():
    # grabs all file names in folder
    files = os.listdir(src)

    image_area = []
    for i in files:
        filepath = os.path.join(src, i)
        img = Image.open(filepath)
        w = img.width
        h = img.height
        
        # getting the area of the image
        area = w * h
        image_area.append([area, i])

    image_area.sort()

    q1_locator = round((0.25) * (len(image_area)))
    Q1 = image_area[q1_locator-1][0]

    q3_locator = round((0.75) * (len(image_area)))
    Q3 = image_area[q3_locator-1][0]

    IQR  = Q3 - Q1

    uppper_boundary = Q3 + (1.5 * IQR)

    lower_boundary = Q1 - (1.5 * IQR)

    # grabs unwanted images
    filtered = [ i[1] for i in image_area if (lower_boundary <= i[0]) and (i[0] <= uppper_boundary) ]
    return filtered


def move():
    # returns list of images that 
    files = filter()
    for i in files:
        src_path = os.path.join(src, i)
        dest_path = os.path.join(dest, i)
        os.rename(src_path, dest_path)
move()