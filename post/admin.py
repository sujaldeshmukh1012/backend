from .models import IpModel, Post
from django.contrib import admin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'posted', 'author', 'likes')
    list_filter = ('views', 'likes', 'id')
    search_fields = ('id', 'title', 'views', 'body')
    ordering = ('-posted',)


class IpAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'time')
    list_filter = ('id', 'ip', 'time')
    search_fields = ('id', 'ip', 'time')
    ordering = ('-time',)


admin.site.register(Post, PostAdmin)
admin.site.register(IpModel, IpAdmin)
