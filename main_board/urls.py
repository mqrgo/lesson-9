from django.urls import path
from main_board import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='index'),
    path('<slug:category_slug>', views.NewsListByCategory.as_view(), name='index_with_category'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', views.DetailView.as_view(), name='detail'),
    path('add_news/', views.AddNews.as_view(), name='add_news'),
    # path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', views.DetailNewsView.as_view(), name='detail'),
    # path('', views.index, name='index'),
]
