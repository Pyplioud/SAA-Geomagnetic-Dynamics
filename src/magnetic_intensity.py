import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import ppigrf
import cartopy.crs as ccrs
import cartopy.feature as cfeature

x = np.linspace(-180, 180, 100)
y = np.linspace(-89.9, 89.9, 50)
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(12, 6), subplot_kw={'projection': ccrs.PlateCarree()})

ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=':')

vmin, vmax = 22000, 65000 

date_init = datetime(1900, 1, 1)
Be, Bn, Bu = ppigrf.igrf(X, Y, 0, date_init)

F_init = np.sqrt(Be**2 + Bn**2 + Bu**2).squeeze()

contour = ax.contourf(X, Y, F_init, levels=50, cmap='cividis', vmin=vmin, vmax=vmax, transform=ccrs.PlateCarree())
plt.colorbar(contour, label="Total Intensity F (nT)")
title = ax.set_title("Total Intensity of the Magnetic Field - Year: 1900")

def update(year):
    global contour
    contour.remove()

    date = datetime(int(year), 1, 1)
    Be, Bn, Bu = ppigrf.igrf(X, Y, 0, date)
    
    Z = np.sqrt(Be**2 + Bn**2 + Bu**2).squeeze()

    contour = ax.contourf(X, Y, Z, levels=50, cmap='cividis', vmin=vmin, vmax=vmax)
    title.set_text(f"Total Intensity of the Magnetic Field - Year: {int(year)}")
    
    return contour

years = np.arange(1900, 2026, 5)

ani = FuncAnimation(
    fig,
    update,
    frames=years,
    interval=150, 
    blit=False
)

plt.show()