from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import ListView

from smarttender.models import EnsTruCode


class EnsTruListView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        codes = EnsTruCode.objects.all().order_by('-created_at').values()
        return JsonResponse({'enstru_codes': list(codes)}, safe=False)
