# coding: utf-8

"""
    Cryptos

    <h3>Authentication</h3>                     You need to authenticate to use this API.                     To authenticate click on the \"Authorize\" button and do one of the following steps.<br />                     1. Send your API key in the headers of the request by typing \"Bearer my-key\" on the Bearer authorization scheme.<br />                     2. Send your API key on the \"ApiKey\" query string parameter. To do this type your API key in the Query String authorization scheme.<br />                     Both methods are equally valid. We offer both options so that you can use the method that is easier to use in your application.<br />                     <br />                     <h3>API limits</h3>                     Your API key may be subject to daily/hourly limits. To know how much requests you have left look at the following headers in the response.<br />                     1. <strong>x-ratelimit-limit</strong> - The total number of requests that you are allowed to make in a given period (hour/day)                       2. <strong>x-ratelimit-remaining</strong> - The number of remaining requests that you can perform in the current period.<br />                     3. <strong>x-ratelimit-reset</strong> - The number of seconds until the current period resets.<br />                     <br />                     <h3>Suggestions</h3>                     You don't need to implement the whole API by hand in your programming language of choice.<br />                     Since this API has an OpenAPI specification you can use                      <a href=\"https://github.com/swagger-api/swagger-codegen\" target=\"_blank\">Swagger Generator</a>                      to automatically generate client stubs for more than 30 programming languages.                     <br />                     <br />                     You don't have an API key? <a href=\"https://api.equibles.com/pricing\" target=\"_blank\">Get one for free here.</a>  # noqa: E501

    OpenAPI spec version: v1
    Contact: equibles@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CryptoCurrencyProfile(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'logo': 'Image',
        'market_cap': 'int',
        'circulating_supply': 'int',
        'max_supply': 'int',
        'description': 'str',
        'website': 'str',
        'ticker': 'str',
        'full_ticker': 'str',
        'asset_type': 'AssetType',
        'name': 'str',
        'exchange': 'Exchange',
        'last_price': 'Price'
    }

    attribute_map = {
        'logo': 'logo',
        'market_cap': 'marketCap',
        'circulating_supply': 'circulatingSupply',
        'max_supply': 'maxSupply',
        'description': 'description',
        'website': 'website',
        'ticker': 'ticker',
        'full_ticker': 'fullTicker',
        'asset_type': 'assetType',
        'name': 'name',
        'exchange': 'exchange',
        'last_price': 'lastPrice'
    }

    def __init__(self, logo=None, market_cap=None, circulating_supply=None, max_supply=None, description=None, website=None, ticker=None, full_ticker=None, asset_type=None, name=None, exchange=None, last_price=None):  # noqa: E501
        """CryptoCurrencyProfile - a model defined in Swagger"""  # noqa: E501
        self._logo = None
        self._market_cap = None
        self._circulating_supply = None
        self._max_supply = None
        self._description = None
        self._website = None
        self._ticker = None
        self._full_ticker = None
        self._asset_type = None
        self._name = None
        self._exchange = None
        self._last_price = None
        self.discriminator = None
        if logo is not None:
            self.logo = logo
        if market_cap is not None:
            self.market_cap = market_cap
        if circulating_supply is not None:
            self.circulating_supply = circulating_supply
        if max_supply is not None:
            self.max_supply = max_supply
        if description is not None:
            self.description = description
        if website is not None:
            self.website = website
        if ticker is not None:
            self.ticker = ticker
        if full_ticker is not None:
            self.full_ticker = full_ticker
        if asset_type is not None:
            self.asset_type = asset_type
        if name is not None:
            self.name = name
        if exchange is not None:
            self.exchange = exchange
        if last_price is not None:
            self.last_price = last_price

    @property
    def logo(self):
        """Gets the logo of this CryptoCurrencyProfile.  # noqa: E501


        :return: The logo of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: Image
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this CryptoCurrencyProfile.


        :param logo: The logo of this CryptoCurrencyProfile.  # noqa: E501
        :type: Image
        """

        self._logo = logo

    @property
    def market_cap(self):
        """Gets the market_cap of this CryptoCurrencyProfile.  # noqa: E501


        :return: The market_cap of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: int
        """
        return self._market_cap

    @market_cap.setter
    def market_cap(self, market_cap):
        """Sets the market_cap of this CryptoCurrencyProfile.


        :param market_cap: The market_cap of this CryptoCurrencyProfile.  # noqa: E501
        :type: int
        """

        self._market_cap = market_cap

    @property
    def circulating_supply(self):
        """Gets the circulating_supply of this CryptoCurrencyProfile.  # noqa: E501


        :return: The circulating_supply of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: int
        """
        return self._circulating_supply

    @circulating_supply.setter
    def circulating_supply(self, circulating_supply):
        """Sets the circulating_supply of this CryptoCurrencyProfile.


        :param circulating_supply: The circulating_supply of this CryptoCurrencyProfile.  # noqa: E501
        :type: int
        """

        self._circulating_supply = circulating_supply

    @property
    def max_supply(self):
        """Gets the max_supply of this CryptoCurrencyProfile.  # noqa: E501


        :return: The max_supply of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_supply

    @max_supply.setter
    def max_supply(self, max_supply):
        """Sets the max_supply of this CryptoCurrencyProfile.


        :param max_supply: The max_supply of this CryptoCurrencyProfile.  # noqa: E501
        :type: int
        """

        self._max_supply = max_supply

    @property
    def description(self):
        """Gets the description of this CryptoCurrencyProfile.  # noqa: E501


        :return: The description of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CryptoCurrencyProfile.


        :param description: The description of this CryptoCurrencyProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def website(self):
        """Gets the website of this CryptoCurrencyProfile.  # noqa: E501


        :return: The website of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this CryptoCurrencyProfile.


        :param website: The website of this CryptoCurrencyProfile.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def ticker(self):
        """Gets the ticker of this CryptoCurrencyProfile.  # noqa: E501


        :return: The ticker of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this CryptoCurrencyProfile.


        :param ticker: The ticker of this CryptoCurrencyProfile.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def full_ticker(self):
        """Gets the full_ticker of this CryptoCurrencyProfile.  # noqa: E501


        :return: The full_ticker of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: str
        """
        return self._full_ticker

    @full_ticker.setter
    def full_ticker(self, full_ticker):
        """Sets the full_ticker of this CryptoCurrencyProfile.


        :param full_ticker: The full_ticker of this CryptoCurrencyProfile.  # noqa: E501
        :type: str
        """

        self._full_ticker = full_ticker

    @property
    def asset_type(self):
        """Gets the asset_type of this CryptoCurrencyProfile.  # noqa: E501


        :return: The asset_type of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: AssetType
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this CryptoCurrencyProfile.


        :param asset_type: The asset_type of this CryptoCurrencyProfile.  # noqa: E501
        :type: AssetType
        """

        self._asset_type = asset_type

    @property
    def name(self):
        """Gets the name of this CryptoCurrencyProfile.  # noqa: E501


        :return: The name of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CryptoCurrencyProfile.


        :param name: The name of this CryptoCurrencyProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def exchange(self):
        """Gets the exchange of this CryptoCurrencyProfile.  # noqa: E501


        :return: The exchange of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: Exchange
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this CryptoCurrencyProfile.


        :param exchange: The exchange of this CryptoCurrencyProfile.  # noqa: E501
        :type: Exchange
        """

        self._exchange = exchange

    @property
    def last_price(self):
        """Gets the last_price of this CryptoCurrencyProfile.  # noqa: E501


        :return: The last_price of this CryptoCurrencyProfile.  # noqa: E501
        :rtype: Price
        """
        return self._last_price

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this CryptoCurrencyProfile.


        :param last_price: The last_price of this CryptoCurrencyProfile.  # noqa: E501
        :type: Price
        """

        self._last_price = last_price

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CryptoCurrencyProfile, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CryptoCurrencyProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
