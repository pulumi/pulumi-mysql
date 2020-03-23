# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Provider(pulumi.ProviderResource):
    def __init__(__self__, resource_name, opts=None, authentication_plugin=None, endpoint=None, max_conn_lifetime_sec=None, max_open_conns=None, password=None, proxy=None, tls=None, username=None, __props__=None, __name__=None, __opts__=None):
        """
        The provider type for the mysql package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/index.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['authentication_plugin'] = authentication_plugin
            if endpoint is None:
                endpoint = utilities.get_env('MYSQL_ENDPOINT')
            __props__['endpoint'] = endpoint
            __props__['max_conn_lifetime_sec'] = pulumi.Output.from_input(max_conn_lifetime_sec).apply(json.dumps) if max_conn_lifetime_sec is not None else None
            __props__['max_open_conns'] = pulumi.Output.from_input(max_open_conns).apply(json.dumps) if max_open_conns is not None else None
            if password is None:
                password = utilities.get_env('MYSQL_PASSWORD')
            __props__['password'] = password
            if proxy is None:
                proxy = utilities.get_env('ALL_PROXY', 'all_proxy')
            __props__['proxy'] = proxy
            if tls is None:
                tls = (utilities.get_env('MYSQL_TLS_CONFIG') or 'false')
            __props__['tls'] = tls
            if username is None:
                username = utilities.get_env('MYSQL_USERNAME')
            __props__['username'] = username
        super(Provider, __self__).__init__(
            'mysql',
            resource_name,
            __props__,
            opts)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

