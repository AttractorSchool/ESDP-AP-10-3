from smarttender.models import RefBuyStatus


def get_ref_buy_status(buy_status):
    try:
        ref_buy_status, created = RefBuyStatus.objects.get_or_create(
            name_kz=buy_status.get('nameKz'),
            name_ru=buy_status.get('nameRu'),
            code=buy_status.get('code')
        )
        return ref_buy_status
    except KeyError:
        pass
