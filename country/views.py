from django.shortcuts import render
from .models import CountryModel

def home_view(request):
    request.title = 'Project 1'
    country = CountryModel.objects.all()
    return render(request, 'index.html', context={
        'word': 'Hello', 'countries': 'country'
    })
