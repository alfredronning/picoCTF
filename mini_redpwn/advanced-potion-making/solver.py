from PIL import Image
from collections import defaultdict

pixel_count = defaultdict(int)
im = Image.open("advanced-potion-making.png")
pixels = im.load()
im_out = Image.new(im.mode, im.size)
output = im_out.load()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        #pixelcounts are {(238, 18, 29): 2973494, (239, 18, 29): 57791, (238, 17, 28): 4193, (237, 17, 27): 42}
        pixel = pixels[i, j]
        output[i, j] = ((pixel[0]-238)*255, (pixel[1]-17)*255, (pixel[2]-27)*128)

im_out.save("out.png")
im_out.close()

