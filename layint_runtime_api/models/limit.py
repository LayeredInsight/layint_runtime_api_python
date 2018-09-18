# coding: utf-8

"""
    Layered Witness & Control

    LI Witness provides deep insight and analytics into containerized applications. Control provides dynamic runtime security and analytics for containerized applications. You can find out more about the Layered Insight Suite at [http://layeredinsight.com](http://layeredinsight.com).

    OpenAPI spec version: 0.9.7
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Limit(object):
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
        'max_num_proc': 'int',
        'max_proc_life': 'int',
        'syscalls': 'SyscallLimit',
        'processes': 'ProcessLimit'
    }

    attribute_map = {
        'max_num_proc': 'MaxNumProc',
        'max_proc_life': 'MaxProcLife',
        'syscalls': 'Syscalls',
        'processes': 'Processes'
    }

    def __init__(self, max_num_proc=None, max_proc_life=None, syscalls=None, processes=None):
        """
        Limit - a model defined in Swagger
        """

        self._max_num_proc = None
        self._max_proc_life = None
        self._syscalls = None
        self._processes = None

        if max_num_proc is not None:
          self.max_num_proc = max_num_proc
        if max_proc_life is not None:
          self.max_proc_life = max_proc_life
        if syscalls is not None:
          self.syscalls = syscalls
        if processes is not None:
          self.processes = processes

    @property
    def max_num_proc(self):
        """
        Gets the max_num_proc of this Limit.
        Maximum number of processes allowed to run in a container. If value is 0, no limit enforced.

        :return: The max_num_proc of this Limit.
        :rtype: int
        """
        return self._max_num_proc

    @max_num_proc.setter
    def max_num_proc(self, max_num_proc):
        """
        Sets the max_num_proc of this Limit.
        Maximum number of processes allowed to run in a container. If value is 0, no limit enforced.

        :param max_num_proc: The max_num_proc of this Limit.
        :type: int
        """

        self._max_num_proc = max_num_proc

    @property
    def max_proc_life(self):
        """
        Gets the max_proc_life of this Limit.
        Maximum lifetime, in seconds, for a process in a container. If breached, an alert will be generated. If value is 0, no limit enforced.

        :return: The max_proc_life of this Limit.
        :rtype: int
        """
        return self._max_proc_life

    @max_proc_life.setter
    def max_proc_life(self, max_proc_life):
        """
        Sets the max_proc_life of this Limit.
        Maximum lifetime, in seconds, for a process in a container. If breached, an alert will be generated. If value is 0, no limit enforced.

        :param max_proc_life: The max_proc_life of this Limit.
        :type: int
        """

        self._max_proc_life = max_proc_life

    @property
    def syscalls(self):
        """
        Gets the syscalls of this Limit.

        :return: The syscalls of this Limit.
        :rtype: SyscallLimit
        """
        return self._syscalls

    @syscalls.setter
    def syscalls(self, syscalls):
        """
        Sets the syscalls of this Limit.

        :param syscalls: The syscalls of this Limit.
        :type: SyscallLimit
        """

        self._syscalls = syscalls

    @property
    def processes(self):
        """
        Gets the processes of this Limit.

        :return: The processes of this Limit.
        :rtype: ProcessLimit
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        """
        Sets the processes of this Limit.

        :param processes: The processes of this Limit.
        :type: ProcessLimit
        """

        self._processes = processes

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
        if not isinstance(other, Limit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
