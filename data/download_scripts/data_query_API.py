import cdsapi

dataset = "sis-energy-derived-reanalysis"
request = {
    "variable": [
        "wind_speed_at_100m",
        "wind_speed_at_10m",
        "surface_downwelling_shortwave_radiation",
        "pressure_at_sea_level",
        "2m_air_temperature",
        "total_precipitation",
        "hydro_power_generation_reservoirs",
        "hydro_power_generation_rivers",
        "solar_photovoltaic_power_generation",
        "wind_power_generation_onshore"
    ],
    "spatial_aggregation": ["country_level"],
    "energy_product_type": ["capacity_factor_ratio"],
    "temporal_aggregation": ["monthly"]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()

# This script uses the CDS API to download monthly energy-derived reanalysis data aggregated at the country level.
# To select a different set of features or variables, visit the following URL to generate a new API query:
# https://cds.climate.copernicus.eu/datasets/sis-energy-derived-reanalysis?tab=download
