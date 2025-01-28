from django.http import JsonResponse
from django.views import View
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from api.tasks.reddit_crontask import fetch_reddit_data


class StartTask(View):
    def get(request, response):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES,
        )
        PeriodicTask.objects.create(
            interval=schedule,
            name='fetch_reddit_data_every_minute',
            task='api.tasks.reddit_crontask.fetch_reddit_data',
        )

        return JsonResponse({'status': 'Task started and scheduled every minute'})

class StopTask(View):
    def get(request, response):
        PeriodicTask.objects.filter(name='fetch_reddit_data_every_minute').delete()
        return JsonResponse({'status': 'Task stopped'})


