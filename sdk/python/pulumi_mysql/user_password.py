# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['UserPassword']


class UserPassword(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The `UserPassword` resource sets and manages a password for a given
        user on a MySQL server.

        > **NOTE on MySQL Passwords:** This resource conflicts with the `password`
           argument for `User`. This resource uses PGP encryption to avoid
           storing unencrypted passwords in the provider state.

        > **NOTE on How Passwords are Created:** This resource **automatically**
           generates a **random** password. The password will be a random UUID.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] host: The source host of the user. Defaults to `localhost`.
        :param pulumi.Input[str] pgp_key: Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
        :param pulumi.Input[str] user: The IAM user to associate with this access key.
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

            __props__['host'] = host
            if pgp_key is None:
                raise TypeError("Missing required property 'pgp_key'")
            __props__['pgp_key'] = pgp_key
            if user is None:
                raise TypeError("Missing required property 'user'")
            __props__['user'] = user
            __props__['encrypted_password'] = None
            __props__['key_fingerprint'] = None
        super(UserPassword, __self__).__init__(
            'mysql:index/userPassword:UserPassword',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            encrypted_password: Optional[pulumi.Input[str]] = None,
            host: Optional[pulumi.Input[str]] = None,
            key_fingerprint: Optional[pulumi.Input[str]] = None,
            pgp_key: Optional[pulumi.Input[str]] = None,
            user: Optional[pulumi.Input[str]] = None) -> 'UserPassword':
        """
        Get an existing UserPassword resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] encrypted_password: The encrypted password, base64 encoded.
        :param pulumi.Input[str] host: The source host of the user. Defaults to `localhost`.
        :param pulumi.Input[str] key_fingerprint: The fingerprint of the PGP key used to encrypt the password
        :param pulumi.Input[str] pgp_key: Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
        :param pulumi.Input[str] user: The IAM user to associate with this access key.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["encrypted_password"] = encrypted_password
        __props__["host"] = host
        __props__["key_fingerprint"] = key_fingerprint
        __props__["pgp_key"] = pgp_key
        __props__["user"] = user
        return UserPassword(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="encryptedPassword")
    def encrypted_password(self) -> pulumi.Output[str]:
        """
        The encrypted password, base64 encoded.
        """
        return pulumi.get(self, "encrypted_password")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[Optional[str]]:
        """
        The source host of the user. Defaults to `localhost`.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> pulumi.Output[str]:
        """
        The fingerprint of the PGP key used to encrypt the password
        """
        return pulumi.get(self, "key_fingerprint")

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> pulumi.Output[str]:
        """
        Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
        """
        return pulumi.get(self, "pgp_key")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[str]:
        """
        The IAM user to associate with this access key.
        """
        return pulumi.get(self, "user")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

