from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved' # Noqa E501
        )


def get_unfinished_visits():
    all_visits = Visit.objects.all()
    unfinished_visits = []
    for visit in all_visits:
        if not visit.leaved_at:
            unfinished_visits.append(visit)
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
    visit_time_in_min = (int(get_duration(visit).total_seconds()))/60
    if visit_time_in_min > minutes:
        return True
    return False
