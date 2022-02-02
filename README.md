# Equibles Cryptos API for Python

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/equibles/cryptos-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/equibles/cryptos-python.git`)

Then import the package:
```python
import equibles_cryptos 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import equibles_cryptos
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import equibles_cryptos
from equibles_cryptos.rest import ApiException
from pprint import pprint

# Configure API key authorization: Query String
configuration = equibles_cryptos.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = equibles_cryptos.CryptosApi(equibles_cryptos.ApiClient(configuration))
page = 1 # int | The number of the page to request. (optional) (default to 1)
page_size = 100 # int | The number of elements in each page. Max value: 100. (optional) (default to 100)

try:
    # Get a list of all the available crytocurrencies.
    api_response = api_instance.list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptosApi->list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.equibles.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CryptosApi* | [**list**](docs/CryptosApi.md#list) | **GET** /cryptos/list | Get a list of all the available crytocurrencies.
*CryptosApi* | [**profile**](docs/CryptosApi.md#profile) | **GET** /cryptos/profile | The profile of this cryptocurrency.
*PricesApi* | [**end_of_day**](docs/PricesApi.md#end_of_day) | **GET** /cryptos/prices/endofday | Lists the end of day prices for a given cryptocurrency.
*PricesApi* | [**intraday**](docs/PricesApi.md#intraday) | **GET** /cryptos/prices/intraday | Lists the intraday prices for a given cryptocurrency with one minute precision.

## Documentation For Models

 - [AssetType](docs/AssetType.md)
 - [CryptoCurrencyProfile](docs/CryptoCurrencyProfile.md)
 - [CryptoCurrencyProfileResponse](docs/CryptoCurrencyProfileResponse.md)
 - [CryptoCurrencyProfilesResponse](docs/CryptoCurrencyProfilesResponse.md)
 - [Exchange](docs/Exchange.md)
 - [Image](docs/Image.md)
 - [Price](docs/Price.md)
 - [PricesResponse](docs/PricesResponse.md)
 - [ResponseStatus](docs/ResponseStatus.md)

## Documentation For Authorization


## Query String

- **Type**: API key
- **API key parameter name**: ApiKey
- **Location**: URL query string


## Author
[Equibles](https://www.equibles.com)\
equibles@gmail.com
