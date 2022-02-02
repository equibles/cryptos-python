# coding: utf-8

"""
    Cryptos

    <h3>Authentication</h3>                     You need to authenticate to use this API.                     To authenticate click on the \"Authorize\" button and do one of the following steps.<br />                     1. Send your API key in the headers of the request by typing \"Bearer my-key\" on the Bearer authorization scheme.<br />                     2. Send your API key on the \"ApiKey\" query string parameter. To do this type your API key in the Query String authorization scheme.<br />                     Both methods are equally valid. We offer both options so that you can use the method that is easier to use in your application.<br />                     <br />                     <h3>API limits</h3>                     Your API key may be subject to daily/hourly limits. To know how much requests you have left look at the following headers in the response.<br />                     1. <strong>x-ratelimit-limit</strong> - The total number of requests that you are allowed to make in a given period (hour/day)                       2. <strong>x-ratelimit-remaining</strong> - The number of remaining requests that you can perform in the current period.<br />                     3. <strong>x-ratelimit-reset</strong> - The number of seconds until the current period resets.<br />                     <br />                     <h3>Suggestions</h3>                     You don't need to implement the whole API by hand in your programming language of choice.<br />                     Since this API has an OpenAPI specification you can use                      <a href=\"https://github.com/swagger-api/swagger-codegen\" target=\"_blank\">Swagger Generator</a>                      to automatically generate client stubs for more than 30 programming languages.                     <br />                     <br />                     You don't have an API key? <a href=\"https://www.equibles.com/api/pricing\" target=\"_blank\">Get one for free here.</a>  # noqa: E501

    OpenAPI spec version: v1
    Contact: equibles@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "equibles_cryptos"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Cryptos",
    author_email="equibles@gmail.com",
    url="",
    keywords=["Swagger", "Cryptos"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    &lt;h3&gt;Authentication&lt;/h3&gt;                     You need to authenticate to use this API.                     To authenticate click on the \&quot;Authorize\&quot; button and do one of the following steps.&lt;br /&gt;                     1. Send your API key in the headers of the request by typing \&quot;Bearer my-key\&quot; on the Bearer authorization scheme.&lt;br /&gt;                     2. Send your API key on the \&quot;ApiKey\&quot; query string parameter. To do this type your API key in the Query String authorization scheme.&lt;br /&gt;                     Both methods are equally valid. We offer both options so that you can use the method that is easier to use in your application.&lt;br /&gt;                     &lt;br /&gt;                     &lt;h3&gt;API limits&lt;/h3&gt;                     Your API key may be subject to daily/hourly limits. To know how much requests you have left look at the following headers in the response.&lt;br /&gt;                     1. &lt;strong&gt;x-ratelimit-limit&lt;/strong&gt; - The total number of requests that you are allowed to make in a given period (hour/day)                       2. &lt;strong&gt;x-ratelimit-remaining&lt;/strong&gt; - The number of remaining requests that you can perform in the current period.&lt;br /&gt;                     3. &lt;strong&gt;x-ratelimit-reset&lt;/strong&gt; - The number of seconds until the current period resets.&lt;br /&gt;                     &lt;br /&gt;                     &lt;h3&gt;Suggestions&lt;/h3&gt;                     You don&#x27;t need to implement the whole API by hand in your programming language of choice.&lt;br /&gt;                     Since this API has an OpenAPI specification you can use                      &lt;a href&#x3D;\&quot;https://github.com/swagger-api/swagger-codegen\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Swagger Generator&lt;/a&gt;                      to automatically generate client stubs for more than 30 programming languages.                     &lt;br /&gt;                     &lt;br /&gt;                     You don&#x27;t have an API key? &lt;a href&#x3D;\&quot;https://www.equibles.com/api/pricing\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Get one for free here.&lt;/a&gt;  # noqa: E501
    """
)
