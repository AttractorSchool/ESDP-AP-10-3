from smarttender.models import RefTypeTrade


def get_ref_type_trade(type_trade):
    try:
        type_trade, created = RefTypeTrade.objects.get_or_create(
            name_kz=type_trade.get('nameKz'),
            name_ru=type_trade.get('nameRu')
        )
        return type_trade
    except KeyError:
        pass
