from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.utils.timezone import now

#######################################################

class Tags(models.Model):
    tag_name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.tag_name

#######################################################

class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
#######################################################

class BlogPost(models.Model):
    title = models.CharField(max_length=100, help_text='Title')
    cover_image = models.ImageField(upload_to='post_cover_image', blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='posts_by_user')
    body = RichTextUploadingField(help_text='Post Body')
    publish_datetime = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField()
    views = models.IntegerField(default=0)
    post_state_choices = [
        ('DRAFT', 'DRAFT'),
        ('PUBLISHED', 'PUBLISHED'),
    ]
    post_state = models.CharField(max_length=30, choices=post_state_choices, default=post_state_choices[0][0])
    tags = models.ManyToManyField(Tags, related_name='posts_under_this_tag')
    categories = models.ManyToManyField(Categories, related_name='posts_under_this_category')

    class Meta:
        ordering = ['-publish_datetime']

    def reset_views(self):
        self.views = 0
        self.save()

    def __str__(self):
        return  str(self.title)

#######################################################

# USE DISQUS FOR COMMENTS
