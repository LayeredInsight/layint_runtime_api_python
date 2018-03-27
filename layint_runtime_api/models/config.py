# coding: utf-8

"""
    Layered Witness & Control

    LI Witness provides deep insight and analytics into containerized applications. Control provides dynamic runtime security and analytics for containerized applications. You can find out more about the Layered Insight Suite at [http://layeredinsight.com](http://layeredinsight.com).

    OpenAPI spec version: 0.9.6
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Config(object):
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
        'id': 'str',
        'name': 'str',
        'user_id': 'int',
        'group_id': 'int',
        'mq': 'str',
        'policy_id': 'str',
        'logging': 'bool',
        'sniffing': 'bool',
        'date_created': 'str',
        'date_updated': 'str',
        'default': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'user_id': 'UserId',
        'group_id': 'GroupId',
        'mq': 'MQ',
        'policy_id': 'PolicyID',
        'logging': 'Logging',
        'sniffing': 'Sniffing',
        'date_created': 'DateCreated',
        'date_updated': 'DateUpdated',
        'default': 'Default'
    }

    def __init__(self, id=None, name=None, user_id=None, group_id=None, mq=None, policy_id=None, logging=False, sniffing=False, date_created=None, date_updated=None, default=False):
        """
        Config - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._user_id = None
        self._group_id = None
        self._mq = None
        self._policy_id = None
        self._logging = None
        self._sniffing = None
        self._date_created = None
        self._date_updated = None
        self._default = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if user_id is not None:
          self.user_id = user_id
        if group_id is not None:
          self.group_id = group_id
        if mq is not None:
          self.mq = mq
        if policy_id is not None:
          self.policy_id = policy_id
        if logging is not None:
          self.logging = logging
        if sniffing is not None:
          self.sniffing = sniffing
        if date_created is not None:
          self.date_created = date_created
        if date_updated is not None:
          self.date_updated = date_updated
        if default is not None:
          self.default = default

    @property
    def id(self):
        """
        Gets the id of this Config.
        12 character internal hexadecimal identifier for this Configuration

        :return: The id of this Config.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Config.
        12 character internal hexadecimal identifier for this Configuration

        :param id: The id of this Config.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Config.
        Name of the configuration

        :return: The name of this Config.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Config.
        Name of the configuration

        :param name: The name of this Config.
        :type: str
        """

        self._name = name

    @property
    def user_id(self):
        """
        Gets the user_id of this Config.
        User ID of owner of the container

        :return: The user_id of this Config.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Config.
        User ID of owner of the container

        :param user_id: The user_id of this Config.
        :type: int
        """

        self._user_id = user_id

    @property
    def group_id(self):
        """
        Gets the group_id of this Config.
        Group ID of owner of the container

        :return: The group_id of this Config.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this Config.
        Group ID of owner of the container

        :param group_id: The group_id of this Config.
        :type: int
        """

        self._group_id = group_id

    @property
    def mq(self):
        """
        Gets the mq of this Config.
        Connection string for RabbitMQ system the instrumented container should connect to. Both AMQP and AMQPS are supported.

        :return: The mq of this Config.
        :rtype: str
        """
        return self._mq

    @mq.setter
    def mq(self, mq):
        """
        Sets the mq of this Config.
        Connection string for RabbitMQ system the instrumented container should connect to. Both AMQP and AMQPS are supported.

        :param mq: The mq of this Config.
        :type: str
        """

        self._mq = mq

    @property
    def policy_id(self):
        """
        Gets the policy_id of this Config.
        12 character hexadecimal internal identifier for security policy for this Container

        :return: The policy_id of this Config.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this Config.
        12 character hexadecimal internal identifier for security policy for this Container

        :param policy_id: The policy_id of this Config.
        :type: str
        """

        self._policy_id = policy_id

    @property
    def logging(self):
        """
        Gets the logging of this Config.
        When true, specifies that behavioral logging should be sent to servers.

        :return: The logging of this Config.
        :rtype: bool
        """
        return self._logging

    @logging.setter
    def logging(self, logging):
        """
        Sets the logging of this Config.
        When true, specifies that behavioral logging should be sent to servers.

        :param logging: The logging of this Config.
        :type: bool
        """

        self._logging = logging

    @property
    def sniffing(self):
        """
        Gets the sniffing of this Config.
        When true, enables basic network monitoring for malicious activity and network behavior recording.

        :return: The sniffing of this Config.
        :rtype: bool
        """
        return self._sniffing

    @sniffing.setter
    def sniffing(self, sniffing):
        """
        Sets the sniffing of this Config.
        When true, enables basic network monitoring for malicious activity and network behavior recording.

        :param sniffing: The sniffing of this Config.
        :type: bool
        """

        self._sniffing = sniffing

    @property
    def date_created(self):
        """
        Gets the date_created of this Config.
        Timestamp for when object was created

        :return: The date_created of this Config.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Config.
        Timestamp for when object was created

        :param date_created: The date_created of this Config.
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """
        Gets the date_updated of this Config.
        Timestamp for when object was last updated

        :return: The date_updated of this Config.
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """
        Sets the date_updated of this Config.
        Timestamp for when object was last updated

        :param date_updated: The date_updated of this Config.
        :type: str
        """

        self._date_updated = date_updated

    @property
    def default(self):
        """
        Gets the default of this Config.
        Default configuration for group

        :return: The default of this Config.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this Config.
        Default configuration for group

        :param default: The default of this Config.
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
        if not isinstance(other, Config):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
