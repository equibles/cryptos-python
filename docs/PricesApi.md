# equibles_cryptos.PricesApi

All URIs are relative to *https://api.equibles.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**end_of_day**](PricesApi.md#end_of_day) | **GET** /cryptos/prices/endofday | Lists the end of day prices for a given cryptocurrency.
[**intraday**](PricesApi.md#intraday) | **GET** /cryptos/prices/intraday | Lists the intraday prices for a given cryptocurrency with one minute precision.

# **end_of_day**
> PricesResponse end_of_day(ticker, start_time=start_time, end_time=end_time, page=page, page_size=page_size)

Lists the end of day prices for a given cryptocurrency.

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
api_instance = equibles_cryptos.PricesApi(equibles_cryptos.ApiClient(configuration))
ticker = 'ticker_example' # str | The ticker of the cryptocurrency. Example: BTC (for Bitcoin)
start_time = '2013-10-20T19:20:30+01:00' # datetime | The start time of the window. UTC time formatted according to ISO 8601 (i.e: 2022-02-01T13:45:17) (optional)
end_time = '2013-10-20T19:20:30+01:00' # datetime | The end time of the window. UTC time formatted according to ISO 8601 (i.e: 2022-02-01T13:45:17) (optional)
page = 1 # int | The number of the page to request. (optional) (default to 1)
page_size = 1000 # int | The number of elements in each page. Max value: 50000. (optional) (default to 1000)

try:
    # Lists the end of day prices for a given cryptocurrency.
    api_response = api_instance.end_of_day(ticker, start_time=start_time, end_time=end_time, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricesApi->end_of_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| The ticker of the cryptocurrency. Example: BTC (for Bitcoin) | 
 **start_time** | **datetime**| The start time of the window. UTC time formatted according to ISO 8601 (i.e: 2022-02-01T13:45:17) | [optional] 
 **end_time** | **datetime**| The end time of the window. UTC time formatted according to ISO 8601 (i.e: 2022-02-01T13:45:17) | [optional] 
 **page** | **int**| The number of the page to request. | [optional] [default to 1]
 **page_size** | **int**| The number of elements in each page. Max value: 50000. | [optional] [default to 1000]

### Return type

[**PricesResponse**](PricesResponse.md)

### Authorization

[Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intraday**
> PricesResponse intraday(ticker, start_time=start_time, end_time=end_time, page=page, page_size=page_size)

Lists the intraday prices for a given cryptocurrency with one minute precision.

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
api_instance = equibles_cryptos.PricesApi(equibles_cryptos.ApiClient(configuration))
ticker = 'ticker_example' # str | The ticker of the cryptocurrency. Example: BTC (for Bitcoin)
start_time = '2013-10-20T19:20:30+01:00' # datetime | The start time of the window. UTC time formatted according to ISO 8601 (i.e: 2022-02-01T13:45:17) (optional)
end_time = '2013-10-20T19:20:30+01:00' # datetime | The end time of the window. UTC time formatted according to ISO 8601 (i.e: 2022-02-01T13:45:17) (optional)
page = 1 # int | The number of the page to request. (optional) (default to 1)
page_size = 1000 # int | The number of elements in each page. Max value: 50000. (optional) (default to 1000)

try:
    # Lists the intraday prices for a given cryptocurrency with one minute precision.
    api_response = api_instance.intraday(ticker, start_time=start_time, end_time=end_time, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricesApi->intraday: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| The ticker of the cryptocurrency. Example: BTC (for Bitcoin) | 
 **start_time** | **datetime**| The start time of the window. UTC time formatted according to ISO 8601 (i.e: 2022-02-01T13:45:17) | [optional] 
 **end_time** | **datetime**| The end time of the window. UTC time formatted according to ISO 8601 (i.e: 2022-02-01T13:45:17) | [optional] 
 **page** | **int**| The number of the page to request. | [optional] [default to 1]
 **page_size** | **int**| The number of elements in each page. Max value: 50000. | [optional] [default to 1000]

### Return type

[**PricesResponse**](PricesResponse.md)

### Authorization

[Query String](../README.md#Query String)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

