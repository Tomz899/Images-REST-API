# from imagekit import ImageSpec
from imagekit.processors import ResizeToFill

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
