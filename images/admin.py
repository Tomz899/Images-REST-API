from django.contrib import admin
from images.models import Image
from users.models import TierUser

admin.site.register(Image)
admin.site.register(TierUser)
