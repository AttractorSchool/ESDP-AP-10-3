from smarttender.models import Lot


def create_lot(trd_buy, lot):
    try:
        lot = Lot(
            trd_buy=trd_buy,
            lot_number=lot.get('lotNumber'),
            count=lot.get('count'),
            amount=lot.get('amount'),
            name_kz=lot.get('nameKz'),
            name_ru=lot.get('nameRu'),
            description_kz=lot.get('descriptionKz'),
            description_ru=lot.get('descriptionRu'),
            customer_name_kz=lot.get('customerNameKz'),
            customer_name_ru=lot.get('customerNameRu'),
            dumping=lot.get('dumping')
        )
        lot.save()
    except KeyError:
        pass
    return lot
