from datacenter.overall_view import get_storage_visit
from datacenter.overall_view import get_unfinished_visits
from django.shortcuts import render


def storage_information_view(request):
    unfinished_visits = get_storage_visit(get_unfinished_visits())
    context = {
        'non_closed_visits': unfinished_visits,
    }
    return render(request, 'storage_information.html', context)
