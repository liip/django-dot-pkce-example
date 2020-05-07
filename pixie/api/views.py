from django.views.generic import View
from django.http.response import JsonResponse
from django.utils import timezone


class TestView(View):
    def get(self, request):
        return JsonResponse(data={'timestamp': timezone.now(), 'message': 'Hello there!'})
