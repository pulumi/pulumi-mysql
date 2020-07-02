# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables


class User(pulumi.CustomResource):
    auth_plugin: pulumi.Output[str]
    """
    Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
    """
    host: pulumi.Output[str]
    """
    The source host of the user. Defaults to "localhost".
    """
    password: pulumi.Output[str]
    """
    Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
    """
    plaintext_password: pulumi.Output[str]
    """
    The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
    """
    tls_option: pulumi.Output[str]
    """
    An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
    """
    user: pulumi.Output[str]
    """
    The name of the user.
    """
    def __init__(__self__, resource_name, opts=None, auth_plugin=None, host=None, password=None, plaintext_password=None, tls_option=None, user=None, __props__=None, __name__=None, __opts__=None):
        """
        The ``User`` resource creates and manages a user on a MySQL
        server.

        > **Note:** The password for the user is provided in plain text, and is
        obscured by an unsalted hash in the state
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
        Care is required when using this resource, to avoid disclosing the password.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_mysql as mysql

        jdoe = mysql.User("jdoe",
            host="example.com",
            plaintext_password="password",
            user="jdoe")
        ```
        ### With An Authentication Plugin

        ```python
        import pulumi
        import pulumi_mysql as mysql

        nologin = mysql.User("nologin",
            auth_plugin="mysql_no_login",
            host="example.com",
            user="nologin")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_plugin: Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost".
        :param pulumi.Input[str] password: Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] plaintext_password: The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
        :param pulumi.Input[str] user: The name of the user.
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

            __props__['auth_plugin'] = auth_plugin
            __props__['host'] = host
            if password is not None:
                warnings.warn("Please use plaintext_password instead", DeprecationWarning)
                pulumi.log.warn("password is deprecated: Please use plaintext_password instead")
            __props__['password'] = password
            __props__['plaintext_password'] = plaintext_password
            __props__['tls_option'] = tls_option
            if user is None:
                raise TypeError("Missing required property 'user'")
            __props__['user'] = user
        super(User, __self__).__init__(
            'mysql:index/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, auth_plugin=None, host=None, password=None, plaintext_password=None, tls_option=None, user=None):
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_plugin: Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost".
        :param pulumi.Input[str] password: Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] plaintext_password: The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
        :param pulumi.Input[str] user: The name of the user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auth_plugin"] = auth_plugin
        __props__["host"] = host
        __props__["password"] = password
        __props__["plaintext_password"] = plaintext_password
        __props__["tls_option"] = tls_option
        __props__["user"] = user
        return User(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
