# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import timezone

from django.shortcuts import render, get_object_or_404
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Post,Article





class Home(TemplateView):
    template_name = 'blog/post_list.html'


class List(ListView):
    template_name = 'blog/list.html'
    model = Post


class Detail(DetailView):
    template_name = 'blog/detail.html'
    model = Post

    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/detail.html', {'post': post})


class MyPostList(ListView):
    template_name = 'blog/mylist.html'
    model = Article


class Myarticles(DetailView):
    template_name = 'blog/article.html'
    model = Article

    def article(request, pk1):
        art = get_object_or_404(Article, pk=pk1)
        return render(request, 'blog/article.html', {'art': art})


class Delete(DeleteView):
    model = Post
    success_url = 'blog/delete.html'







# Create your views here.




