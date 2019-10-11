import requests
import pandas as pd

def get_country_code(country, code_len=3):
    '''Obtains ISO 3166 code given a country.

    Args:
        country: country name
        code_len: alpha len of code (2 or 3, default 3)
    '''

    # API calling
    query = 'https://restcountries.eu/rest/v2/name' + country
    country_info = requests.get(query).json()[0]

    # Extract country code from json
    country_code_key = f'alpha{str(code_len)}Code'
    country_code = country_info.get(country_code_key)

    return country_code

def check_country_code(country_code):
    '''Returns a boolean if a country code exists.'''

    # API calling
    query = 'https://restcountries.eu/rest/v2/alpha/' + country_code

    # Check if the response is valid
    return requests.get(query).ok

def get_annual_asylum_stats(year, origin_country=None, asylum_country=None):
    '''Returns a dicionary with asylum seekers stats in given year.

    Args:
        year
        origin_country: origin country code or name (optional)
        asylum_country: asylum country code or name (optional)
    '''

    # Set API parameters
    year_parameter = '?year=' + str(year)
    origin_country_parameter = ''
    asylum_country_parameter = ''

    if origin_country:
        # If origin_country is the country name, get its country code
        if check_country_code(origin_country) == False:
            origin_country = get_country_code(origin_country)
            origin_country_parameter = '&country_of_origin=' + origin_country

    if asylum_country:
        # If asylum_country is the country name, get its country code
        if check_country_code(asylum_country) == False:
            asylum_country = get_country_code(asylum_country)
            asylum_country_parameter = '&country_of_asylum=' + asylum_country

    # API calling
    api_url = 'http://data.unhcr.org/api/stats/asylum_seekers.json'
    query = api_url + year_parameter + origin_country_parameter + asylum_country_parameter
    annual_asylum_stats = requests.get(query).json()

    return annual_asylum_stats

def asylum_stats_to_dataframe(first_year, last_year, origin_country=None, asylum_country=None):
    '''Creates a dataframe with asylum seekers stats between given years.

    Args:
        first_year: beginning of period (included)
        last_year: end of period (included)
        origin_country: origin country code or name (optional)
        asylum: asylum country code or name (optional)
    '''

    # Iterate over years period
    years_period = range(first_year, last_year + 1)
    for year in years_period:
        annual_asylum_stats = get_annual_asylum_stats(year, origin_country, asylum_country)

        # Append stats to the dataframe. Create it first if it doesn't exist
        try:
            asylum_stats = asylum_stats.append([annual_asylum_stats])
        except:
            asylum_stats = pd.DataFrame(columns=annual_asylum_stats.keys())
            asylum_stats = asylum_stats.append([annual_asylum_stats])

    return asylum_stats