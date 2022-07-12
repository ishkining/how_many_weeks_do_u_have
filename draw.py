from PIL import Image, ImageDraw, ImageFont


def get_dayOfweek(day, month, year):
    temp = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    return ((year + int(year / 4) - int(year / 100) + int(year / 400) + temp[month-1] + day) % 7)


def get_differnceOfDays(day1, month1, year1, day2, month2, year2):
    how_many_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    number_days_date1 = year1 * 365 + day1
    for iterator in range(0, month1 - 1):
        number_days_date1 += how_many_days_in_month[iterator]

    number_days_date1 += int((year1 - 1 if month1 <= 2 else year1) / 4) - int(
        (year1 - 1 if month1 <= 2 else year1) / 100) + int((year1 - 1 if month1 <= 2 else year1) / 400)

    number_days_date2 = year2 * 365 + day2
    for iterator in range(0, month2 - 1):
        number_days_date2 += how_many_days_in_month[iterator]

    number_days_date2 += int((year2 - 1 if month2 <= 2 else year2) / 4) - int(
        (year2 - 1 if month2 <= 2 else year2) / 100) + int((year2 - 1 if month2 <= 2 else year2) / 400)

    return (number_days_date2 - number_days_date1)


width = 1980
height = 1024
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

will_die = 45
step_x = width // 53
step_y = height // will_die

# age_choice = int(input('Choose age:\n'))
# start_week = int(input('Choose starting week:\n'))
# end_week = int(input('Choose ending week:\n'))

start_day = int(input('Type start day:\n'))
start_month = int(input('Type start month:\n'))
start_year = int(input('Type start year:\n'))

print(get_dayOfweek(start_day, start_month, start_year))
print(get_differnceOfDays(1, 1, 2022, start_day, start_month, start_year))


# for iterator_x in range(1, 53):
#     draw.text((iterator_x * step_x + (step_x * 0.15), 0), str(iterator_x),
#               font=ImageFont.truetype("arial", 12), fill=(0, 0, 0))
#     counter = 0
#     for iterator_y in range(0, will_die):
#         if iterator_y == counter and counter != 0:
#             draw.text((5, iterator_y * step_y + (step_y * 0.15)), str(iterator_y),
#                       font=ImageFont.truetype("arial", 12), fill=(0, 0, 0))
#         if (age_choice == iterator_y) and (iterator_x >= start_week and iterator_x < end_week):
#             draw.ellipse((0 + iterator_x*step_x, 0 + iterator_y*step_y + 20, 20 + iterator_x*step_x, 20 + iterator_y*step_y + 20),
#                          fill=(255, 0, 0), outline=(0, 0, 0))
#         else:
#             draw.ellipse((0 + iterator_x*step_x, 0 + iterator_y*step_y + 20, 20 + iterator_x*step_x, 20 + iterator_y*step_y + 20),
#                          fill=(255, 255, 255), outline=(0, 0, 0))
#         counter += 1
#         if counter == will_die:
#             draw.text((5, iterator_y * step_y + (step_y * 1.15)), str(iterator_y + 1),
#                       font=ImageFont.truetype("arial", 12), fill=(0, 0, 0))
#     counter = 0

# image.show()
# image.save('image.jpg', quality=95)
