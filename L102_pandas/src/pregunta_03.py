import pandas as pd
from pathlib import Path

def pregunta_03():
    """
    Usando `data/tbl0.tsv`, cuente cuántos registros hay para cada categoría
    de la columna `c1`. Retorne una Serie de Pandas cuyo índice son las
    categorías, en orden alfabético, y cuyos valores son las cantidades.

    Ejemplo del formato de la respuesta:

        c1
        A     8
        B     7
        C     5
        ...
    """
    INPUT_DIR = Path("data")
    path0 = INPUT_DIR / "tbl0.tsv"
    tbl0 = pd.read_csv(path0, sep = "\t")

    return tbl0["c1"].value_counts().sort_index()

