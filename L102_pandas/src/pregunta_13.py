import pandas as pd
from pathlib import Path

def pregunta_13():
    """
    Combine las tablas `data/tbl0.tsv` y `data/tbl2.tsv` usando la columna
    `c0`, que ambas comparten. Luego, sume los valores de la columna `c5b`
    para cada categoría de la columna `c1`. Retorne una Serie de Pandas cuyo
    índice son las categorías, en orden alfabético, y cuyos valores son las
    sumas.

    Ejemplo del formato de la respuesta:

        c1
        A    146
        B    134
        C     81
        ...
    """

    INPUT_DIR = Path("data")

    path0 = INPUT_DIR / "tbl0.tsv"
    path2 = INPUT_DIR / "tbl2.tsv"

    tbl0 = pd.read_csv(path0, sep="\t")
    tbl2 = pd.read_csv(path2, sep="\t")

    merged = tbl0.merge(tbl2, on="c0")

    return merged.groupby('c1')['c5b'].sum()
