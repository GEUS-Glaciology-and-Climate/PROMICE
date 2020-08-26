
import geopandas as gpd

def ice_extent():
    URL = "https://promice.org/PromiceDataPortal/api/download/c7c1dd52-4af1-4fda-adfa-8bf126383cbc/PROMICE_250_2019-12-04_EPSG4326/PROMICE_250_2019-12-04.shp"
    URL = "https://promice.org/PromiceDataPortal/api/download/c7c1dd52-4af1-4fda-adfa-8bf126383cbc/PROMICE_250_2019-12-04_EPSG4326"

    # download_warning(URL)
    
    df = gpd.read_file(URL)
    return df

