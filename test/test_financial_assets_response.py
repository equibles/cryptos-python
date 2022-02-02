# coding: utf-8

"""
    Stocks

    <h3>Authentication</h3>                     You need to authenticate to use this API.                     To authenticate click on the \"Authorize\" button and do one of the following steps.<br />                     1. Send your API key in the headers of the request by typing \"Bearer my-key\" on the Bearer authorization scheme.<br />                     2. Send your API key on the \"ApiKey\" query string parameter. To do this type your API key in the Query String authorization scheme.<br />                     Both methods are equally valid. We offer both options so that you can use the method that is easier to use in your application.<br />                     <br />                     <h3>API limits</h3>                     Your API key may be subject to daily/hourly limits. To know how much requests you have left look at the following headers in the response.<br />                     1. <strong>x-ratelimit-limit</strong> - The total number of requests that you are allowed to make in a given period (hour/day)                       2. <strong>x-ratelimit-remaining</strong> - The number of remaining requests that you can perform in the current period.<br />                     3. <strong>x-ratelimit-reset</strong> - The number of seconds until the current period resets.<br />                     <br />                     <h3>Suggestions</h3>                     You don't need to implement the whole API by hand in your programming language of choice.<br />                     Since this API has an OpenAPI specification you can use                      <a href=\"https://github.com/swagger-api/swagger-codegen\" target=\"_blank\">Swagger Generator</a>                      to automatically generate client stubs for more than 30 programming languages.                     <br />                     <br />                     You don't have an API key? <a href=\"https://www.equibles.com/api/pricing\" target=\"_blank\">Get one for free here.</a>  # noqa: E501

    OpenAPI spec version: v1
    Contact: equibles@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import equibles_cryptos
from equibles_cryptos.models.financial_assets_response import FinancialAssetsResponse  # noqa: E501
from equibles_cryptos.rest import ApiException


class TestFinancialAssetsResponse(unittest.TestCase):
    """FinancialAssetsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFinancialAssetsResponse(self):
        """Test FinancialAssetsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = equibles_cryptos.models.financial_assets_response.FinancialAssetsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
