from pydantic.dataclasses import dataclass
from typing import Final


@dataclass
class Plot:
    n_rows: Final[int]
    n_cols: Final[int]
    
    x_data: Final[Tuple[str]]
    y_data: Final[Tuple[str]]
    
    titles: Final[Tuple[str]]

    shared_xaxes: Final[str] = ""
    shared_yaxes: Final[str] = ""

