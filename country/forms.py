from django import forms
from .models import CountryModel


#    2)

class CountryModelForm(forms.ModelForm):
    class Meta:
        model = CountryModel
        fields = ['Country_Name', 'Country_Capital', 'Country_Currency']
        widgets = {
            'Country_Name': forms.TextInput(
                attrs={
                    'placeholder': 'Country Name'
                }
            ),
            'Country_Capital': forms.TextInput(
                attrs={
                    'placeholder': 'Country Capital'
                }
            ),
            'Country_Currency': forms.TextInput(
                attrs={
                    'placeholder': 'Country Currency'
                }
            )
        }


#    1)

# class CountryModelForm(forms.Form):
#     Country_Name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'main', 'placeholder': 'Country Name'
#     }), label=False)
#     Country_Capital = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'main', 'placeholder': 'Country Capital'
#     }), label=False)
#     Country_Currency = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'main', 'placeholder': 'Country Currency'
#     }), label=False)
