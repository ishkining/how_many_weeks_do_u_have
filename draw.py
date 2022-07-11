from PIL import Image, ImageDraw, ImageFont

width = 1980
height = 1024
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

will_die = 45
step_x = width // 53
step_y = height // will_die


for iterator_x in range(1, 53):
    draw.text((iterator_x * step_x + (step_x * 0.15), 0), str(iterator_x),
              font=ImageFont.truetype("arial", 12), fill=(0, 0, 0))
    counter = 0
    for iterator_y in range(0, will_die):
        if iterator_y == counter and counter != 0:
            draw.text((5, iterator_y * step_y + (step_y * 0.15)), str(iterator_y),
                      font=ImageFont.truetype("arial", 12), fill=(0, 0, 0))
        draw.ellipse((0 + iterator_x*step_x, 0 + iterator_y*step_y + 20, 20 + iterator_x*step_x, 20 + iterator_y*step_y + 20),
                     fill=(255, 255, 255), outline=(0, 0, 0))
        counter += 1
        if counter == will_die:
            draw.text((5, iterator_y * step_y + (step_y * 1.15)), str(iterator_y + 1),
                      font=ImageFont.truetype("arial", 12), fill=(0, 0, 0))
    counter = 0

image.show()
image.save('image.jpg', quality=95)
