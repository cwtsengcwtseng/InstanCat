from django.contrib import admin

# Register your models here.
from insta.models import Post, instaUser, Like

admin.site.register(Post)
admin.site.register(instaUser)
admin.site.register(Like)
