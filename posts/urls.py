from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('createpost/', views.create_post, name='createpost'),
    path('<slug:slug>',views.page_view, name='page')
]
