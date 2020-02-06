# colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'darkgreen']
# with open('E:/Downloads/rainbow_colors.txt', 'w') as rainbow_colors:
#     for color in colors_list:
#         print(color, file=rainbow_colors)

colors_list = []
with open('E:/Downloads/rainbow_colors.txt', 'r') as rainbow_colors:
    for color in rainbow_colors:
        colors_list.append(color.strip('\n')) # strip - обрезает в строке то, что надо нам обрезать

print(colors_list)

with open('E:/Downloads/rainbow_colors.txt', 'a') as rainbow_colors:
    print('dark green', file=rainbow_colors)
    print('dark blue', file=rainbow_colors)

colors_list = []
with open('E:/Downloads/rainbow_colors.txt', 'r') as rainbow_colors:
    for color in rainbow_colors:
        colors_list.append(color.strip('\n')) # strip - обрезает в строке то, что надо нам обрезать

print(colors_list)