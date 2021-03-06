import os
from PIL import Image

ALGORITHMS = [Image.ADAPTIVE, Image.NEAREST, Image.ANTIALIAS, Image.BICUBIC, Image.BILINEAR, Image.AFFINE, Image.QUAD]

input_path = raw_input("Path to images: ")                     
output_path = raw_input("Output path: ")
new_size = (input("Width: "),input("Height: ")
print "Which algorithm should I use?"
for i in ALGORITHMS: print i,                     
algorithm = raw_input()

for imagefile in os.listdir(input_path):
    base = imagefile
    imagefile = input_path + '\\' + imagefile
    print "Resizing.. " + base
    img = Image.open(imagefile, "r")
    print img.size
    d = img.resize(new_size,algorithm)
    out = file(output_path + "\\" + base, "w")
    try:
        d.save(out)
    finally:
        out.close()
print "Done"

