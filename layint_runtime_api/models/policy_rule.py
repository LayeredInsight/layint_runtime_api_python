# coding: utf-8

"""
    Layered Control

    LI Control provides dynamic runtime security and analytics for containerized applications. You can find out more about the Layered Insight Suite at [http://layeredinsight.com](http://layeredinsight.com).

    OpenAPI spec version: 0.9.3
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PolicyRule(object):
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
        'name': 'str',
        'in_active': 'bool',
        'rule_type': 'str',
        'program': 'str',
        'listening_port': 'int',
        'listening_addr': 'str',
        'protocol': 'str',
        'remote_port': 'int',
        'syscall': 'int',
        'arg1': 'str',
        'arg2': 'str',
        'arg3': 'str',
        'file': 'str',
        'action': 'str',
        'date_created': 'str',
        'date_updated': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'in_active': 'InActive',
        'rule_type': 'RuleType',
        'program': 'Program',
        'listening_port': 'ListeningPort',
        'listening_addr': 'ListeningAddr',
        'protocol': 'Protocol',
        'remote_port': 'RemotePort',
        'syscall': 'Syscall',
        'arg1': 'Arg1',
        'arg2': 'Arg2',
        'arg3': 'Arg3',
        'file': 'File',
        'action': 'Action',
        'date_created': 'DateCreated',
        'date_updated': 'DateUpdated'
    }

    def __init__(self, name=None, in_active=False, rule_type=None, program='*', listening_port=None, listening_addr=None, protocol=None, remote_port=None, syscall=None, arg1=None, arg2=None, arg3=None, file=None, action=None, date_created=None, date_updated=None):
        """
        PolicyRule - a model defined in Swagger
        """

        self._name = None
        self._in_active = None
        self._rule_type = None
        self._program = None
        self._listening_port = None
        self._listening_addr = None
        self._protocol = None
        self._remote_port = None
        self._syscall = None
        self._arg1 = None
        self._arg2 = None
        self._arg3 = None
        self._file = None
        self._action = None
        self._date_created = None
        self._date_updated = None

        if name is not None:
          self.name = name
        if in_active is not None:
          self.in_active = in_active
        if rule_type is not None:
          self.rule_type = rule_type
        if program is not None:
          self.program = program
        if listening_port is not None:
          self.listening_port = listening_port
        if listening_addr is not None:
          self.listening_addr = listening_addr
        if protocol is not None:
          self.protocol = protocol
        if remote_port is not None:
          self.remote_port = remote_port
        if syscall is not None:
          self.syscall = syscall
        if arg1 is not None:
          self.arg1 = arg1
        if arg2 is not None:
          self.arg2 = arg2
        if arg3 is not None:
          self.arg3 = arg3
        if file is not None:
          self.file = file
        if action is not None:
          self.action = action
        if date_created is not None:
          self.date_created = date_created
        if date_updated is not None:
          self.date_updated = date_updated

    @property
    def name(self):
        """
        Gets the name of this PolicyRule.
        Name to refer to rule with and display

        :return: The name of this PolicyRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyRule.
        Name to refer to rule with and display

        :param name: The name of this PolicyRule.
        :type: str
        """

        self._name = name

    @property
    def in_active(self):
        """
        Gets the in_active of this PolicyRule.
        Allows the enabling/disabling of this rule

        :return: The in_active of this PolicyRule.
        :rtype: bool
        """
        return self._in_active

    @in_active.setter
    def in_active(self, in_active):
        """
        Sets the in_active of this PolicyRule.
        Allows the enabling/disabling of this rule

        :param in_active: The in_active of this PolicyRule.
        :type: bool
        """

        self._in_active = in_active

    @property
    def rule_type(self):
        """
        Gets the rule_type of this PolicyRule.
        Specifies the type of rule this is

        :return: The rule_type of this PolicyRule.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """
        Sets the rule_type of this PolicyRule.
        Specifies the type of rule this is

        :param rule_type: The rule_type of this PolicyRule.
        :type: str
        """
        allowed_values = ["execution", "Execution", "file", "File", "listener", "Listener", "java", "Java", "network", "Network", "syscall", "Syscall", "syscallgroup", "Syscallgroup"]
        if rule_type not in allowed_values:
            raise ValueError(
                "Invalid value for `rule_type` ({0}), must be one of {1}"
                .format(rule_type, allowed_values)
            )

        self._rule_type = rule_type

    @property
    def program(self):
        """
        Gets the program of this PolicyRule.
        Specifies path to program that this rule applies to. Wildcards are allowed.

        :return: The program of this PolicyRule.
        :rtype: str
        """
        return self._program

    @program.setter
    def program(self, program):
        """
        Sets the program of this PolicyRule.
        Specifies path to program that this rule applies to. Wildcards are allowed.

        :param program: The program of this PolicyRule.
        :type: str
        """

        self._program = program

    @property
    def listening_port(self):
        """
        Gets the listening_port of this PolicyRule.
        Local network port number this this rule applies to. Used only by network and listener rules.

        :return: The listening_port of this PolicyRule.
        :rtype: int
        """
        return self._listening_port

    @listening_port.setter
    def listening_port(self, listening_port):
        """
        Sets the listening_port of this PolicyRule.
        Local network port number this this rule applies to. Used only by network and listener rules.

        :param listening_port: The listening_port of this PolicyRule.
        :type: int
        """

        self._listening_port = listening_port

    @property
    def listening_addr(self):
        """
        Gets the listening_addr of this PolicyRule.
        Local IP address this rule applies to. Used only by network rules.

        :return: The listening_addr of this PolicyRule.
        :rtype: str
        """
        return self._listening_addr

    @listening_addr.setter
    def listening_addr(self, listening_addr):
        """
        Sets the listening_addr of this PolicyRule.
        Local IP address this rule applies to. Used only by network rules.

        :param listening_addr: The listening_addr of this PolicyRule.
        :type: str
        """

        self._listening_addr = listening_addr

    @property
    def protocol(self):
        """
        Gets the protocol of this PolicyRule.
        Network protocol that this rule applies to. Used only by network rules.

        :return: The protocol of this PolicyRule.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this PolicyRule.
        Network protocol that this rule applies to. Used only by network rules.

        :param protocol: The protocol of this PolicyRule.
        :type: str
        """

        self._protocol = protocol

    @property
    def remote_port(self):
        """
        Gets the remote_port of this PolicyRule.
        Remote network port number this this rule applies to. Used only by network rules.

        :return: The remote_port of this PolicyRule.
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        """
        Sets the remote_port of this PolicyRule.
        Remote network port number this this rule applies to. Used only by network rules.

        :param remote_port: The remote_port of this PolicyRule.
        :type: int
        """

        self._remote_port = remote_port

    @property
    def syscall(self):
        """
        Gets the syscall of this PolicyRule.
        System call number, for rules where an individual system call is to be blocked. Used only in syscall rules.

        :return: The syscall of this PolicyRule.
        :rtype: int
        """
        return self._syscall

    @syscall.setter
    def syscall(self, syscall):
        """
        Sets the syscall of this PolicyRule.
        System call number, for rules where an individual system call is to be blocked. Used only in syscall rules.

        :param syscall: The syscall of this PolicyRule.
        :type: int
        """

        self._syscall = syscall

    @property
    def arg1(self):
        """
        Gets the arg1 of this PolicyRule.
        Variable argument, usage differs depending on rule type.

        :return: The arg1 of this PolicyRule.
        :rtype: str
        """
        return self._arg1

    @arg1.setter
    def arg1(self, arg1):
        """
        Sets the arg1 of this PolicyRule.
        Variable argument, usage differs depending on rule type.

        :param arg1: The arg1 of this PolicyRule.
        :type: str
        """

        self._arg1 = arg1

    @property
    def arg2(self):
        """
        Gets the arg2 of this PolicyRule.
        Variable argument, usage differs depending on rule type.

        :return: The arg2 of this PolicyRule.
        :rtype: str
        """
        return self._arg2

    @arg2.setter
    def arg2(self, arg2):
        """
        Sets the arg2 of this PolicyRule.
        Variable argument, usage differs depending on rule type.

        :param arg2: The arg2 of this PolicyRule.
        :type: str
        """

        self._arg2 = arg2

    @property
    def arg3(self):
        """
        Gets the arg3 of this PolicyRule.
        Variable argument, usage differs depending on rule type.

        :return: The arg3 of this PolicyRule.
        :rtype: str
        """
        return self._arg3

    @arg3.setter
    def arg3(self, arg3):
        """
        Sets the arg3 of this PolicyRule.
        Variable argument, usage differs depending on rule type.

        :param arg3: The arg3 of this PolicyRule.
        :type: str
        """

        self._arg3 = arg3

    @property
    def file(self):
        """
        Gets the file of this PolicyRule.
        Path to file that rule applies to

        :return: The file of this PolicyRule.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """
        Sets the file of this PolicyRule.
        Path to file that rule applies to

        :param file: The file of this PolicyRule.
        :type: str
        """

        self._file = file

    @property
    def action(self):
        """
        Gets the action of this PolicyRule.
        Action that should be taken if this rule is matched

        :return: The action of this PolicyRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this PolicyRule.
        Action that should be taken if this rule is matched

        :param action: The action of this PolicyRule.
        :type: str
        """
        allowed_values = ["allow", "deny", "readonly", "readwrite"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def date_created(self):
        """
        Gets the date_created of this PolicyRule.
        Timestamp for when object was created

        :return: The date_created of this PolicyRule.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this PolicyRule.
        Timestamp for when object was created

        :param date_created: The date_created of this PolicyRule.
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """
        Gets the date_updated of this PolicyRule.
        Timestamp for when object was last updated

        :return: The date_updated of this PolicyRule.
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """
        Sets the date_updated of this PolicyRule.
        Timestamp for when object was last updated

        :param date_updated: The date_updated of this PolicyRule.
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
        if not isinstance(other, PolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
