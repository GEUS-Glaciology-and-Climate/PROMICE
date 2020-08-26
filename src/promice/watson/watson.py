
import pandas as pd

def discharge():
    URL = "https://promice.org/PromiceDataPortal/api/download/27633c40-6514-44de-985e-de8e6f572a0c/v1.0.0/Watson+River+discharge+%282006-2019%29/Watson_discharge_day_v03.txt"
    df = pd.read_csv(URL, sep="\s+", parse_dates=[[0,1,2]], index_col=0)\
           .rename({"WaterFluxDiversOnly(m3/s)"         : "divers",
                    "Uncertainty(m3/s)"                 : "divers_err",
                    "WaterFluxDivers&Temperature(m3/s)" : "divers_t",
                    "Uncertainty(m3/s).1"               : "divers_t_err",
                    "WaterFluxCumulative(km3)"          : "Q",
                    "Uncertainty(km3)"                  : "err"}, 
                   axis='columns')\
           .drop(["DayOfYear", "DayOfCentury", "divers", "divers_err", "divers_t", "divers_t_err"], axis='columns')
    df.index.name = "Date"
    return df

