from django.urls import path, include

from charityapp.blog.views import ActGreenBlogView, ArticleDetailsView, EditArticleView, DeleteArticleView, \
    CreateArticleView

urlpatterns = [
    path('', ActGreenBlogView.as_view(), name='act-green-blog'),
    path('article/<int:pk>/', include([
        path('read/', ArticleDetailsView.as_view(), name='article-details'),
        path('edit/', EditArticleView.as_view(), name='edit-article'),
        path('delete/', DeleteArticleView.as_view(), name='delete-article'),
    ])),
    path('article/create/', CreateArticleView.as_view(), name='create-article'),
]
