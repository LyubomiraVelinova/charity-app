from django.contrib import admin

from charityapp.blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "short_resume", "author", "created_at", "updated_at", "featured_image")
