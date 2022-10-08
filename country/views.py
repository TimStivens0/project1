from django.shortcuts import render, redirect, get_object_or_404
from .models import CountryModel
from .forms import CountryModelForm


def delete_view(request, id):
    country = get_object_or_404(CountryModel, id=id)
    country.delete()
    return redirect('/')


def update_view(request, id):
    country = get_object_or_404(CountryModel, id=id)
    form = CountryModelForm(data=request.POST or None, instance=country)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'update.html', context={
        'form': form
    })


def home_view(request):
    request.title = 'Project 1'
    countries = CountryModel.objects.all()
    return render(request, 'index.html', context={
        'countries': countries
    })


def input_view(request):
    form = CountryModelForm()
    if request.method == 'POST':
        data = CountryModelForm(data=request.POST)
        if data.is_valid():
            #    2)

            data.save()


            #    1)

            # country = CountryModel(
            #     Country_Name=data.cleaned_data['Country_Name'],
            #     Country_Capital=data.cleaned_data['Country_Capital'],
            #     Country_Currency=data.cleaned_data['Country_Currency']
            # )
            # country.save()
            return redirect('/')
    return render(request, 'input.html', context={
        'form': form
    })
