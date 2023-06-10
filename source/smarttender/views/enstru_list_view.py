from django.http import JsonResponse
from django.views.generic import ListView

from smarttender.models import EnsTruCode


class EnsTruListView(ListView):

    def get(self, request, *args, **kwargs):
        codes = EnsTruCode.objects.all().values()
        return JsonResponse({'enstru_codes': list(codes)}, safe=False)