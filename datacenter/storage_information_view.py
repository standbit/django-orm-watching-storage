from datacenter.models import Passcard, get_unfinished_visits, get_visit_description
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = get_visit_description(get_unfinished_visits())
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
