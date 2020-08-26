
import pandas as pd
import xarray as xr
import fsspec

# Use xarray with HTTP: https://github.com/pydata/xarray/issues/3653#issuecomment-570163736

def discharge(resolution="GIS"):
    res_file = {"gate": "https://dataverse01.geus.dk/api/access/datafile/:persistentId?persistentId=doi:10.22008/promice/data/ice_discharge/d/v02/IRLTR2",
                "sector": "https://dataverse01.geus.dk/api/access/datafile/:persistentId?persistentId=doi:10.22008/promice/data/ice_discharge/d/v02/UXWVIF",
                "region": "https://dataverse01.geus.dk/api/access/datafile/:persistentId?persistentId=doi:10.22008/promice/data/ice_discharge/d/v02/B3PQEH",
                "GIS": "https://dataverse01.geus.dk/api/access/datafile/:persistentId?persistentId=doi:10.22008/promice/data/ice_discharge/d/v02/ANRF6L"}
    
    assert(resolution in res_file.keys())
    URL = res_file[resolution]
    # download_warn(URL)
    with fsspec.open(URL) as fobj:
        ds = xr.open_dataset(fobj)

    return ds

def gates():
    URL = "https://dataverse01.geus.dk/api/access/datafile/:persistentId?persistentId=doi:10.22008/promice/data/ice_discharge/gates/v02/XDHKTU"
    # download_warn(URL)

    df = pd.read_csv(URL, delimiter="\t", index_col=0)
    return df
