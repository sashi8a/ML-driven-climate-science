# 🌍 ML-Driven Climate Emulation & Forecasting

## Project Overview
This repository houses an active research initiative exploring the application of Machine Learning (ML) techniques to Earth System Science. 

The primary goal is to **forecast, emulate, and downscale** critical climate variables that act as fundamental drivers in energy and commodity markets. By bridging climate dynamics with market-relevant indicators, this project aims to improve predictive capabilities for renewable energy generation (wind/solar) and resource availability.

## 🎯 Research Objectives
* **Climate Emulation:** Developing lightweight ML surrogates to approximate expensive physical simulations (e.g., GCMs).
* **Market-Relevant Forecasting:** Focusing on variables that directly impact energy supply curves:
    * *Solar:* Irradiance (GHI/DNI) and Cloud Cover properties.
    * *Wind:* Near-surface wind speed and vector components (u, v).
    * *Hydro/Agri:* Precipitation rates and water availability (soil moisture).
* **Downscaling:** Improving the spatial resolution of coarse reanalysis data for localized impact assessment.

## 🛰️ Data Sources
We utilize petabyte-scale climate datasets from major institutional providers:
* **ERA5 Reanalysis (ECMWF):** The backbone for historical ground-truth weather data (hourly estimates).
* **CMIP6 (Coupled Model Intercomparison Project):** Future climate projection scenarios for long-term horizon analysis.
* **Satellite Observations:** Supplementary remote sensing data for validation.

## 🧪 Key Variables & Market Impact
| Variable | Unit | Commodity Market Relevance |
| :--- | :--- | :--- |
| **Global Horizontal Irradiance (GHI)** | $W/m^2$ | Direct proxy for Solar PV generation output. |
| **Total Cloud Cover** | 0-1 | Inverse correlation with solar production; demand variability. |
| **10m / 100m Wind Components** | $m/s$ | Wind farm efficiency; base-load power variance. |
| **Total Precipitation** | $mm$ | Hydroelectric reservoir levels; agricultural crop yields. |

## 🧠 Methodologies (Active Development)
This project is currently experimenting with the following architectures:
* **Convolutional LSTMs (ConvLSTM):** For capturing spatiotemporal dependencies in weather grids.
* **UNet / ResNet:** For image-to-image tasks (e.g., super-resolution/downscaling).
* **Physics-Informed Neural Networks (PINNs):** Constraining ML predictions with thermodynamic laws.
* **Gaussian Processes:** For uncertainty quantification in sparse data regions.

## 📂 Repository Structure
```text
ML-Climate-Science/
├── data/
│   ├── raw/             # Raw NetCDF/GRIB files (Not synced to Git)
│   ├── processed/       # Cleaned .zarr or .npy arrays
│   └── download_scripts/# Scripts using CDSAPI / Pangeo
├── notebooks/           # Exploratory Data Analysis (EDA) and visualization
├── src/
│   ├── preprocessing.py # Xarray manipulation and regridding
│   ├── emulators.py     # Neural Network architecture definitions
│   └── evaluation.py    # RMSE, Anomaly Correlation Coefficient (ACC) metrics
├── configs/             # Hyperparameter configuration files (YAML)
└── README.md
