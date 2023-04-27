"""Configure NASA SPICE kernels
"""

from pathlib import Path
from urllib import request

import spiceypy


HERE = Path(__file__).parent.resolve()
DATA = HERE / ".." / ".." / ".." / "data"

# get spice kernels
urls = [
    "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp",
    "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0012.tls",
    "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00010.tpc",
]
kernels = [
    DATA / "spice" / "spk" / "de430.bsp",
    DATA / "spice" / "lsk" / "naif0012.tls",
    DATA / "spice" / "pck" / "pck00010.tpc",
]

for url, kernel in zip(urls, kernels):
    request.urlretrieve(
        url=url,
        filename=kernel,
    )
