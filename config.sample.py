# from PIL import ImageFont

folder = '/Volumes/Projects/sayfromage/__root__/__fondue__/'

config = {
    'frames': 16,
    'start_batch': 1,
    'how_many_batches': 200,
    'overwrite': False,
    'source': '%s___USE___/' % folder,
    'target': '%s__IN__/' % folder,
    'overlay-text': True,
    'image-quality': 95,
    'image_format': 'XXXX_XX',
    # to get list of available fonts
    # identify -list Type
    'font': 'CourierNew',
    # font size is determined by the text area size which is
    # resize_width divided by font_size
    'font_size': 8,
    'delay_between_batches': 30,  # in seconds
    'delay_between_frames': 1,  # in seconds
    'user_confirm': False,
    'resize_width': 1080,
    'greenscreen': False,
    'greenscreen-colour': '#13843D',
    'greenscreen-fuzz': '15%',
    # resize, resize_height, write_exif - not used
    # 'resize': True,
    # 'resize_height': 1620,
    # 'write_exif': False,
    #  old style font - not used
    # 'font': ImageFont.truetype("Courier New Bold.ttf", 150),
}
