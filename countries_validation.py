import requests


def get_country_code(country, code_len=3):
    """Returns ISO 3166-1 code given a valid country.

    Args:
        :param country: country name
        :param code_len: alpha len of code (2 or 3, default 3)
        :return: country code string
    """

    # API calling
    query = 'https://restcountries.eu/rest/v2/name' + country
    country_info = requests.get(query).json()[0]

    # Extract country code from json
    country_code_key = f'alpha{str(code_len)}Code'
    country_code = country_info.get(country_code_key)

    return country_code


def check_country_code(country_code):
    """Returns a boolean if a country code exists."""

    # API calling
    query = 'https://restcountries.eu/rest/v2/alpha/' + country_code

    # Check if the response is valid
    return requests.get(query).ok
