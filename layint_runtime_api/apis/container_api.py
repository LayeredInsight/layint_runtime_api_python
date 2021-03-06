# coding: utf-8

"""
    Layered Witness & Control

    LI Witness provides deep insight and analytics into containerized applications. Control provides dynamic runtime security and analytics for containerized applications. You can find out more about the Layered Insight Suite at [http://layeredinsight.com](http://layeredinsight.com).

    OpenAPI spec version: 0.9.7
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ContainerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def build_container_dossier_tempate(self, container_id, **kwargs):
        """
        Builds a security policy based on containers behavior
        This call builds a new custom security policy based on the recorded activities of the container.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.build_container_dossier_tempate(container_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str container_id: hexadecimal ID of container to gather dossier for (required)
        :param str merge_policy_id: hexadecimal ID of policy to merge gathered dossier rules
        :param str log_action: action string to match action type in log for gathered dossier rules
        :return: DossierTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.build_container_dossier_tempate_with_http_info(container_id, **kwargs)
        else:
            (data) = self.build_container_dossier_tempate_with_http_info(container_id, **kwargs)
            return data

    def build_container_dossier_tempate_with_http_info(self, container_id, **kwargs):
        """
        Builds a security policy based on containers behavior
        This call builds a new custom security policy based on the recorded activities of the container.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.build_container_dossier_tempate_with_http_info(container_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str container_id: hexadecimal ID of container to gather dossier for (required)
        :param str merge_policy_id: hexadecimal ID of policy to merge gathered dossier rules
        :param str log_action: action string to match action type in log for gathered dossier rules
        :return: DossierTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'merge_policy_id', 'log_action']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method build_container_dossier_tempate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params) or (params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `build_container_dossier_tempate`")


        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['containerID'] = params['container_id']

        query_params = []
        if 'merge_policy_id' in params:
            query_params.append(('mergePolicyID', params['merge_policy_id']))
        if 'log_action' in params:
            query_params.append(('logAction', params['log_action']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Containers/{containerID}/DossierTemplate', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DossierTemplateResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_container(self, container_id, **kwargs):
        """
        Delete a container
        Delete a container
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_container(container_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str container_id: hexadecimal ID of container to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_container_with_http_info(container_id, **kwargs)
        else:
            (data) = self.delete_container_with_http_info(container_id, **kwargs)
            return data

    def delete_container_with_http_info(self, container_id, **kwargs):
        """
        Delete a container
        Delete a container
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_container_with_http_info(container_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str container_id: hexadecimal ID of container to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_container" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params) or (params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `delete_container`")


        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['containerID'] = params['container_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Containers/{containerID}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_container_dossier(self, container_id, **kwargs):
        """
        Gets dossier for container
        This call produces a list of all data Witness has learend about the container
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_container_dossier(container_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str container_id: hexadecimal ID of container to gather dossier for (required)
        :return: Dossier
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_container_dossier_with_http_info(container_id, **kwargs)
        else:
            (data) = self.get_container_dossier_with_http_info(container_id, **kwargs)
            return data

    def get_container_dossier_with_http_info(self, container_id, **kwargs):
        """
        Gets dossier for container
        This call produces a list of all data Witness has learend about the container
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_container_dossier_with_http_info(container_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str container_id: hexadecimal ID of container to gather dossier for (required)
        :return: Dossier
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_container_dossier" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params) or (params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `get_container_dossier`")


        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['containerID'] = params['container_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Containers/{containerID}/Dossier', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Dossier',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_container_logs(self, container_id, **kwargs):
        """
        Gets behavioral logs for container
        This call produces a list of all behavior logs Witness has received for the container
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_container_logs(container_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str container_id: hexadecimal ID of container to gather logs for (required)
        :param int page_size: Maximum number of log records to return per \"page\" (think pager in a browser)
        :param int page: Page number of results to return. Results will start with record number (Page * PageSize)
        :return: ContainerLogs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_container_logs_with_http_info(container_id, **kwargs)
        else:
            (data) = self.get_container_logs_with_http_info(container_id, **kwargs)
            return data

    def get_container_logs_with_http_info(self, container_id, **kwargs):
        """
        Gets behavioral logs for container
        This call produces a list of all behavior logs Witness has received for the container
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_container_logs_with_http_info(container_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str container_id: hexadecimal ID of container to gather logs for (required)
        :param int page_size: Maximum number of log records to return per \"page\" (think pager in a browser)
        :param int page: Page number of results to return. Results will start with record number (Page * PageSize)
        :return: ContainerLogs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'page_size', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_container_logs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params) or (params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `get_container_logs`")


        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['containerID'] = params['container_id']

        query_params = []
        if 'page_size' in params:
            query_params.append(('PageSize', params['page_size']))
        if 'page' in params:
            query_params.append(('Page', params['page']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Containers/{containerID}/GetContainerLogs', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ContainerLogs',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_containers(self, **kwargs):
        """
        Get containers
        Returns a list of containers that are accessible to this user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_containers(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Containers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_containers_with_http_info(**kwargs)
        else:
            (data) = self.get_containers_with_http_info(**kwargs)
            return data

    def get_containers_with_http_info(self, **kwargs):
        """
        Get containers
        Returns a list of containers that are accessible to this user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_containers_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Containers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_containers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Containers', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Containers',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def toggle_container_sniffer(self, container_id, **kwargs):
        """
        Toggles network sniffer
        Toggles network sniffer on/off for specified container. This call doesn't take any parameters beside the container ID - each call of the API toggles the sniffer setting between enabled and disabled. Sniffer in a running container will change status within 30 seconds of this API call.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.toggle_container_sniffer(container_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str container_id: hexadecimal ID of registry to return (required)
        :return: Container
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.toggle_container_sniffer_with_http_info(container_id, **kwargs)
        else:
            (data) = self.toggle_container_sniffer_with_http_info(container_id, **kwargs)
            return data

    def toggle_container_sniffer_with_http_info(self, container_id, **kwargs):
        """
        Toggles network sniffer
        Toggles network sniffer on/off for specified container. This call doesn't take any parameters beside the container ID - each call of the API toggles the sniffer setting between enabled and disabled. Sniffer in a running container will change status within 30 seconds of this API call.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.toggle_container_sniffer_with_http_info(container_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str container_id: hexadecimal ID of registry to return (required)
        :return: Container
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method toggle_container_sniffer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params) or (params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `toggle_container_sniffer`")


        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['containerID'] = params['container_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Containers/{containerID}/ToggleSniffer', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Container',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
