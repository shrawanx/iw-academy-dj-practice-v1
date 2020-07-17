from django.http import HttpResponse
from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView, RedirectView


class FirstView(View):
    # get  --> get()
    # post method --> post()

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is GET")

    def post(self, request, *args, **kwargs):
        return HttpResponse("This is POST")


class FirstTemplate(TemplateView):
    template_name = 'classbased/template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = "Hello World"
        return context


class FirstTemplateRedirect(RedirectView):
    url = '/c/template/'
