from smarttender.models import Offer


def create_offer(lot):
    try:
        offer = Offer(
            lot=lot
        )
        offer.save()
    except KeyError:
        pass
