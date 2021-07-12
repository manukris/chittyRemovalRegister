from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.edit import UpdateView,CreateView
from .models import RemovalReg


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




class RemovalListView(ListView):
    model = RemovalReg
    template_name = 'removallist.html'


class RemovalUpdateView(UpdateView):
    model = RemovalReg
    template_name = 'update.html'
    fields = [
        "chittyName",
        "chittalName",
        "chittalNo",
        "removalDate",
    ]
    success_url = "/"

class AddRemovalView(CreateView):
    model = RemovalReg
    fields  = [
        "chittyName",
        "chittalName",
        "chittalNo",
        "removalDate",
    ]
    template_name = 'add.html'
    success_url = "/"



class SearchRemoval(ListView):
    template_name = 'search.html'
    model = RemovalReg

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            object_list = self.model.objects.filter(chittyName__startswith=query).order_by('chittalNo')
        else:
            object_list = self.model.objects.none()
        return object_list