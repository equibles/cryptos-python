# coding: utf-8

"""
    Stocks

    <h3>Authentication</h3>                     You need to authenticate to use this API.                     To authenticate click on the \"Authorize\" button and do one of the following steps.<br />                     1. Send your API key in the headers of the request by typing \"Bearer my-key\" on the Bearer authorization scheme.<br />                     2. Send your API key on the \"ApiKey\" query string parameter. To do this type your API key in the Query String authorization scheme.<br />                     Both methods are equally valid. We offer both options so that you can use the method that is easier to use in your application.<br />                     <br />                     <h3>API limits</h3>                     Your API key may be subject to daily/hourly limits. To know how much requests you have left look at the following headers in the response.<br />                     1. <strong>x-ratelimit-limit</strong> - The total number of requests that you are allowed to make in a given period (hour/day)                       2. <strong>x-ratelimit-remaining</strong> - The number of remaining requests that you can perform in the current period.<br />                     3. <strong>x-ratelimit-reset</strong> - The number of seconds until the current period resets.<br />                     <br />                     <h3>Suggestions</h3>                     You don't need to implement the whole API by hand in your programming language of choice.<br />                     Since this API has an OpenAPI specification you can use                      <a href=\"https://github.com/swagger-api/swagger-codegen\" target=\"_blank\">Swagger Generator</a>                      to automatically generate client stubs for more than 30 programming languages.                     <br />                     <br />                     You don't have an API key? <a href=\"https://www.equibles.com/api/pricing\" target=\"_blank\">Get one for free here.</a>  # noqa: E501

    OpenAPI spec version: v1
    Contact: equibles@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DividendsResponse(object):
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
        'status': 'ResponseStatus',
        'error_message': 'str',
        'results': 'list[Dividend]',
        'count': 'int'
    }

    attribute_map = {
        'status': 'status',
        'error_message': 'errorMessage',
        'results': 'results',
        'count': 'count'
    }

    def __init__(self, status=None, error_message=None, results=None, count=None):  # noqa: E501
        """DividendsResponse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._error_message = None
        self._results = None
        self._count = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if error_message is not None:
            self.error_message = error_message
        if results is not None:
            self.results = results
        if count is not None:
            self.count = count

    @property
    def status(self):
        """Gets the status of this DividendsResponse.  # noqa: E501


        :return: The status of this DividendsResponse.  # noqa: E501
        :rtype: ResponseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DividendsResponse.


        :param status: The status of this DividendsResponse.  # noqa: E501
        :type: ResponseStatus
        """

        self._status = status

    @property
    def error_message(self):
        """Gets the error_message of this DividendsResponse.  # noqa: E501

        The error message if the request was not successful.  # noqa: E501

        :return: The error_message of this DividendsResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this DividendsResponse.

        The error message if the request was not successful.  # noqa: E501

        :param error_message: The error_message of this DividendsResponse.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def results(self):
        """Gets the results of this DividendsResponse.  # noqa: E501

        The response results.  # noqa: E501

        :return: The results of this DividendsResponse.  # noqa: E501
        :rtype: list[Dividend]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this DividendsResponse.

        The response results.  # noqa: E501

        :param results: The results of this DividendsResponse.  # noqa: E501
        :type: list[Dividend]
        """

        self._results = results

    @property
    def count(self):
        """Gets the count of this DividendsResponse.  # noqa: E501

        The total number of results in this response.  # noqa: E501

        :return: The count of this DividendsResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DividendsResponse.

        The total number of results in this response.  # noqa: E501

        :param count: The count of this DividendsResponse.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(DividendsResponse, dict):
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
        if not isinstance(other, DividendsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
