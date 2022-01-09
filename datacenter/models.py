import datetime
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
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )


def get_unfinished_visits():
    all_visits = Visit.objects.all()
    unfinished_visits = []
    for visit in all_visits:
        if not visit.leaved_at:
            unfinished_visits.append(visit)
    return unfinished_visits


def get_duration(visit):
    now = localtime().replace(microsecond=0)
    entered_time = localtime(visit.entered_at)
    delta = now - entered_time
    return delta


def format_duration(duration):
    seconds = int(duration.total_seconds())
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = (seconds % 3600) % 60
    return f'{hours}:{minutes}:{secs}'


def get_visit_description(visits):
    visits_description = []
    for lost_visit in visits:
        descript = {
            'who_entered': lost_visit.passcard,
            'entered_at': localtime(lost_visit.entered_at),
            'duration': format_duration(get_duration(lost_visit)),
        }
        visits_description.append(descript)
    return visits_description
