
from django.shortcuts import render
from .forms import DishSearchForm
from .models import Dish

def search_view(request):
    form = DishSearchForm(request.GET or None)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        print("Query", query)
        results = Dish.objects.filter(items__icontains=query)

    print(results)
    return render(request, 'Search.html', {'form': form, 'results': results})
