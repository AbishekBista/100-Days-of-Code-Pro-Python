import colorgram

colors = colorgram.extract('painting.jpg', 30)
color_list = []
for color in colors:
    red = color.rgb[0]
    green = color.rgb[1]
    blue = color.rgb[2]
    color_list.append((red, green, blue))

print(color_list)
