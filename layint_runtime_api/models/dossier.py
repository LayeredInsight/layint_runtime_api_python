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


class Dossier(object):
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
        'files': 'list[str]',
        'programs': 'list[str]',
        'ports': 'list[int]',
        'i_ps': 'list[str]'
    }

    attribute_map = {
        'files': 'Files',
        'programs': 'Programs',
        'ports': 'Ports',
        'i_ps': 'IPs'
    }

    def __init__(self, files=None, programs=None, ports=None, i_ps=None):
        """
        Dossier - a model defined in Swagger
        """

        self._files = None
        self._programs = None
        self._ports = None
        self._i_ps = None

        if files is not None:
          self.files = files
        if programs is not None:
          self.programs = programs
        if ports is not None:
          self.ports = ports
        if i_ps is not None:
          self.i_ps = i_ps

    @property
    def files(self):
        """
        Gets the files of this Dossier.
        List of files that the container has accessed

        :return: The files of this Dossier.
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this Dossier.
        List of files that the container has accessed

        :param files: The files of this Dossier.
        :type: list[str]
        """

        self._files = files

    @property
    def programs(self):
        """
        Gets the programs of this Dossier.
        List of programs that the container has executed

        :return: The programs of this Dossier.
        :rtype: list[str]
        """
        return self._programs

    @programs.setter
    def programs(self, programs):
        """
        Sets the programs of this Dossier.
        List of programs that the container has executed

        :param programs: The programs of this Dossier.
        :type: list[str]
        """

        self._programs = programs

    @property
    def ports(self):
        """
        Gets the ports of this Dossier.
        List of network ports that the container has accessed

        :return: The ports of this Dossier.
        :rtype: list[int]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this Dossier.
        List of network ports that the container has accessed

        :param ports: The ports of this Dossier.
        :type: list[int]
        """

        self._ports = ports

    @property
    def i_ps(self):
        """
        Gets the i_ps of this Dossier.
        List of IP addressses that the container has communicated with

        :return: The i_ps of this Dossier.
        :rtype: list[str]
        """
        return self._i_ps

    @i_ps.setter
    def i_ps(self, i_ps):
        """
        Sets the i_ps of this Dossier.
        List of IP addressses that the container has communicated with

        :param i_ps: The i_ps of this Dossier.
        :type: list[str]
        """

        self._i_ps = i_ps

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
        if not isinstance(other, Dossier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
