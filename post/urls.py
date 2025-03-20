from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('create/', views.create_post, name='create_post'),
    # path('delete/', views.delete_post, name='delete_post'),
    # path('detail/<int:pk>/', views.detail_post, name='detail_post'),
]
