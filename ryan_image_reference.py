# %%
# https://drive.google.com/drive/folders/17jwyjeroLeOoA2Cpwi4jNlhoTfuvwht-?usp=drive_link

# %%
import rasterio
import pandas as pd
import numpy as np
import geopandas as gpd

from glob import glob

files = glob("100mGrid_*.gpkg")

for file in files:

    # remove '100mGrid*.gpkg' from the file name
    city_name = file.split("_")[1].split(".")[0]
    print(city_name)
    grid = gpd.read_file("100mGrid_Kano.gpkg")

    # see polygon bounds
    grid.bounds
    # get total bounds of the grid
    grid.total_bounds
    # create rasterio transform based on grid

    # get the bounds of the grid
    minx, miny, maxx, maxy = grid.total_bounds

    # get the width and height of the grid
    width = maxx - minx
    height = maxy - miny

    # get the number of rows and columns for 100m grid
    cols = int(width // 100)
    rows = int(height // 100)

    # calculate the x and y resolution
    xres = width / cols
    yres = height / rows

    # create the transform
    transform = rasterio.transform.from_origin(minx, maxy, xres, yres)

    # print the transform
    transform

    # create a raster with the same dimensions as the grid using transform

    # create an empty array with the same dimensions as the grid

    data = np.random.randint(0, 255, size=(rows, cols)).astype(np.uint8)
    # create a rasterio dataset
    with rasterio.open(
        f"100mGrid_{city_name}.tif",
        "w",
        driver="GTiff",
        height=rows,
        width=cols,
        count=1,
        dtype=data.dtype,
        crs=grid.crs,
        transform=transform,
    ) as dst:
        dst.write(data, 1)

# %%
