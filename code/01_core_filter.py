
import pandas as pd
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive


df = NasaExoplanetArchive.query_criteria(
    table='pscomppars',
    select=(
        # Identifiers & System Multiplicity
        'pl_name, hostname, sy_snum, sy_pnum, discoverymethod, disc_year, '

        # Planetary Parameters
        'pl_orbper, pl_orbsmax, pl_orbincl, pl_orbpererr1, pl_orbpererr2, pl_orbper_reflink, '
        'pl_rade, pl_radeerr1, pl_radeerr2, '
        'pl_radj, '
        'pl_bmasse, pl_bmasseerr1, pl_bmasseerr2, pl_bmassprov, pl_bmasse_reflink, '
        'pl_bmassj, pl_dens, '
        'pl_orbeccen, pl_orbeccenerr1, pl_orbeccenerr2, '
        'pl_insol, pl_eqt, '

        # Stellar Parameters
        'st_spectype, st_teff, st_rad, st_mass, st_met'
    ),
    where='sy_pnum = 1'
)

# Convert astroquery Table to pandas DataFrame
df = df.to_pandas()
print(f"Raw Master Sample Size: n = {len(df)}")

df.to_csv('nea_raw_2026_10_03.csv', index=False)
