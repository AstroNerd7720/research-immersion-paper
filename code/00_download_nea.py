
import pandas as pd
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive


total_raw = NasaExoplanetArchive.query_criteria(
    table='pscomppars',
    select=(
        # Identifiers & System Multiplicity
        'pl_name, hostname, sy_snum, sy_pnum, discoverymethod, disc_year, '

        # Planetary Parameters
        'pl_orbper, pl_orbsmax, pl_orbincl '
        'pl_rade, pl_radeerr1, pl_radeerr2, '
        'pl_radj, '
        'pl_bmasse, pl_bmasseerr1, pl_bmasseerr2, '
        'pl_bmassj, pl_dens, '
        'pl_orbeccen, pl_orbeccenerr1, pl_orbeccenerr2, '
        'pl_insol, pl_eqt, '

        # Stellar Parameters
        'st_spectype, st_teff, st_rad, st_mass, st_met'
    )
)

# Convert astroquery Table to pandas DataFrame
df_total = total_raw.to_pandas()
print(f"Raw Master Sample Size: n = {len(df_total)}")

#df.to_csv('download_nea_2026_10_03.csv', index=False)
