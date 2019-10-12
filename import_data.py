import requests
import pandas as pd


def get_annual_asylum_stats(year, origin_country=None, asylum_country=None):
    """Returns a dictionary with asylum seekers stats in given year.

    Args:
        :param year:
        :param origin_country: (optional) origin country code or name
        :param asylum_country: (optional) asylum country code or name
        :return: 
    """

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
    """Creates a dataframe from asylum seekers stats between two years.

    Args:
        :param first_year: beginning of period, included
        :param last_year: end of period, included
        :param origin_country: (optional) origin country code or name
        :param asylum_country: (optional) asylum country code or name
        :return: dataframe with all the annual stats for the period.
    """

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
