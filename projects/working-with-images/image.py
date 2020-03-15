from PIL import Image, ImageFilter

img = Image.open("./pokodex/original.jpg")
print(img)
print(img.format)
print(img.mode)
print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
crooked = filtered_img.rotate(90)
resized = img.resize((300, 300))
crooked.save('original_blur.png', 'png')
resized.save('original_resize.png', 'png')
# filtered_img.show()

# Exercise
img_astro = Image.open('./astro.jpg')
print(img_astro.size)
# thumbnail keeps aspect ratio, but doesnt return samething
img_astro.thumbnail((400, 400))
img_astro.save('thumbnail.jpg', 'jpeg')
print(img_astro.size)
