*Warning: currently the API is down, so the project is paused.*

# Refugees migratory flows
A project about asylum seekers in Europe

<p align="center"><img src="images/unhcr-logo.png"></p>

## About the project

It tries to show the magnitude of the exodus from different humanitarian crises based on data provided by the UN Refugee Agency.

### Prerequisites

Install the needed libraries for the project:

```
pip3 install requests
pip3 install pandas
```

### Sources

The following APIs are used:

- [UNHCR](http://www.vgchartz.com/gamedb/) - Main data source
- [REST countries](https://restcountries.eu) - For input options validation

### Files structure

- **main.ipynb**: Jupyter file with a project visualization
- **import_data.py**: Downloads data from UNHCR API
- **countries_validation.ipynb**: Converts input countries into codes compatible with UNHCR API
- **config.py**: Project paths configuration

Folders:

- data: imported data
- images