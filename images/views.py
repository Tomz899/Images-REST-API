from rest_framework import permissions, viewsets

from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    """
    Bellow definition overrides queryset and filter images by loged user.
    """

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(img_owner=user)
