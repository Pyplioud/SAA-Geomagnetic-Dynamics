import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import ppigrf
import cartopy.crs as ccrs

x = np.linspace(-180, 180, 100)
y = np.linspace(-89.9, 89.9, 50)
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(12, 6))

vmin, vmax = -60000, 60000 

date_init = datetime(1900, 1, 1)
_, _, Bu_init = ppigrf.igrf(X, Y, 0, date_init)
Bu_init = Bu_init.squeeze()

contour = ax.contourf(X, Y, Bu_init, levels=50, cmap='RdBu', vmin=vmin, vmax=vmax)
plt.colorbar(contour, label='Intensity Bu (nT)')
title = ax.set_title(f"Magnetic Field - Year: 1900")

def update(year):
    global contour
    
    contour.remove()

    date = datetime(int(year), 1, 1)
    _, _, Bu = ppigrf.igrf(X, Y, 0, date)
    Z = Bu.squeeze()

    contour = ax.contourf(X, Y, Z, levels=50, cmap='RdBu', vmin=vmin, vmax=vmax)
    title.set_text(f"Magnetic Field - Year: {int(year)}")
    
    return contour

years = np.arange(1900, 2026, 5)

ani = FuncAnimation(
    fig,
    update,
    frames=years,
    interval=200, 
    blit=False
)

plt.show()