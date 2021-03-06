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


class Image(object):
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
        'description': 'str',
        'user_id': 'str',
        'group_id': 'str',
        'image_id': 'str',
        'sha_sum': 'str',
        'size': 'int',
        'registry': 'str',
        'config_id': 'str',
        'policy_id': 'str',
        'status': 'int',
        'status_msg': 'str',
        'date_created': 'str',
        'date_updated': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'user_id': 'UserID',
        'group_id': 'GroupID',
        'image_id': 'ImageId',
        'sha_sum': 'SHASum',
        'size': 'Size',
        'registry': 'Registry',
        'config_id': 'ConfigID',
        'policy_id': 'PolicyId',
        'status': 'Status',
        'status_msg': 'StatusMsg',
        'date_created': 'DateCreated',
        'date_updated': 'DateUpdated'
    }

    def __init__(self, id=None, name=None, description=None, user_id=None, group_id=None, image_id=None, sha_sum=None, size=None, registry=None, config_id=None, policy_id=None, status=None, status_msg=None, date_created=None, date_updated=None):
        """
        Image - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._user_id = None
        self._group_id = None
        self._image_id = None
        self._sha_sum = None
        self._size = None
        self._registry = None
        self._config_id = None
        self._policy_id = None
        self._status = None
        self._status_msg = None
        self._date_created = None
        self._date_updated = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if user_id is not None:
          self.user_id = user_id
        if group_id is not None:
          self.group_id = group_id
        if image_id is not None:
          self.image_id = image_id
        if sha_sum is not None:
          self.sha_sum = sha_sum
        if size is not None:
          self.size = size
        if registry is not None:
          self.registry = registry
        if config_id is not None:
          self.config_id = config_id
        if policy_id is not None:
          self.policy_id = policy_id
        if status is not None:
          self.status = status
        if status_msg is not None:
          self.status_msg = status_msg
        if date_created is not None:
          self.date_created = date_created
        if date_updated is not None:
          self.date_updated = date_updated

    @property
    def id(self):
        """
        Gets the id of this Image.
        12 character internal hexadecimal identifier for this image

        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Image.
        12 character internal hexadecimal identifier for this image

        :param id: The id of this Image.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Image.
        Image name

        :return: The name of this Image.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Image.
        Image name

        :param name: The name of this Image.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Image.
        Description for this image

        :return: The description of this Image.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Image.
        Description for this image

        :param description: The description of this Image.
        :type: str
        """

        self._description = description

    @property
    def user_id(self):
        """
        Gets the user_id of this Image.
        User ID of owner of the image

        :return: The user_id of this Image.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Image.
        User ID of owner of the image

        :param user_id: The user_id of this Image.
        :type: str
        """

        self._user_id = user_id

    @property
    def group_id(self):
        """
        Gets the group_id of this Image.
        Group ID of owner of the image

        :return: The group_id of this Image.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this Image.
        Group ID of owner of the image

        :param group_id: The group_id of this Image.
        :type: str
        """

        self._group_id = group_id

    @property
    def image_id(self):
        """
        Gets the image_id of this Image.
        Docker image ID

        :return: The image_id of this Image.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this Image.
        Docker image ID

        :param image_id: The image_id of this Image.
        :type: str
        """

        self._image_id = image_id

    @property
    def sha_sum(self):
        """
        Gets the sha_sum of this Image.
        SHA256 hash value for this image

        :return: The sha_sum of this Image.
        :rtype: str
        """
        return self._sha_sum

    @sha_sum.setter
    def sha_sum(self, sha_sum):
        """
        Sets the sha_sum of this Image.
        SHA256 hash value for this image

        :param sha_sum: The sha_sum of this Image.
        :type: str
        """

        self._sha_sum = sha_sum

    @property
    def size(self):
        """
        Gets the size of this Image.
        Size of the image, in bytes

        :return: The size of this Image.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this Image.
        Size of the image, in bytes

        :param size: The size of this Image.
        :type: int
        """

        self._size = size

    @property
    def registry(self):
        """
        Gets the registry of this Image.
        12 character hexadecimal internal identifier to layered insight record defining the registry this image is stored in

        :return: The registry of this Image.
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """
        Sets the registry of this Image.
        12 character hexadecimal internal identifier to layered insight record defining the registry this image is stored in

        :param registry: The registry of this Image.
        :type: str
        """

        self._registry = registry

    @property
    def config_id(self):
        """
        Gets the config_id of this Image.
        12 character hexadecimal internal identifier for Runtime configuration for this Container

        :return: The config_id of this Image.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """
        Sets the config_id of this Image.
        12 character hexadecimal internal identifier for Runtime configuration for this Container

        :param config_id: The config_id of this Image.
        :type: str
        """

        self._config_id = config_id

    @property
    def policy_id(self):
        """
        Gets the policy_id of this Image.
        12 character hexadecimal internal identifier for security policy for this Container

        :return: The policy_id of this Image.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this Image.
        12 character hexadecimal internal identifier for security policy for this Container

        :param policy_id: The policy_id of this Image.
        :type: str
        """

        self._policy_id = policy_id

    @property
    def status(self):
        """
        Gets the status of this Image.
        Value representing the current status of working with the image: 0: Added to system, but not yet analyzed 1: Processing - preparing for download 2: Downloading for analysis and instrumentation 3: There was an error during download, analysis, or instrumentation of the image 4: Instrumented image; Needs to be run to gather behavioral data 5: Instrumented and ready for use

        :return: The status of this Image.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Image.
        Value representing the current status of working with the image: 0: Added to system, but not yet analyzed 1: Processing - preparing for download 2: Downloading for analysis and instrumentation 3: There was an error during download, analysis, or instrumentation of the image 4: Instrumented image; Needs to be run to gather behavioral data 5: Instrumented and ready for use

        :param status: The status of this Image.
        :type: int
        """

        self._status = status

    @property
    def status_msg(self):
        """
        Gets the status_msg of this Image.
        Stores details about status of image, if any

        :return: The status_msg of this Image.
        :rtype: str
        """
        return self._status_msg

    @status_msg.setter
    def status_msg(self, status_msg):
        """
        Sets the status_msg of this Image.
        Stores details about status of image, if any

        :param status_msg: The status_msg of this Image.
        :type: str
        """

        self._status_msg = status_msg

    @property
    def date_created(self):
        """
        Gets the date_created of this Image.
        Timestamp for when object was created

        :return: The date_created of this Image.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Image.
        Timestamp for when object was created

        :param date_created: The date_created of this Image.
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """
        Gets the date_updated of this Image.
        Timestamp for when object was last updated

        :return: The date_updated of this Image.
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """
        Sets the date_updated of this Image.
        Timestamp for when object was last updated

        :param date_updated: The date_updated of this Image.
        :type: str
        """

        self._date_updated = date_updated

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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
