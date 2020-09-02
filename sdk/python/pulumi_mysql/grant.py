# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = ['Grant']


class Grant(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 grant: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 tls_option: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The ``Grant`` resource creates and manages privileges given to
        a user on a MySQL server.

        ## Examples

        ### Granting Privileges to a User

        ```python
        import pulumi
        import pulumi_mysql as mysql

        jdoe_user = mysql.User("jdoeUser",
            host="example.com",
            plaintext_password="password",
            user="jdoe")
        jdoe_grant = mysql.Grant("jdoeGrant",
            database="app",
            host=jdoe_user.host,
            privileges=[
                "SELECT",
                "UPDATE",
            ],
            user=jdoe_user.user)
        ```

        ### Granting Privileges to a Role

        ```python
        import pulumi
        import pulumi_mysql as mysql

        developer_role = mysql.Role("developerRole")
        developer_grant = mysql.Grant("developerGrant",
            database="app",
            privileges=[
                "SELECT",
                "UPDATE",
            ],
            role=developer_role.name)
        ```

        ### Adding a Role to a User

        ```python
        import pulumi
        import pulumi_mysql as mysql

        jdoe = mysql.User("jdoe",
            host="example.com",
            plaintext_password="password",
            user="jdoe")
        developer_role = mysql.Role("developerRole")
        developer_grant = mysql.Grant("developerGrant",
            database="app",
            host=jdoe.host,
            roles=[developer_role.name],
            user=jdoe.user)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database: The database to grant privileges on.
        :param pulumi.Input[bool] grant: Whether to also give the user privileges to grant the same privileges to other users.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost". Conflicts with `role`.
        :param pulumi.Input[List[pulumi.Input[str]]] privileges: A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        :param pulumi.Input[str] role: The role to grant `privileges` to. Conflicts with `user` and `host`.
        :param pulumi.Input[List[pulumi.Input[str]]] roles: A list of rols to grant to the user. Conflicts with `privileges`.
        :param pulumi.Input[str] table: Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        :param pulumi.Input[str] user: The name of the user. Conflicts with `role`.
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if database is None:
                raise TypeError("Missing required property 'database'")
            __props__['database'] = database
            __props__['grant'] = grant
            __props__['host'] = host
            __props__['privileges'] = privileges
            __props__['role'] = role
            __props__['roles'] = roles
            __props__['table'] = table
            __props__['tls_option'] = tls_option
            __props__['user'] = user
        super(Grant, __self__).__init__(
            'mysql:index/grant:Grant',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            database: Optional[pulumi.Input[str]] = None,
            grant: Optional[pulumi.Input[bool]] = None,
            host: Optional[pulumi.Input[str]] = None,
            privileges: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            role: Optional[pulumi.Input[str]] = None,
            roles: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            table: Optional[pulumi.Input[str]] = None,
            tls_option: Optional[pulumi.Input[str]] = None,
            user: Optional[pulumi.Input[str]] = None) -> 'Grant':
        """
        Get an existing Grant resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database: The database to grant privileges on.
        :param pulumi.Input[bool] grant: Whether to also give the user privileges to grant the same privileges to other users.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost". Conflicts with `role`.
        :param pulumi.Input[List[pulumi.Input[str]]] privileges: A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        :param pulumi.Input[str] role: The role to grant `privileges` to. Conflicts with `user` and `host`.
        :param pulumi.Input[List[pulumi.Input[str]]] roles: A list of rols to grant to the user. Conflicts with `privileges`.
        :param pulumi.Input[str] table: Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        :param pulumi.Input[str] user: The name of the user. Conflicts with `role`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["database"] = database
        __props__["grant"] = grant
        __props__["host"] = host
        __props__["privileges"] = privileges
        __props__["role"] = role
        __props__["roles"] = roles
        __props__["table"] = table
        __props__["tls_option"] = tls_option
        __props__["user"] = user
        return Grant(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[str]:
        """
        The database to grant privileges on.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter
    def grant(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to also give the user privileges to grant the same privileges to other users.
        """
        return pulumi.get(self, "grant")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[Optional[str]]:
        """
        The source host of the user. Defaults to "localhost". Conflicts with `role`.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def privileges(self) -> pulumi.Output[Optional[List[str]]]:
        """
        A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        """
        return pulumi.get(self, "privileges")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[str]]:
        """
        The role to grant `privileges` to. Conflicts with `user` and `host`.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Optional[List[str]]]:
        """
        A list of rols to grant to the user. Conflicts with `privileges`.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def table(self) -> pulumi.Output[Optional[str]]:
        """
        Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        """
        return pulumi.get(self, "table")

    @property
    @pulumi.getter(name="tlsOption")
    def tls_option(self) -> pulumi.Output[Optional[str]]:
        """
        An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        """
        return pulumi.get(self, "tls_option")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the user. Conflicts with `role`.
        """
        return pulumi.get(self, "user")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

