from django.contrib import admin

from .models import UserProfile, UserPersona, UserInterest
from ..accounts.models import Post

admin.site.register(UserProfile)
admin.site.register(UserPersona)
admin.site.register(UserInterest)
admin.site.register(Post)
