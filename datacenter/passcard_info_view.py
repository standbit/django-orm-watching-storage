from datacenter.overall_view import get_passcard_visits_description
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=this_passcard)
    visits_description = get_passcard_visits_description(this_passcard_visits)
    context = {
        "passcard": this_passcard_visits[0].passcard,
        "this_passcard_visits": visits_description
    }
    return render(request, "passcard_info.html", context)
