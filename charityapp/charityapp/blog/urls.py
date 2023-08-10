from django.urls import path, include

from charityapp.blog.views import ActGreenBlogView, ArticleReadView, ArticleEditView, ArticleDeleteView, \
    ArticleCreateView

urlpatterns = [
    path('', ActGreenBlogView.as_view(), name='act-green-blog-page'),
    path('article/', include([
        path('create/', ArticleCreateView.as_view(), name='create-article'),
        path('<int:pk>/', include([
            path('read/', ArticleReadView.as_view(), name='article-details'),
            path('edit/', ArticleEditView.as_view(), name='edit-article'),
            path('delete/', ArticleDeleteView.as_view(), name='delete-article'),
        ])),
    ])),
]
