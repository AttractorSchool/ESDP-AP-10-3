import requests
from django.views.generic import ListView

from smarttender.models import TenderAPI


class TenderAPIListView(ListView):
    model = TenderAPI
    template_name = 'tenders.html'
    context_object_name = 'tenders'

    def post(self, request, *args, **kwargs):
        url = 'https://ows.goszakup.gov.kz/v3/trd-buy/all'
        headers = {
            'Authorization': 'Bearer 4c47e9fc44b56c35a1c7aa7f0dcb8b04'
        }
        response = requests.get(url, headers=headers, verify=False)
        data = response.json()
        items = data['items']
        filtered_items = []

        for tender in items:
            total_sum = tender.get('total_sum')
            if total_sum is not None and total_sum >= 500000:
                filtered_items.append(tender)

        for tender in filtered_items:
            if not TenderAPI.objects.filter(
                    lot=tender.get('number_anno'),
                    company=tender.get('org_name_ru'),
                    name=tender.get('name_ru')
            ).exists():
                tender = TenderAPI(
                    lot=tender['number_anno'],
                    company=tender['org_name_ru'],
                    name=tender['name_ru']
                )
                tender.save()
        return self.get(request, *args, **kwargs)
