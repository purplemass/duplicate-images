import os
import sys
import shutil
import piexif


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


config = {
    'frames': 16,
    'batches': 1,
    'source': '/sayfromage/photos_bullet_16_500/',
    'target': '/sayfromage/photos_bullet_16_5000/',
    'overlay': True,
    'overlay-quality': 95,
    'overwrite': True,
    'font': ImageFont.truetype("Courier New Bold.ttf", 100)
}


def scan_folder():
    current_files = list()
    for my_file in os.listdir(config['source']):
        if is_file_valid(my_file):
            current_files.append(my_file)
    return current_files


def is_file_valid(my_file):
    if not my_file.startswith('.') and \
        (".jpg" in my_file or ".JPG" in my_file or
            ".gif" in my_file or ".GIF" in my_file):
        return True
    else:
        return False


def duplicate(current_files):
    current = 0
    for count in range(1, config['batches']+1):
        for frame in range(1, config['frames']+1):
            source = "%s%s" % (config['source'], current_files[current])
            target = "%sIMG_%04d_%02d.JPG" % (config['target'], count, frame)
            what = "COPIED"
            if not os.path.exists(target):
                create_duplicate(source, target, count, frame)
            else:
                if config['overwrite']:
                    create_duplicate(source, target, count, frame)
                else:
                    what = "SKIPPED"

            print "%04d: %s --> %s [%s]" % (count, source, target, what)
            current += 1
            if current >= len(current_files):
                current = 0


def create_duplicate(source, target, count, frame):
    if config['overlay']:
        img = Image.open(source)
        draw = ImageDraw.Draw(img)
        draw.text(
            (1450, 60),
            "%04d-%02d" % (count, frame),
            (255, 14, 179),
            font=config['font']
        )
        img.save(target, quality=config['overlay-quality'])
    else:
        shutil.copy2(source, target)

if not os.path.exists(config['source']):
    print "\n%s doesn't exists!!!!\n\n" % config['source']
    sys.exit(0)

if not os.path.exists(config['target']):
    print "\n%s doesn't exists!!!!\n" % config['target']
    sys.exit(0)

duplicate(scan_folder())

"""
EXIF STUFF:

        # exif
        exif_dict = piexif.load(img.info['exif'])
        # img = img.transpose(Image.ROTATE_90)
        # img = img.rotate(Image.ROTATE_90, expand=True)

        # set exif width, height
        # w, h = img.size
        # exif_dict["0th"][piexif.ImageIFD.XResolution] = (w, 1)
        # exif_dict["0th"][piexif.ImageIFD.YResolution] = (h, 1)
        # exif_dict["Exif"][40962] = 1080
        # exif_dict["Exif"][40963] = 1080

        exif_dict["0th"][piexif.ImageIFD.Orientation] = 6
        exif_dict["0th"][274] = 6

        # del exif_dict["0th"][piexif.ImageIFD.Orientation]
        # exif_dict["0th"][34665] = 90
        # exif_dict["0th"][34665] = 90
        exif_bytes = piexif.dump(exif_dict)

        # from pprint import pprint
        # print exif_dict["0th"][piexif.ImageIFD.Orientation]
        # exif_tags = {'Exif', '0th', 'Interop', '1st', 'thumbnail', 'GPS'}

        # pprint(exif_dict['0th'])
        # pprint(exif_dict['Exif'])

        # for k in exif_dict.keys():
        #     print k
        # sys.exit(0)
        # pprint(exif_dict)
"""
