from PIL import Image, ImageDraw, ImageFilter


#im = Image.open("6MzjjikJ_400x400.jpg")
for i in range(50):
    im = Image.open("30.png")

    im1 = im.filter(ImageFilter.BLUR)
    img = Image.new('RGB', (6000, 6000), color='black')
    img2 = Image.new('RGB', (4000, 4000), color='grey')
    draw = ImageDraw.Draw(im)
    draw.line((10, 20, 30, 40, 50, 60, 70, 80, 90, 0) + im.size, fill=628)
    draw.line((202, 200, 666, 90), fill=388)
    draw.line((302, 666, 666, 190), fill=488)
    draw.line((402, 666, 666, 290), fill=358)
    draw.line((502, 666, 666, 390), fill=348)
    draw.line((602, 666, 666, 490), fill=111)
    im1 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    im6 = im1.filter(ImageFilter.BLUR)
    im5 = im6.filter(ImageFilter.EMBOSS)
    im7 = im5.filter(ImageFilter.CONTOUR)
    im8 = im7.filter(ImageFilter.EMBOSS)
    im2 = im.filter(ImageFilter.MinFilter(3))
    im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
    im8.save('30.png')
