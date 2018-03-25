# coding: utf-8

"""
    Layered Control

    LI Control provides dynamic runtime security and analytics for containerized applications. You can find out more about the Layered Insight Suite at [http://layeredinsight.com](http://layeredinsight.com).

    OpenAPI spec version: 0.9.4
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


class EventApi(object):
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

    def describe_event(self, event_id, **kwargs):
        """
        Gets description about specific event
        Describes an event in a manner that can be understood by humans.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.describe_event(event_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str event_id: hexadecimal ID of event to get description of (required)
        :return: AlertEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.describe_event_with_http_info(event_id, **kwargs)
        else:
            (data) = self.describe_event_with_http_info(event_id, **kwargs)
            return data

    def describe_event_with_http_info(self, event_id, **kwargs):
        """
        Gets description about specific event
        Describes an event in a manner that can be understood by humans.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.describe_event_with_http_info(event_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str event_id: hexadecimal ID of event to get description of (required)
        :return: AlertEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_id' is set
        if ('event_id' not in params) or (params['event_id'] is None):
            raise ValueError("Missing the required parameter `event_id` when calling `describe_event`")


        collection_formats = {}

        path_params = {}
        if 'event_id' in params:
            path_params['eventID'] = params['event_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Events/{eventID}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AlertEvents',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
