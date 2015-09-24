import os
import sys
import shutil
import time
import argparse

from PIL import Image
from PIL import ImageDraw

import piexif

from config import config


def check_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--start_batch", required=False)
    parser.add_argument("-x", "--how_many_batches", required=False)
    parser.add_argument("-i", "--enable_input", required=False)

    try:
        args = parser.parse_args()
    except SystemExit:
        print "Arguments error: %s" % sys.argv
        sys.exit(0)

    if args.start_batch:
        config['start_batch'] = int(args.start_batch)
    if args.how_many_batches:
        config['how_many_batches'] = int(args.how_many_batches)
    if args.enable_input:
        if (args.enable_input == "true"):
            config['enable_input'] = True
        else:
            config['enable_input'] = False


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
    current_batch = 0
    xxx_inc = 0
    for batch in range(
        config['start_batch'],
        config['start_batch'] + config['how_many_batches']
    ):
        for frame in range(1, config['frames']+1):
            source = "%s%s" % (config['source'], current_files[current_batch])
            if config['image_format'] == "XXXX_XX":
                target = "%sIMG_%04d_%02d.JPG" % (
                    config['target'], batch, frame)
            else:
                target = "%sIMG_%04d.JPG" % (
                    config['target'], (xxx_inc*config['frames']) + frame)
            what = "COPIED"
            if not os.path.exists(target):
                create_duplicate(source, target, batch, frame)
            else:
                if config['overwrite']:
                    create_duplicate(source, target, batch, frame)
                else:
                    what = "SKIPPED"

            print "%04d-%02d: %s --> %s [%s]" % (
                batch, frame, source, target, what)
            current_batch += 1
            if current_batch >= len(current_files):
                current_batch = 0

        if (what != "SKIPPED"):
            if (config['enable_input']):
                raw_input("Enter to continue >")

            else:
                print 'stopping for %s seconds' % (
                    config['delay_between_batches'])
                time.sleep(config['delay_between_batches'])
        xxx_inc += 1


def create_duplicate(source, target, batch, frame):
    if config['overlay-text'] or config['resize']:
        img = Image.open(source)
        if config['overlay-text']:
            # exif
            exif_dict = piexif.load(img.info['exif'])
            exif_dict["0th"][piexif.ImageIFD.Orientation] = 8
            exif_bytes = piexif.dump(exif_dict)
            # text overlay
            if config['image_format'] == "XXXX_XX":
                text = "%04d-%02d" % (batch, frame)
            else:
                text = "%04d" % (batch)
            draw = ImageDraw.Draw(img)
            draw.text(
                (800, 60),
                text,
                (255, 14, 179),
                font=config['font']
            )
        if config['resize']:
            img = img.resize(
                (config['resize_width'], config['resize_height']),
                Image.ANTIALIAS)
        img.save(target, quality=config['image-quality'], exif=exif_bytes)
    else:
        shutil.copy2(source, target)
    time.sleep(config['delay_between_frames'])


if __name__ == '__main__':

    if not os.path.exists(config['source']):
        print "\n%s doesn't exists!!!!\n\n" % config['source']
        sys.exit(0)

    if not os.path.exists(config['target']):
        print "\n%s doesn't exists!!!!\n" % config['target']
        sys.exit(0)

    check_arguments()
    duplicate(scan_folder())


"""
EXIF STUFF:

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
