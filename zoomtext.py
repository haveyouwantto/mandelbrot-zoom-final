import subprocess

import math

from PIL import Image, ImageDraw, ImageFont


fontname = 'LargeFontMono.ttf'
exp_font = ImageFont.truetype(fontname, 48)
zooms_font = ImageFont.truetype(fontname, 32)
with open('tl.csv',) as csv:
    p = subprocess.Popen('ffmpeg -f rawvideo -s 1920x1080 -pix_fmt rgb24 -r 60 -i - -crf 15 -y test.mkv',
                         shell=True, stdin=subprocess.PIPE)
    line = csv.readline()
    while line != '':
        args = line.split(',')
        try:
            zooms = float(args[1]) - 5
            log10zoom = math.log(2, 10)*zooms
            zoomtext = 'ZOOM: {0:.2f}E+{1:d}'.format(
                10**(log10zoom-int(log10zoom)), int(log10zoom)) if log10zoom >= 7 else 'ZOOM: {0:.2f}'.format(10 ** log10zoom)
            z2 = '{0:.2f} zooms'.format(zooms)
            img = Image.new('RGBA', (1920, 1080), '#00cc00')
            draw = ImageDraw.Draw(img)

            color = (0, 0xcc//2, 0, 0x80)
            lsx, lsy = exp_font.getsize(zoomtext)
            #draw.rectangle((8, 8, lsx+24, lsy+24), fill=color)
            draw.text((20, 20), zoomtext, "#000000", exp_font)
            draw.text((16, 16), zoomtext, "#ffffff", exp_font)

            rsx, rsy = zooms_font.getsize(z2)
            draw.text((1909-rsx, 1069-rsy), z2, "#000000", zooms_font)
            draw.text((1906-rsx, 1066-rsy), z2, "#ffffff", zooms_font)

            p.stdin.write(img.convert("RGB").tobytes())
        except IndexError as e:
            pass
        except ValueError as e:
            print(e)
        line = csv.readline()
