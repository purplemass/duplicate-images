from PIL import ImageFont

config = {
    'frames': 16,
    'start_batch': 1,
    'how_many_batches': 200,
    'overwrite': False,
    'source': '/sayfromage/photos_bullet_16_500/',
    'target': '/sayfromage/photos_bullet_16_5000/',
    'overlay-text': True,
    'image-quality': 95,
    'image_format': 'XXXX',
    'font': ImageFont.truetype("Courier New Bold.ttf", 250),
    'delay_between_batches': 2,  # in seconds
    'delay_between_frames': 0.5,  # in seconds
    'enable_input': True,
    'resize': True,
    'resize_width': 1152,
    'resize_height': 768,
    'write_exif': True,
    'greenscreen': False,
    'greenscreen-colour': '#13843D',
    'greenscreen-fuzz': '15%',
}
