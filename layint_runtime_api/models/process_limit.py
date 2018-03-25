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


class ProcessLimit(object):
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
        'process_name': 'str',
        'rate_per_sec': 'int'
    }

    attribute_map = {
        'process_name': 'ProcessName',
        'rate_per_sec': 'RatePerSec'
    }

    def __init__(self, process_name=None, rate_per_sec=None):
        """
        ProcessLimit - a model defined in Swagger
        """

        self._process_name = None
        self._rate_per_sec = None

        if process_name is not None:
          self.process_name = process_name
        if rate_per_sec is not None:
          self.rate_per_sec = rate_per_sec

    @property
    def process_name(self):
        """
        Gets the process_name of this ProcessLimit.
        Name of process to place a limit on

        :return: The process_name of this ProcessLimit.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        """
        Sets the process_name of this ProcessLimit.
        Name of process to place a limit on

        :param process_name: The process_name of this ProcessLimit.
        :type: str
        """

        self._process_name = process_name

    @property
    def rate_per_sec(self):
        """
        Gets the rate_per_sec of this ProcessLimit.
        Limit of number of processes with specified name running. If limit is breached, alert is created. If value is 0, no enforcement happens.

        :return: The rate_per_sec of this ProcessLimit.
        :rtype: int
        """
        return self._rate_per_sec

    @rate_per_sec.setter
    def rate_per_sec(self, rate_per_sec):
        """
        Sets the rate_per_sec of this ProcessLimit.
        Limit of number of processes with specified name running. If limit is breached, alert is created. If value is 0, no enforcement happens.

        :param rate_per_sec: The rate_per_sec of this ProcessLimit.
        :type: int
        """

        self._rate_per_sec = rate_per_sec

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
        if not isinstance(other, ProcessLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
