from smarttender.models import Calculation


def create_calculation(lot):
    try:
        calculation = Calculation(
            lot=lot
        )
        calculation.save()
    except KeyError:
        pass
