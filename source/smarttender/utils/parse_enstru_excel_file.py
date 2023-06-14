import math

import pandas as pd

from smarttender.models import EnsTruCode


def parse_enstru_excel_file(enstru_excel_file):
    df = pd.read_excel(enstru_excel_file)
    empty_row_count = 0

    for index, row in df.iterrows():
        if pd.isnull(row[1]) and pd.isnull(row[2]) and pd.isnull(row[3]):
            empty_row_count += 1
        else:
            empty_row_count = 0

        if empty_row_count >= 2:
            break

        row = [value if not (isinstance(value, float) and math.isnan(value)) else None for value in row]

        enstru = EnsTruCode.objects.create(
            code=row[0],
            name=row[1]
        )
