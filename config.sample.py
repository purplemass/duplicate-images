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
    'font': ImageFont.truetype("Courier New Bold.ttf", 100),
    'delay_between_batches': 2,  # in seconds
    'delay_between_frames': 0.5,  # in seconds
}
