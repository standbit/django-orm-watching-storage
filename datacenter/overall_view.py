from datacenter.models import Visit
from django.utils.timezone import localtime


def get_unfinished_visits():
    unfinished_visits = Visit.objects.filter(leaved_at=None)
    return unfinished_visits


def format_duration(duration):
    seconds = int(duration.total_seconds())
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = (seconds % 3600) % 60
    return f'{hours}:{minutes}:{secs}'


def get_storage_visit(visits):
    storage_visits = []
    for visit in visits:
        descript = {
            'who_entered': visit.passcard,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit),
        }
        storage_visits.append(descript)
    return storage_visits


def get_passcard_visits_description(visits):
    passcard_visits_description = []
    for visit in visits:
        descript = {
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit),
        }
        passcard_visits_description.append(descript)
    return passcard_visits_description


def get_duration(visit):
    now = localtime().replace(microsecond=0)
    entered_time = localtime(visit.entered_at)
    leaved_time = localtime(visit.leaved_at)
    if not visit.leaved_at:
        delta = now - entered_time
    else:
        delta = leaved_time - entered_time
    return delta


def is_visit_long(visit, minutes=60):
    visit_time_in_min = get_duration(visit).total_seconds()/60
    return visit_time_in_min > minutes
