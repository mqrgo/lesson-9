from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from main_board.models import NewsPost
from django.views.generic import ListView, DetailView, FormView
from main_board.forms import NewsPostForm


class NewsListView(ListView):
    model = NewsPost
    template_name = 'main_board/index.html'
    context_object_name = 'posts'


class NewsListByCategory(ListView):
    template_name = 'main_board/index.html'
    context_object_name = 'posts'

    def get_queryset(self) -> QuerySet[Any]:
        return NewsPost.objects.filter(
            category__slug=self.kwargs['category_slug']
        )


class DetailView(DetailView):
    template_name = 'main_board/detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        obj = get_object_or_404(
            NewsPost,
            created__year=self.kwargs['year'],
            created__month=self.kwargs['month'],
            created__day=self.kwargs['day'],
            slug=self.kwargs[self.slug_url_kwarg]
        )
        return obj


class AddNews(FormView):
    template_name = 'main_board/add_news.html'
    form_class = NewsPostForm
    success_url = '/'

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return super().form_valid(form)


# def index(request, category_slug=None):
#     categories = Category.objects.all()
#     posts = NewsPost.objects.all()
#     if category_slug:
#         posts = NewsPost.objects.filter(category__slug=category_slug)
#     return render(request, 'main_board/index.html', {
#         'posts': posts, 'categories': categories
#         }
#     )

# def detail(request, year, month, day, post_slug):
#     post = get_object_or_404(
#         NewsPost,
#         created__year=year,
#         created__month=month,
#         created__day=day,
#         slug=post_slug,
#     )
#     return render(request, 'main_board/detail.html', {'post': post})
