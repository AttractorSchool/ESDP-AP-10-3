from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import ListView

from smarttender.forms import SearchForm
from smarttender.models import Tender
from smarttender.utils import parse_excel_file, parse_enstru_excel_file


class TenderListView(LoginRequiredMixin, ListView):
    model = Tender
    template_name = 'index.html'
    context_object_name = 'tenders'
    paginate_by = 30
    paginate_orphans = 1
    ordering = '-created_at'

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)

        if self.search_value:
            query = Q(lot__lot_number__icontains=self.search_value) | Q(lot__name_ru__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def post(self, request, *args, **kwargs):
        if request.FILES and 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            parse_excel_file(excel_file)
            messages.success(request, 'Файл успешно загружен!')
        elif request.FILES and 'enstru_excel_file' in request.FILES:
            enstru_excel_file = request.FILES['enstru_excel_file']
            parse_enstru_excel_file(enstru_excel_file)
            messages.success(request, 'Файл успешно загружен!')
        else:
            messages.error(request, 'Ошибка загрузки файла!')
        return self.get(request, *args, **kwargs)
