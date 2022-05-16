from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'