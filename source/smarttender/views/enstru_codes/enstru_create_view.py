from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from smarttender.models import EnsTruCode


class EnsTruCreateView(LoginRequiredMixin, CreateView):
    model = EnsTruCode
