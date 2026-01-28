import cdsapi

c = cdsapi.Client()

# This is a sample request downloading 2m temperature for a single hour
# on Jan 1st, 2023.
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': '2m_temperature',
        'year': '2023',
        'month': '01',
        'day': '01',
        'time': '12:00',
        'format': 'netcdf',
    },
    'era5_sample_2m_temperature.nc')
