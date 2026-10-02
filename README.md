# Characterization of Apparent Single-Planet Systems Using NASA Exoplanet Archive Data

## Overview

This repository contains the data, analysis code, figures, tables, and manuscript files for the research study:

**Characterization of Single-Exoplanetary Systems Using NASA Exoplanet Archive (NEA) Data**

The study characterizes apparent single-planet systems using planetary, orbital, and host-star properties obtained from the NASA Exoplanet Archive.

## Data Source

The planetary and stellar data were obtained from the:

- NASA Exoplanet Archive
- Planetary Systems Composite Parameters (`pscomppars`) table

The initial sample was selected using:

`sy_pnum = 1`

This identifies systems with one currently cataloged planet in the NASA Exoplanet Archive. It does not establish that the physical system contains only one planet.

## Sample

Raw sample:

**N = 3708**

Core quality-filtered sample:

**N = 2102**

The core sample was obtained using a maximum fractional planetary-radius uncertainty of 20%.

The fractional radius uncertainty was calculated as:

$\frac{\max(|\sigma_{R,+}|,|\sigma_{R,-}|)}{R_p} \leq 0.20$

where the larger of the upper and lower radius uncertainties was used.

## Planet Classification

Planetary classifications were operationally defined using published radius-based classification schemes.

| Planet classification | Radius |
|---|---|
| Terrestrial | $R_p \leq 1.0\,R_\oplus$ |
| Super-Earth | $1.0 < R_p \leq 1.7\,R_\oplus$ |
| Sub-Neptune | $1.7 < R_p \leq 3.5\,R_\oplus$ |
| Neptunian | $3.5 < R_p \leq 6.0\,R_\oplus$ |
| Jovian | $R_p > 6.0\,R_\oplus$ |

## Analyses

The study includes analyses of:

- Planetary mass and radius distributions
- Mass-radius relationship
- Radius distribution of small planets and the radius valley
- Radius versus orbital period
- Jovian orbital eccentricity versus period
- Neptunian Desert
- Planetary classification versus host-star spectral type
- Host-star metallicity versus planetary classification
- Conventional habitable-zone irradiation of selected small planets

## Statistical Methods

The analyses use:

- Spearman rank correlation
- Chi-square test of independence
- Cramér's V
- Kruskal-Wallis test
- Mann-Whitney U tests with Holm correction
- Two-dimensional kernel density estimation (KDE)

## Repository Structure

```text
data/       Datasets used in the analysis
code/       Data retrieval and analysis scripts
figures/    Final research figures
tables/     Statistical results and supporting tables
manuscript/ Manuscript and reference files
```

## Software Environment
Python 3.13.15
*pandas 2.2.3
*numpy 2.1.3
*scipy 1.16.3
*matplotlib 3.10.0
*seaborn 0.13.2
*astropy 7.2.2
*astroquery 0.4.11
*Reproducibility

The analysis workflow is organized so that the raw NASA Exoplanet Archive dataset is processed into the core quality-filtered sample before the individual analyses are performed.

Additional parameter-specific filtering is applied only when required by a particular analysis.
