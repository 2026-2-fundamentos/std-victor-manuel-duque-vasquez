import pandas as pd
from pathlib import Path

def pregunta_06():
    """
    Usando `data/tbl1.tsv`, obtenga los valores distintos de la columna `c4`,
    conviértalos a mayúsculas y retórnelos como una lista ordenada
    alfabéticamente.

    Ejemplo del formato de la respuesta:

        ["A", "B", "C", "D", "E", "F", "G"]
    """

    INPUT_DIR = Path("data")
    path1 = INPUT_DIR / "tbl1.tsv"
    tbl1 = pd.read_csv(path1, sep="\t")

    return sorted(tbl1['c4'].str.upper().unique())