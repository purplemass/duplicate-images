from PIL import ImageFont

config = {
    'frames': 16,
    'batches': 500,
    'start_batch': 1,
    'source': '/sayfromage/photos_bullet_16_500/',
    'target': '/sayfromage/photos_bullet_16_5000/',
    'overlay': True,
    'overlay-quality': 95,
    'overwrite': False,
    'font': ImageFont.truetype("Courier New Bold.ttf", 100),
    'delay_between_batches': 2,  # in seconds
    'delay_between_frames': 0.5,  # in seconds
}
