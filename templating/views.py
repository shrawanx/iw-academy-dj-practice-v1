from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def hello_templates(request):
    template = loader.get_template('templating/hello.html')
    context = {
        'name': 'Ram bahadur',
        'my_dict': {
            'name': 'My name is Ram Bahadur'
        }
    }
    template_data = template.render(context, request)
    return HttpResponse(template_data)


def hello_render(request):
    context = {
        'name': 'Ram bahadur'
    }
    return render(request, "templating/hello_render.html", context)
