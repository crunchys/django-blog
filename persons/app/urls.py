from django.urls import path

from .views import *

urlpatterns = [
    path('', PersonHome.as_view(), name='home'),
    path('category/<slug:category_slug>/', PersonCategory.as_view(), name='category'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post')
]
