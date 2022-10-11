from django.contrib import admin

from personal_blog.models import Category, Contact, NewsLetter, Post, Tag, Comment

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(NewsLetter)
admin.site.register(Contact)
admin.site.register(Comment)
