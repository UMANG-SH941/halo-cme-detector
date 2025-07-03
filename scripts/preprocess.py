import cdflib
import pandas as pd
import os

def convert_cdf_to_df(cdf_path):
    cdf = cdflib.CDF(cdf_path)
    time = cdflib.cdfepoch.to_datetime(cdf.varget('Epoch'))
    proton_flux = cdf.varget('Proton_Flux')
    alpha_flux = cdf.varget('Alpha_Flux')

    df = pd.DataFrame({
        'Time': time,
        'Proton_Flux': proton_flux,
        'Alpha_Flux': alpha_flux
    })
    return df

if __name__ == "__main__":
    file_path = "data/raw/sample.CDF"  # replace with actual file
    df = convert_cdf_to_df(file_path)
    df.to_csv("data/processed/sample.csv", index=False)
    print("Converted and saved!")
