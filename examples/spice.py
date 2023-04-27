from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import spiceypy as spice

print(spice.tkvrsn("TOOLKIT"))

HERE = Path(__file__).parent
DATA = HERE / ".." / "data"

spice.furnsh(f"{DATA.as_posix()}/metakernel.tm")

step = 4000
utc = ["Jun 20, 2016", "Dec 1, 2040"]

et0 = spice.str2et(utc[0])
etf = spice.str2et(utc[1])

print(f"ET0: {et0}, ETF: {etf}")

times = [x * (etf-et0)/step + et0 for x in range(step)]

mercury, _ = spice.spkpos("1", times, "J2000", "NONE", "10")
venus, _ = spice.spkpos("2", times, "J2000", "NONE", "SUN")
earth, _ = spice.spkpos("3", times, "J2000", "NONE", "SUN")
moon, _ = spice.spkpos("301", times, "J2000", "NONE", "SUN")
mars, _ = spice.spkpos("4", times, "J2000", "NONE", "SUN")
jupiter, _ = spice.spkpos("5", times, "J2000", "NONE", "SUN")
saturn, _ = spice.spkpos("6", times, "J2000", "NONE", "SUN")

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(*(mercury.T))
ax.plot(*(venus.T))
ax.plot(*(earth.T))
ax.plot(*(moon.T))
ax.plot(*(mars.T))
ax.plot(*(jupiter.T))
ax.plot(*(saturn.T))
plt.show()
