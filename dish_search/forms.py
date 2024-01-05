from django import forms

class DishSearchForm(forms.Form):
    query = forms.CharField(label='Search for dishes', max_length=255)
