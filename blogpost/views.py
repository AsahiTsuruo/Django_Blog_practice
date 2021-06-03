from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import BlogModel
from django.urls import reverse_lazy
from django.db.models import Q, query

# Create your views here.

class BlogList(ListView):
    template_name = 'list.html'
    #model = BlogModel
    

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = BlogModel.objects.filter(
                Q(title__icontains=q_word) | Q(content__icontains=q_word) | Q(category__icontains=q_word)
            )
        else:
            object_list = BlogModel.objects.all()
        tmp1 = [obj for obj in BlogModel.objects.all()]
        print("-----tmp1------",tmp1)
        tmp2 = BlogModel.objects.all()
        print("-----tmp2------",tmp2)
        tmp3 = BlogModel.objects.values_list()
        print("-----tmp3------",tmp3)
        return object_list

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')