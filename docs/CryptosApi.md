# equibles_cryptos.CryptosApi

All URIs are relative to *https://api.equibles.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](CryptosApi.md#list) | **GET** /cryptos/list | Get a list of all the available crytocurrencies.
[**profile**](CryptosApi.md#profile) | **GET** /cryptos/profile | The profile of this cryptocurrency.

# **list**
> CryptoCurrencyProfilesResponse list(page=page, page_size=page_size)

Get a list of all the available crytocurrencies.

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the page to request. | [optional] [default to 1]
 **page_size** | **int**| The number of elements in each page. Max value: 100. | [optional] [default to 100]

### Return type

[**CryptoCurrencyProfilesResponse**](CryptoCurrencyProfilesResponse.md)

### Authorization

[Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile**
> CryptoCurrencyProfileResponse profile(ticker)

The profile of this cryptocurrency.

### Example
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
ticker = 'ticker_example' # str | The cryptocurrency ticker. Example: BTC (for Bitcoin)

try:
    # The profile of this cryptocurrency.
    api_response = api_instance.profile(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptosApi->profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| The cryptocurrency ticker. Example: BTC (for Bitcoin) | 

### Return type

[**CryptoCurrencyProfileResponse**](CryptoCurrencyProfileResponse.md)

### Authorization

[Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

