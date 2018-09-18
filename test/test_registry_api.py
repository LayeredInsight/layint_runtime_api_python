# coding: utf-8

"""
    Layered Witness & Control

    LI Witness provides deep insight and analytics into containerized applications. Control provides dynamic runtime security and analytics for containerized applications. You can find out more about the Layered Insight Suite at [http://layeredinsight.com](http://layeredinsight.com).

    OpenAPI spec version: 0.9.7
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import layint_runtime_api
from layint_runtime_api.rest import ApiException
from layint_runtime_api.apis.registry_api import RegistryApi


class TestRegistryApi(unittest.TestCase):
    """ RegistryApi unit test stubs """

    def setUp(self):
        self.api = layint_runtime_api.apis.registry_api.RegistryApi()

    def tearDown(self):
        pass

    def test_add_registry(self):
        """
        Test case for add_registry

        Create new registry definition
        """
        pass

    def test_delete_registry(self):
        """
        Test case for delete_registry

        Delete specified registry
        """
        pass

    def test_get_registries(self):
        """
        Test case for get_registries

        Get defined registries
        """
        pass

    def test_get_registry(self):
        """
        Test case for get_registry

        Get specified registry
        """
        pass

    def test_get_registry_by_name(self):
        """
        Test case for get_registry_by_name

        Get registry by name
        """
        pass

    def test_list_all_images_in_registry(self):
        """
        Test case for list_all_images_in_registry

        Get container images in registry
        """
        pass

    def test_update_registry(self):
        """
        Test case for update_registry

        Update specified registry
        """
        pass


if __name__ == '__main__':
    unittest.main()
