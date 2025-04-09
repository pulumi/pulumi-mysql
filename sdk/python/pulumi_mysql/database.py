# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = ['DatabaseArgs', 'Database']

@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *,
                 default_character_set: Optional[pulumi.Input[builtins.str]] = None,
                 default_collation: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a Database resource.
        :param pulumi.Input[builtins.str] default_character_set: The default character set to use when
               a table is created without specifying an explicit character set. Defaults
               to "utf8".
        :param pulumi.Input[builtins.str] default_collation: The default collation to use when a table
               is created without specifying an explicit collation. Defaults to
               ``utf8_general_ci``. Each character set has its own set of collations, so
               changing the character set requires also changing the collation.
               
               Note that the defaults for character set and collation above do not respect
               any defaults set on the MySQL server, so that the configuration can be set
               appropriately even though this provider cannot see the server-level defaults. If
               you wish to use the server's defaults you must consult the server's
               configuration and then set the ``default_character_set`` and
               ``default_collation`` to match.
        :param pulumi.Input[builtins.str] name: The name of the database. This must be unique within
               a given MySQL server and may or may not be case-sensitive depending on
               the operating system on which the MySQL server is running.
        """
        if default_character_set is not None:
            pulumi.set(__self__, "default_character_set", default_character_set)
        if default_collation is not None:
            pulumi.set(__self__, "default_collation", default_collation)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="defaultCharacterSet")
    def default_character_set(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The default character set to use when
        a table is created without specifying an explicit character set. Defaults
        to "utf8".
        """
        return pulumi.get(self, "default_character_set")

    @default_character_set.setter
    def default_character_set(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "default_character_set", value)

    @property
    @pulumi.getter(name="defaultCollation")
    def default_collation(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The default collation to use when a table
        is created without specifying an explicit collation. Defaults to
        ``utf8_general_ci``. Each character set has its own set of collations, so
        changing the character set requires also changing the collation.

        Note that the defaults for character set and collation above do not respect
        any defaults set on the MySQL server, so that the configuration can be set
        appropriately even though this provider cannot see the server-level defaults. If
        you wish to use the server's defaults you must consult the server's
        configuration and then set the ``default_character_set`` and
        ``default_collation`` to match.
        """
        return pulumi.get(self, "default_collation")

    @default_collation.setter
    def default_collation(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "default_collation", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the database. This must be unique within
        a given MySQL server and may or may not be case-sensitive depending on
        the operating system on which the MySQL server is running.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DatabaseState:
    def __init__(__self__, *,
                 default_character_set: Optional[pulumi.Input[builtins.str]] = None,
                 default_collation: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering Database resources.
        :param pulumi.Input[builtins.str] default_character_set: The default character set to use when
               a table is created without specifying an explicit character set. Defaults
               to "utf8".
        :param pulumi.Input[builtins.str] default_collation: The default collation to use when a table
               is created without specifying an explicit collation. Defaults to
               ``utf8_general_ci``. Each character set has its own set of collations, so
               changing the character set requires also changing the collation.
               
               Note that the defaults for character set and collation above do not respect
               any defaults set on the MySQL server, so that the configuration can be set
               appropriately even though this provider cannot see the server-level defaults. If
               you wish to use the server's defaults you must consult the server's
               configuration and then set the ``default_character_set`` and
               ``default_collation`` to match.
        :param pulumi.Input[builtins.str] name: The name of the database. This must be unique within
               a given MySQL server and may or may not be case-sensitive depending on
               the operating system on which the MySQL server is running.
        """
        if default_character_set is not None:
            pulumi.set(__self__, "default_character_set", default_character_set)
        if default_collation is not None:
            pulumi.set(__self__, "default_collation", default_collation)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="defaultCharacterSet")
    def default_character_set(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The default character set to use when
        a table is created without specifying an explicit character set. Defaults
        to "utf8".
        """
        return pulumi.get(self, "default_character_set")

    @default_character_set.setter
    def default_character_set(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "default_character_set", value)

    @property
    @pulumi.getter(name="defaultCollation")
    def default_collation(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The default collation to use when a table
        is created without specifying an explicit collation. Defaults to
        ``utf8_general_ci``. Each character set has its own set of collations, so
        changing the character set requires also changing the collation.

        Note that the defaults for character set and collation above do not respect
        any defaults set on the MySQL server, so that the configuration can be set
        appropriately even though this provider cannot see the server-level defaults. If
        you wish to use the server's defaults you must consult the server's
        configuration and then set the ``default_character_set`` and
        ``default_collation`` to match.
        """
        return pulumi.get(self, "default_collation")

    @default_collation.setter
    def default_collation(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "default_collation", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the database. This must be unique within
        a given MySQL server and may or may not be case-sensitive depending on
        the operating system on which the MySQL server is running.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_character_set: Optional[pulumi.Input[builtins.str]] = None,
                 default_collation: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        The ``Database`` resource creates and manages a database on a MySQL
        server.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_mysql as mysql

        app = mysql.Database("app", name="my_awesome_app")
        ```

        ## Import

        Databases can be imported using their name, e.g.

        ```sh
        $ pulumi import mysql:index/database:Database example my-example-database
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] default_character_set: The default character set to use when
               a table is created without specifying an explicit character set. Defaults
               to "utf8".
        :param pulumi.Input[builtins.str] default_collation: The default collation to use when a table
               is created without specifying an explicit collation. Defaults to
               ``utf8_general_ci``. Each character set has its own set of collations, so
               changing the character set requires also changing the collation.
               
               Note that the defaults for character set and collation above do not respect
               any defaults set on the MySQL server, so that the configuration can be set
               appropriately even though this provider cannot see the server-level defaults. If
               you wish to use the server's defaults you must consult the server's
               configuration and then set the ``default_character_set`` and
               ``default_collation`` to match.
        :param pulumi.Input[builtins.str] name: The name of the database. This must be unique within
               a given MySQL server and may or may not be case-sensitive depending on
               the operating system on which the MySQL server is running.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DatabaseArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``Database`` resource creates and manages a database on a MySQL
        server.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_mysql as mysql

        app = mysql.Database("app", name="my_awesome_app")
        ```

        ## Import

        Databases can be imported using their name, e.g.

        ```sh
        $ pulumi import mysql:index/database:Database example my-example-database
        ```

        :param str resource_name: The name of the resource.
        :param DatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_character_set: Optional[pulumi.Input[builtins.str]] = None,
                 default_collation: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatabaseArgs.__new__(DatabaseArgs)

            __props__.__dict__["default_character_set"] = default_character_set
            __props__.__dict__["default_collation"] = default_collation
            __props__.__dict__["name"] = name
        super(Database, __self__).__init__(
            'mysql:index/database:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_character_set: Optional[pulumi.Input[builtins.str]] = None,
            default_collation: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None) -> 'Database':
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] default_character_set: The default character set to use when
               a table is created without specifying an explicit character set. Defaults
               to "utf8".
        :param pulumi.Input[builtins.str] default_collation: The default collation to use when a table
               is created without specifying an explicit collation. Defaults to
               ``utf8_general_ci``. Each character set has its own set of collations, so
               changing the character set requires also changing the collation.
               
               Note that the defaults for character set and collation above do not respect
               any defaults set on the MySQL server, so that the configuration can be set
               appropriately even though this provider cannot see the server-level defaults. If
               you wish to use the server's defaults you must consult the server's
               configuration and then set the ``default_character_set`` and
               ``default_collation`` to match.
        :param pulumi.Input[builtins.str] name: The name of the database. This must be unique within
               a given MySQL server and may or may not be case-sensitive depending on
               the operating system on which the MySQL server is running.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatabaseState.__new__(_DatabaseState)

        __props__.__dict__["default_character_set"] = default_character_set
        __props__.__dict__["default_collation"] = default_collation
        __props__.__dict__["name"] = name
        return Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultCharacterSet")
    def default_character_set(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The default character set to use when
        a table is created without specifying an explicit character set. Defaults
        to "utf8".
        """
        return pulumi.get(self, "default_character_set")

    @property
    @pulumi.getter(name="defaultCollation")
    def default_collation(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The default collation to use when a table
        is created without specifying an explicit collation. Defaults to
        ``utf8_general_ci``. Each character set has its own set of collations, so
        changing the character set requires also changing the collation.

        Note that the defaults for character set and collation above do not respect
        any defaults set on the MySQL server, so that the configuration can be set
        appropriately even though this provider cannot see the server-level defaults. If
        you wish to use the server's defaults you must consult the server's
        configuration and then set the ``default_character_set`` and
        ``default_collation`` to match.
        """
        return pulumi.get(self, "default_collation")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the database. This must be unique within
        a given MySQL server and may or may not be case-sensitive depending on
        the operating system on which the MySQL server is running.
        """
        return pulumi.get(self, "name")

