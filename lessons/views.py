from django.shortcuts import render

# Create your views here.

def intro(request):
    context = {}
    template = 'lessons/intro.html'
    return render(request, template, context)