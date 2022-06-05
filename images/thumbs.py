# from imagekit import ImageSpec
from imagekit.processors import ResizeToFill

"""
Dictionary specs for resizing images for user tiers.
"""

basic_specs = {
    "source": "image",
    "processors": [ResizeToFill(200, 200)],
    "format": "JPEG",
    "options": {"quality": 80},
}

premium_specs = {
    "source": "image",
    "processors": [ResizeToFill(400, 400)],
    "format": "JPEG",
    "options": {"quality": 80},
}
