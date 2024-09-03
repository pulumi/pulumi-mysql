# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['GrantArgs', 'Grant']

@pulumi.input_type
class GrantArgs:
    def __init__(__self__, *,
                 database: pulumi.Input[str],
                 grant: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 tls_option: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Grant resource.
        :param pulumi.Input[str] database: The database to grant privileges on.
        :param pulumi.Input[bool] grant: Whether to also give the user privileges to grant the same privileges to other users.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost". Conflicts with `role`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        :param pulumi.Input[str] role: The role to grant `privileges` to. Conflicts with `user` and `host`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of rols to grant to the user. Conflicts with `privileges`.
        :param pulumi.Input[str] table: Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        :param pulumi.Input[str] user: The name of the user. Conflicts with `role`.
        """
        pulumi.set(__self__, "database", database)
        if grant is not None:
            pulumi.set(__self__, "grant", grant)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if privileges is not None:
            pulumi.set(__self__, "privileges", privileges)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if table is not None:
            pulumi.set(__self__, "table", table)
        if tls_option is not None:
            pulumi.set(__self__, "tls_option", tls_option)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        """
        The database to grant privileges on.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def grant(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to also give the user privileges to grant the same privileges to other users.
        """
        return pulumi.get(self, "grant")

    @grant.setter
    def grant(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "grant", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        The source host of the user. Defaults to "localhost". Conflicts with `role`.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def privileges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        """
        return pulumi.get(self, "privileges")

    @privileges.setter
    def privileges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "privileges", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role to grant `privileges` to. Conflicts with `user` and `host`.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of rols to grant to the user. Conflicts with `privileges`.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[str]]:
        """
        Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        """
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table", value)

    @property
    @pulumi.getter(name="tlsOption")
    def tls_option(self) -> Optional[pulumi.Input[str]]:
        """
        An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        """
        return pulumi.get(self, "tls_option")

    @tls_option.setter
    def tls_option(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_option", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user. Conflicts with `role`.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


@pulumi.input_type
class _GrantState:
    def __init__(__self__, *,
                 database: Optional[pulumi.Input[str]] = None,
                 grant: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 tls_option: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Grant resources.
        :param pulumi.Input[str] database: The database to grant privileges on.
        :param pulumi.Input[bool] grant: Whether to also give the user privileges to grant the same privileges to other users.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost". Conflicts with `role`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        :param pulumi.Input[str] role: The role to grant `privileges` to. Conflicts with `user` and `host`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of rols to grant to the user. Conflicts with `privileges`.
        :param pulumi.Input[str] table: Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        :param pulumi.Input[str] user: The name of the user. Conflicts with `role`.
        """
        if database is not None:
            pulumi.set(__self__, "database", database)
        if grant is not None:
            pulumi.set(__self__, "grant", grant)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if privileges is not None:
            pulumi.set(__self__, "privileges", privileges)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if table is not None:
            pulumi.set(__self__, "table", table)
        if tls_option is not None:
            pulumi.set(__self__, "tls_option", tls_option)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        The database to grant privileges on.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def grant(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to also give the user privileges to grant the same privileges to other users.
        """
        return pulumi.get(self, "grant")

    @grant.setter
    def grant(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "grant", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        The source host of the user. Defaults to "localhost". Conflicts with `role`.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def privileges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        """
        return pulumi.get(self, "privileges")

    @privileges.setter
    def privileges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "privileges", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role to grant `privileges` to. Conflicts with `user` and `host`.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of rols to grant to the user. Conflicts with `privileges`.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[str]]:
        """
        Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        """
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table", value)

    @property
    @pulumi.getter(name="tlsOption")
    def tls_option(self) -> Optional[pulumi.Input[str]]:
        """
        An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        """
        return pulumi.get(self, "tls_option")

    @tls_option.setter
    def tls_option(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_option", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user. Conflicts with `role`.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


class Grant(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 grant: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 tls_option: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The `Grant` resource creates and manages privileges given to
        a user on a MySQL server.

        ## Examples

        ### Granting Privileges to a User

        ```python
        import pulumi
        import pulumi_mysql as mysql

        jdoe = mysql.User("jdoe",
            user="jdoe",
            host="example.com",
            plaintext_password="password")
        jdoe_grant = mysql.Grant("jdoe",
            user=jdoe.user,
            host=jdoe.host,
            database="app",
            privileges=[
                "SELECT",
                "UPDATE",
            ])
        ```

        ### Granting Privileges to a Role

        ```python
        import pulumi
        import pulumi_mysql as mysql

        developer = mysql.Role("developer", name="developer")
        developer_grant = mysql.Grant("developer",
            role=developer.name,
            database="app",
            privileges=[
                "SELECT",
                "UPDATE",
            ])
        ```

        ### Adding a Role to a User

        ```python
        import pulumi
        import pulumi_mysql as mysql

        jdoe = mysql.User("jdoe",
            user="jdoe",
            host="example.com",
            plaintext_password="password")
        developer = mysql.Role("developer", name="developer")
        developer_grant = mysql.Grant("developer",
            user=jdoe.user,
            host=jdoe.host,
            database="app",
            roles=[developer.name])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database: The database to grant privileges on.
        :param pulumi.Input[bool] grant: Whether to also give the user privileges to grant the same privileges to other users.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost". Conflicts with `role`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        :param pulumi.Input[str] role: The role to grant `privileges` to. Conflicts with `user` and `host`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of rols to grant to the user. Conflicts with `privileges`.
        :param pulumi.Input[str] table: Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        :param pulumi.Input[str] user: The name of the user. Conflicts with `role`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GrantArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `Grant` resource creates and manages privileges given to
        a user on a MySQL server.

        ## Examples

        ### Granting Privileges to a User

        ```python
        import pulumi
        import pulumi_mysql as mysql

        jdoe = mysql.User("jdoe",
            user="jdoe",
            host="example.com",
            plaintext_password="password")
        jdoe_grant = mysql.Grant("jdoe",
            user=jdoe.user,
            host=jdoe.host,
            database="app",
            privileges=[
                "SELECT",
                "UPDATE",
            ])
        ```

        ### Granting Privileges to a Role

        ```python
        import pulumi
        import pulumi_mysql as mysql

        developer = mysql.Role("developer", name="developer")
        developer_grant = mysql.Grant("developer",
            role=developer.name,
            database="app",
            privileges=[
                "SELECT",
                "UPDATE",
            ])
        ```

        ### Adding a Role to a User

        ```python
        import pulumi
        import pulumi_mysql as mysql

        jdoe = mysql.User("jdoe",
            user="jdoe",
            host="example.com",
            plaintext_password="password")
        developer = mysql.Role("developer", name="developer")
        developer_grant = mysql.Grant("developer",
            user=jdoe.user,
            host=jdoe.host,
            database="app",
            roles=[developer.name])
        ```

        :param str resource_name: The name of the resource.
        :param GrantArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GrantArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 grant: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 tls_option: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GrantArgs.__new__(GrantArgs)

            if database is None and not opts.urn:
                raise TypeError("Missing required property 'database'")
            __props__.__dict__["database"] = database
            __props__.__dict__["grant"] = grant
            __props__.__dict__["host"] = host
            __props__.__dict__["privileges"] = privileges
            __props__.__dict__["role"] = role
            __props__.__dict__["roles"] = roles
            __props__.__dict__["table"] = table
            __props__.__dict__["tls_option"] = tls_option
            __props__.__dict__["user"] = user
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
            privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            role: Optional[pulumi.Input[str]] = None,
            roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        :param pulumi.Input[str] role: The role to grant `privileges` to. Conflicts with `user` and `host`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of rols to grant to the user. Conflicts with `privileges`.
        :param pulumi.Input[str] table: Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        :param pulumi.Input[str] user: The name of the user. Conflicts with `role`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GrantState.__new__(_GrantState)

        __props__.__dict__["database"] = database
        __props__.__dict__["grant"] = grant
        __props__.__dict__["host"] = host
        __props__.__dict__["privileges"] = privileges
        __props__.__dict__["role"] = role
        __props__.__dict__["roles"] = roles
        __props__.__dict__["table"] = table
        __props__.__dict__["tls_option"] = tls_option
        __props__.__dict__["user"] = user
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
    def privileges(self) -> pulumi.Output[Optional[Sequence[str]]]:
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
    def roles(self) -> pulumi.Output[Optional[Sequence[str]]]:
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

