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

        # Get the current page number from the request's query parameters
        paginator = Paginator(articles, 6)
        # Get the Page object for the current page number
        page = self.request.GET.get('page')
        # Get the Page object for the current page number
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
        return super().form_valid(form)


class ArticleReadView(views.DetailView):
    template_name = 'blog/read-article.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_instance = self.get_object()  # Use self.get_object() to get the Article instance
        sections = article_instance.content.split(':')

        context['sections'] = sections

        # text = article_instance.content
        #
        # # Use regular expressions to split the text into sentences
        # split_text = re.split(r'\. |(?<=:)', text)
        #
        # # Separate the title from the content and combine them into a list of tuples
        # titles_and_contents = [(s.split(":")[0] + ":", s.split(":")[1].strip()) for s in split_text if ":" in s]
        #
        # # If there's content before the first title, add it as the first content
        # if text.startswith(titles_and_contents[0][0]):
        #     titles_and_contents.insert(0, (split_text[0], ""))
        #
        # context['titles_and_contents'] = titles_and_contents

        return context


class ArticleEditView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    template_name = 'blog/edit-article.html'
    model = Article
    fields = ['title', 'subtitle', 'short_resume', 'introduction', 'content', 'featured_image']

    def get_success_url(self):
        # Redirect to the detail view of the edited article
        return reverse('article-details', kwargs={'pk': self.object.pk})

    def test_func(self):
        # Check if the logged-in user is the author of the article
        article = self.get_object()
        return self.request.user == article.author


class ArticleDeleteView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.DeleteView):
    template_name = 'blog/delete-article.html'
    model = Article
    success_url = reverse_lazy('act-green-blog-page')

    def test_func(self):
        # Check if the logged-in user is the author of the article
        article = self.get_object()
        return self.request.user == article.author
