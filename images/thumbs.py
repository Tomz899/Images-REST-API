# from imagekit import ImageSpec
from imagekit.processors import ResizeToFill


# class Thumbnail(ImageSpec):
#     processors = [ResizeToFill(100, 50)]
#     format = "JPEG"
#     options = {"quality": 60}


basic_image_field_specs = {
    "source": "image",
    "processors": [ResizeToFill(100, 50)],
    "format": "JPEG",
    "options": {"quality": 80},
}
