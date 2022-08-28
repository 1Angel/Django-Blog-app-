from django.contrib import admin
from post.models import Post, Comentario, UserProfile
# Register your models here.
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(UserProfile)

