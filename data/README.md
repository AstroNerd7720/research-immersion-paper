# Data

## Source

NASA Exoplanet Archive

## Table

Planetary Systems Composite Parameters (`pscomppars`)

## Selection

`sy_pnum = 1`

## Files

### `nea_raw_2026-10-03.csv`

Raw output obtained from the NASA Exoplanet Archive query.

Sample size:

**N = 3708**

### `nea_core_2026-10-03.csv`

Core quality-filtered dataset used for the main population-level analyses.

Sample size:

**N = 2102**

## Core Radius-Quality Criterion

A maximum fractional radius uncertainty of 20% was used:

$\frac{\max(|\sigma_{R,+}|,|\sigma_{R,-}|)}{R_p} \leq 0.20$

Both upper and lower radius uncertainties were required to be available.
