# from PIL import ImageFont

folder = '/sayfromage/'

config = {
    'frames': 16,
    'start_batch': 1,
    'how_many_batches': 200,
    'overwrite': False,
    'source': '%sphotos_bullet_16_500/' % folder,
    'target': '%sphotos_bullet_16_5000/' % folder,
    'overlay-text': True,
    'image-quality': 95,
    'image_format': 'XXXX',
    # to get list of available fonts
    # identify -list Type
    'font': 'CourierNew',
    # 'font': ImageFont.truetype("Courier New Bold.ttf", 150),
    'delay_between_batches': 2,  # in seconds
    'delay_between_frames': 0.5,  # in seconds
    'user_confirm': True,
    'resize': True,
    'resize_width': 1080,
    # resize_height disbaled
    # 'resize_height': 1620,
    # write_exif disbaled
    # 'write_exif': False,
    'greenscreen': False,
    'greenscreen-colour': '#13843D',
    'greenscreen-fuzz': '15%',
}
