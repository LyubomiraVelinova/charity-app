from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from charityapp.blog.models import Article


class ActGreenBlogView(views.TemplateView):
    template_name = 'blog/act-green-blog-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all()

        paginator = Paginator(articles, 6)
        page = self.request.GET.get('page')
        current_page = paginator.get_page(page)

        context['articles'] = current_page
        return context


class ArticleCreateView(views.CreateView):
    model = Article
    fields = ['title', 'subtitle', 'short_resume', 'introduction', 'featured_image', 'content']
    template_name = 'blog/create_article.html'
    success_url = reverse_lazy('act-green-blog-page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Article created successfully!')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Please correct the errors below.')
        return response


class ArticleReadView(views.DetailView):
    template_name = 'blog/read-article.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_instance = self.get_object()
        sections = article_instance.content.split(':')
        context['sections'] = sections

        return context


class ArticleEditView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    template_name = 'blog/edit-article.html'
    model = Article
    fields = ['title', 'subtitle', 'short_resume', 'introduction', 'content', 'featured_image']

    def get_success_url(self):
        return reverse('article-details', kwargs={'pk': self.object.pk})

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class ArticleDeleteView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.DeleteView):
    template_name = 'blog/delete-article.html'
    model = Article
    success_url = reverse_lazy('act-green-blog-page')

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author
