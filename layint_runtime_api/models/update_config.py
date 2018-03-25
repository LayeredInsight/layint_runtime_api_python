# coding: utf-8

"""
    Layered Control

    LI Control provides dynamic runtime security and analytics for containerized applications. You can find out more about the Layered Insight Suite at [http://layeredinsight.com](http://layeredinsight.com).

    OpenAPI spec version: 0.9.4
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'logging': 'bool',
        'sniffing': 'bool',
        'default': 'bool'
    }

    attribute_map = {
        'logging': 'Logging',
        'sniffing': 'Sniffing',
        'default': 'Default'
    }

    def __init__(self, logging=False, sniffing=False, default=False):
        """
        UpdateConfig - a model defined in Swagger
        """

        self._logging = None
        self._sniffing = None
        self._default = None

        if logging is not None:
          self.logging = logging
        if sniffing is not None:
          self.sniffing = sniffing
        if default is not None:
          self.default = default

    @property
    def logging(self):
        """
        Gets the logging of this UpdateConfig.

        :return: The logging of this UpdateConfig.
        :rtype: bool
        """
        return self._logging

    @logging.setter
    def logging(self, logging):
        """
        Sets the logging of this UpdateConfig.

        :param logging: The logging of this UpdateConfig.
        :type: bool
        """

        self._logging = logging

    @property
    def sniffing(self):
        """
        Gets the sniffing of this UpdateConfig.

        :return: The sniffing of this UpdateConfig.
        :rtype: bool
        """
        return self._sniffing

    @sniffing.setter
    def sniffing(self, sniffing):
        """
        Sets the sniffing of this UpdateConfig.

        :param sniffing: The sniffing of this UpdateConfig.
        :type: bool
        """

        self._sniffing = sniffing

    @property
    def default(self):
        """
        Gets the default of this UpdateConfig.

        :return: The default of this UpdateConfig.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this UpdateConfig.

        :param default: The default of this UpdateConfig.
        :type: bool
        """

        self._default = default

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UpdateConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
