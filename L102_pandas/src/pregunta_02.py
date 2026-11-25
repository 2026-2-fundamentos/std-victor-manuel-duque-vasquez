import pandas as pd
from pathlib import Path

def pregunta_02():
    """
    ¿Cuántas columnas tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        4
    """
    input_dir = Path("data")
    path0 = input_dir / "tbl0.tsv"
    tbl0 = pd.read_csv(path0, sep = "\t")

    return tbl0.shape[1]
