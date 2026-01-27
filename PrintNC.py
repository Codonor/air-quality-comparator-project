import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

## Load the NetCDF file
ds = xr.open_dataset(r"D:\Polution\June\S5P_OFFL_L2__NO2____20230622T114311_20230622T132441_29483_03_020500_20230624T040618.nc", engine="netcdf4")
print(ds)

## Access the PRODUCT group
ds = xr.open_dataset(r"D:\Polution\June\S5P_OFFL_L2__NO2____20230622T114311_20230622T132441_29483_03_020500_20230624T040618.nc",
                  group="PRODUCT")

lat = ds['latitude']
lon = ds['longitude']
no2 = ds['nitrogendioxide_tropospheric_column']
qa  = ds['qa_value']


## Good quality pixels only
good = qa > 0.75

# Bristol bounding box
bristol = (
    (lat > 51.3) & (lat < 51.7) &
    (lon > -2.8) & (lon < -2.2)
)

## Scatter plot of all data points
no2_bristol = no2.where(good & bristol)

good = qa > 0.75
print(int((bristol & good).sum()))

plt.scatter(lon.values, lat.values, s=1)
plt.scatter(-2.584482, 51.462839, color='red', s=50)
plt.xlim(-3, -2)
plt.ylim(51, 52)
plt.show()

## Scatter plot of NO2 over Bristol

plt.scatter(lon.where(bristol & good), lat.where(bristol & good),
            c=no2.where(bristol & good), cmap='inferno', s=20)
plt.colorbar(label='NO₂ column (mol/m²)')
plt.scatter(-2.584482, 51.457968, color='cyan', s=50)  ## AURN station
plt.title("TROPOMI NO₂ over Bristol")
plt.show()

## Map with Cartopy

## Bristol bounding box
extent = [-3, -2, 51, 52]

fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent(extent, crs=ccrs.PlateCarree())

## Add map features
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

## Plot NO₂
sc = ax.scatter(
    lon.where(bristol & good),
    lat.where(bristol & good),
    c=no2.where(bristol & good),
    cmap='inferno',
    s=20,
    transform=ccrs.PlateCarree()
)

plt.colorbar(sc, label='NO₂ column (mol/m²)')
ax.scatter(-2.584482, 51.457968, color='cyan', s=50, transform=ccrs.PlateCarree())
plt.title("TROPOMI NO₂ over Bristol")
plt.show()