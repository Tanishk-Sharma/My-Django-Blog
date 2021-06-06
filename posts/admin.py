from django.contrib import admin
from .models import BlogPost, Tags, Categories


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_state', 'author', 'publish_datetime')
    list_filter = ('post_state', 'author', 'publish_datetime')
    search_fields = ['title', 'body', 'author']

admin.site.register(BlogPost, BlogPostAdmin)

class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)

admin.site.register(Tags, TagsAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

admin.site.register(Categories, CategoriesAdmin)
