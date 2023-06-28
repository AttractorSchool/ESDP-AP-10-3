from smarttender.models import RefTradeMethod


def get_ref_trade_methods(trade_methods):
    try:
        ref_trade_method, created = RefTradeMethod.objects.get_or_create(
            name_kz=trade_methods.get('nameKz'),
            name_ru=trade_methods.get('nameRu'),
            code=trade_methods.get('code'),
            symbol_code=trade_methods.get('symbolCode')
        )
        return ref_trade_method
    except KeyError:
        pass
