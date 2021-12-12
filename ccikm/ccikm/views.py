from django.shortcuts import render
from django.http import HttpResponse


def Index(request):
    return render(request, 'news_details.html', context={})
