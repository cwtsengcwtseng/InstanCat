from django.contrib import admin

# Register your models here.
from insta.models import Post, instaUser

admin.site.register(Post)
admin.site.register(instaUser)
