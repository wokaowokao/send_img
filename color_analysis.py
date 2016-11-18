import colorsys
import os
from PIL import ImageDraw
from PIL import Image
def get_dominant_color(image):
#颜色模式转换，以便输出rgb颜色值
    image = image.convert('RGBA')
#生成缩略图，减少计算量，减小cpu压力
    image.thumbnail((200, 200))
    # print(image.size)
    #foo = colorsys.rgb_to_hsv( 60,  61,  62)
    #print(foo)
    #foo = image.getcolors(image.size[0] * image.size[1]);
    #print(foo)
    max_score = 0
    dominant_color = None
    color = image.getcolors(image.size[0] * image.size[1])
    color.sort(key=lambda d: d[0],reverse=True)
    return color[:5]
    #for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        # 跳过纯黑色dd
        # if a == 0:
        #     continue
        # saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
        # y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        # y = (y - 16.0) / (235 - 16)
        # # 忽略高亮色
        # if y > 0.9:
        #     continue
        # # Calculate the score, preferring highly saturated colors.
        # # Add 0.1 to the saturation so we don't completely ignore grayscale
        # # colors by multiplying the count by zero, but still give them a low
        # # weight.
        # score = (saturation + 0.1) * count
    #     if count > max_score:
    #         max_score = count
    #         dominant_color = (r, g, b)
    # return dominant_color

color = get_dominant_color(Image.open('1479210728685.jpg'))
im = Image.new ('RGBA', (100, 20), (255, 255, 255))
 
print(color)

 
draw = ImageDraw.Draw(im)
draw.rectangle((0, 0, 20, 20), fill=(color[0][1]))
draw.rectangle((20, 0, 40, 20), fill=(color[1][1]))
draw.rectangle((40, 0, 60, 20), fill=(color[2][1]))
draw.rectangle((60, 0, 80, 20), fill=(color[3][1]))
draw.rectangle((80, 0, 100, 20), fill=(color[4][1]))
im.show()
os.system('pause')