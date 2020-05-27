from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/index/', views.post_index, name='post_index'),
    path('post/delete/', views.post_delete, name='post_delete'),
    path('post/search/', views.post_search, name='post_search'),
    path('post/search_result/', views.post_search_result, name='post_search_result')
]