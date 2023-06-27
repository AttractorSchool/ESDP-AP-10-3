from smarttender.models import TrdBuy


def create_trd_buy(trd_buy):
    try:
        trd_buy = TrdBuy(
            number_anno=trd_buy.get('numberAnno'),
            name_kz=trd_buy.get('nameKz'),
            name_ru=trd_buy.get('nameRu'),
            total_sum=trd_buy.get('totalSum'),
            count_lots=trd_buy.get('countLots'),
            customer_name_kz=trd_buy.get('customerNameKz'),
            customer_name_ru=trd_buy.get('customerNameRu'),
            org_bin=trd_buy.get('orgBin'),
            org_pid=trd_buy.get('orgPid'),
            org_name_kz=trd_buy.get('orgNameKz'),
            org_name_ru=trd_buy.get('orgNameRu'),
            start_date=trd_buy.get('startDate'),
            end_date=trd_buy.get('endDate'),
            publish_date=trd_buy.get('publishDate'),
            itogi_date_public=trd_buy.get('itogiDatePublic')
        )
        trd_buy.save()
    except KeyError:
        pass
    return trd_buy
