from django.contrib import admin

from charityapp.blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
