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


class Container(object):
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
        'date_created': 'str',
        'date_updated': 'str',
        'image_id': 'str',
        'config_id': 'str',
        'status': 'str',
        'location': 'str',
        'application': 'str',
        'passive': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'user_id': 'UserId',
        'group_id': 'GroupId',
        'date_created': 'DateCreated',
        'date_updated': 'DateUpdated',
        'image_id': 'ImageId',
        'config_id': 'ConfigId',
        'status': 'Status',
        'location': 'Location',
        'application': 'Application',
        'passive': 'Passive'
    }

    def __init__(self, id=None, name=None, user_id=None, group_id=None, date_created=None, date_updated=None, image_id=None, config_id=None, status=None, location=None, application=None, passive=False):
        """
        Container - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._user_id = None
        self._group_id = None
        self._date_created = None
        self._date_updated = None
        self._image_id = None
        self._config_id = None
        self._status = None
        self._location = None
        self._application = None
        self._passive = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if user_id is not None:
          self.user_id = user_id
        if group_id is not None:
          self.group_id = group_id
        if date_created is not None:
          self.date_created = date_created
        if date_updated is not None:
          self.date_updated = date_updated
        if image_id is not None:
          self.image_id = image_id
        if config_id is not None:
          self.config_id = config_id
        if status is not None:
          self.status = status
        if location is not None:
          self.location = location
        if application is not None:
          self.application = application
        if passive is not None:
          self.passive = passive

    @property
    def id(self):
        """
        Gets the id of this Container.
        12 character internal hexadecimal identifier for this Container

        :return: The id of this Container.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Container.
        12 character internal hexadecimal identifier for this Container

        :param id: The id of this Container.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Container.
        Containers name, or empty string

        :return: The name of this Container.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Container.
        Containers name, or empty string

        :param name: The name of this Container.
        :type: str
        """

        self._name = name

    @property
    def user_id(self):
        """
        Gets the user_id of this Container.
        User ID of owner of the container

        :return: The user_id of this Container.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Container.
        User ID of owner of the container

        :param user_id: The user_id of this Container.
        :type: int
        """

        self._user_id = user_id

    @property
    def group_id(self):
        """
        Gets the group_id of this Container.
        Group ID of owner of the container

        :return: The group_id of this Container.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this Container.
        Group ID of owner of the container

        :param group_id: The group_id of this Container.
        :type: int
        """

        self._group_id = group_id

    @property
    def date_created(self):
        """
        Gets the date_created of this Container.
        Timestamp for when object was created

        :return: The date_created of this Container.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Container.
        Timestamp for when object was created

        :param date_created: The date_created of this Container.
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """
        Gets the date_updated of this Container.
        Timestamp for when object was last updated

        :return: The date_updated of this Container.
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """
        Sets the date_updated of this Container.
        Timestamp for when object was last updated

        :param date_updated: The date_updated of this Container.
        :type: str
        """

        self._date_updated = date_updated

    @property
    def image_id(self):
        """
        Gets the image_id of this Container.
        12 character hexadecimal internal identifier for container image this container is running

        :return: The image_id of this Container.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this Container.
        12 character hexadecimal internal identifier for container image this container is running

        :param image_id: The image_id of this Container.
        :type: str
        """

        self._image_id = image_id

    @property
    def config_id(self):
        """
        Gets the config_id of this Container.
        12 character hexadecimal internal identifier for Runtime configuration for this Container

        :return: The config_id of this Container.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """
        Sets the config_id of this Container.
        12 character hexadecimal internal identifier for Runtime configuration for this Container

        :param config_id: The config_id of this Container.
        :type: str
        """

        self._config_id = config_id

    @property
    def status(self):
        """
        Gets the status of this Container.
        Current status of the container.

        :return: The status of this Container.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Container.
        Current status of the container.

        :param status: The status of this Container.
        :type: str
        """
        allowed_values = ["stopped", "running"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def location(self):
        """
        Gets the location of this Container.
        Displays user defined 'location' of this container.

        :return: The location of this Container.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this Container.
        Displays user defined 'location' of this container.

        :param location: The location of this Container.
        :type: str
        """

        self._location = location

    @property
    def application(self):
        """
        Gets the application of this Container.
        Displays user defined 'Application' for this container

        :return: The application of this Container.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """
        Sets the application of this Container.
        Displays user defined 'Application' for this container

        :param application: The application of this Container.
        :type: str
        """

        self._application = application

    @property
    def passive(self):
        """
        Gets the passive of this Container.
        Instructs Runtime to bypass any protection in this container when this field is set to true

        :return: The passive of this Container.
        :rtype: bool
        """
        return self._passive

    @passive.setter
    def passive(self, passive):
        """
        Sets the passive of this Container.
        Instructs Runtime to bypass any protection in this container when this field is set to true

        :param passive: The passive of this Container.
        :type: bool
        """

        self._passive = passive

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
        if not isinstance(other, Container):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
