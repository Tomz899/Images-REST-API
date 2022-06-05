from django.test import TestCase
from .models import Image

# from django.core.files.uploadedfile import SimpleUploadedFile

# class ImageTest(TestCase):
#     test_image = SimpleUploadedFile(name='test.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get("localhost:8000")
        self.assertEqual(response.status_code, 200)
