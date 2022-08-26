from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
from .utils import *


class PersonHome(DataMixin, ListView):
    model = Person
    template_name = 'app/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Person.objects.all().select_related('category')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Oops... Seems like this page is gone missing</h1>')


class ShowPost(DataMixin, DetailView):
    model = Person
    template_name = 'app/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'],
                                      category_selected=None)
        return dict(list(context.items()) + list(c_def.items()))


class PersonCategory(DataMixin, ListView):
    model = Person
    template_name = 'app/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Person.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title=c,
                                      category_selected=c.id)
        return dict(list(context.items()) + list(c_def.items()))