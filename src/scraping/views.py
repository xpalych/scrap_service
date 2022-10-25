from django.shortcuts import render

from scraping.forms import FindForm
from scraping.models import Vacancy
from scraping.utils import from_cyrillic_to_eng


def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    _filter = {}
    if city:
        _filter['city__slug'] = city
    if language:
        _filter['language__slug'] = language
    if _filter:
        qs = Vacancy.objects.filter(**_filter)
    else:
        qs = Vacancy.objects.all()
    return render(request, 'scraping/home.html', {'object_list': qs,
                                                  'form': form})
