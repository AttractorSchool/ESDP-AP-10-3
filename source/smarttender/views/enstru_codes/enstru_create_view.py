from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from smarttender.models import EnsTruCode


@csrf_exempt
def enstru_create_view(request):
    if request.method == 'POST':
        enstru_code = request.POST.get('ensTruCode')
        enstru_name = request.POST.get('ensTruName')

        enstru = EnsTruCode(
            code=enstru_code,
            name=enstru_name
        )
        enstru.save()

        return JsonResponse({'message': 'Код ЕНС ТРУ успешно сохранен'})
