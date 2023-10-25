# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['UserPasswordArgs', 'UserPassword']

@pulumi.input_type
class UserPasswordArgs:
    def __init__(__self__, *,
                 pgp_key: pulumi.Input[str],
                 user: pulumi.Input[str],
                 host: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserPassword resource.
        :param pulumi.Input[str] pgp_key: Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
        :param pulumi.Input[str] user: The IAM user to associate with this access key.
        :param pulumi.Input[str] host: The source host of the user. Defaults to `localhost`.
        """
        UserPasswordArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            pgp_key=pgp_key,
            user=user,
            host=host,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             pgp_key: Optional[pulumi.Input[str]] = None,
             user: Optional[pulumi.Input[str]] = None,
             host: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if pgp_key is None and 'pgpKey' in kwargs:
            pgp_key = kwargs['pgpKey']
        if pgp_key is None:
            raise TypeError("Missing 'pgp_key' argument")
        if user is None:
            raise TypeError("Missing 'user' argument")

        _setter("pgp_key", pgp_key)
        _setter("user", user)
        if host is not None:
            _setter("host", host)

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> pulumi.Input[str]:
        """
        Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
        """
        return pulumi.get(self, "pgp_key")

    @pgp_key.setter
    def pgp_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "pgp_key", value)

    @property
    @pulumi.getter
    def user(self) -> pulumi.Input[str]:
        """
        The IAM user to associate with this access key.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: pulumi.Input[str]):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        The source host of the user. Defaults to `localhost`.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)


@pulumi.input_type
class _UserPasswordState:
    def __init__(__self__, *,
                 encrypted_password: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 key_fingerprint: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserPassword resources.
        :param pulumi.Input[str] encrypted_password: The encrypted password, base64 encoded.
        :param pulumi.Input[str] host: The source host of the user. Defaults to `localhost`.
        :param pulumi.Input[str] key_fingerprint: The fingerprint of the PGP key used to encrypt the password
        :param pulumi.Input[str] pgp_key: Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
        :param pulumi.Input[str] user: The IAM user to associate with this access key.
        """
        _UserPasswordState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            encrypted_password=encrypted_password,
            host=host,
            key_fingerprint=key_fingerprint,
            pgp_key=pgp_key,
            user=user,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             encrypted_password: Optional[pulumi.Input[str]] = None,
             host: Optional[pulumi.Input[str]] = None,
             key_fingerprint: Optional[pulumi.Input[str]] = None,
             pgp_key: Optional[pulumi.Input[str]] = None,
             user: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if encrypted_password is None and 'encryptedPassword' in kwargs:
            encrypted_password = kwargs['encryptedPassword']
        if key_fingerprint is None and 'keyFingerprint' in kwargs:
            key_fingerprint = kwargs['keyFingerprint']
        if pgp_key is None and 'pgpKey' in kwargs:
            pgp_key = kwargs['pgpKey']

        if encrypted_password is not None:
            _setter("encrypted_password", encrypted_password)
        if host is not None:
            _setter("host", host)
        if key_fingerprint is not None:
            _setter("key_fingerprint", key_fingerprint)
        if pgp_key is not None:
            _setter("pgp_key", pgp_key)
        if user is not None:
            _setter("user", user)

    @property
    @pulumi.getter(name="encryptedPassword")
    def encrypted_password(self) -> Optional[pulumi.Input[str]]:
        """
        The encrypted password, base64 encoded.
        """
        return pulumi.get(self, "encrypted_password")

    @encrypted_password.setter
    def encrypted_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encrypted_password", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        The source host of the user. Defaults to `localhost`.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> Optional[pulumi.Input[str]]:
        """
        The fingerprint of the PGP key used to encrypt the password
        """
        return pulumi.get(self, "key_fingerprint")

    @key_fingerprint.setter
    def key_fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_fingerprint", value)

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[str]]:
        """
        Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
        """
        return pulumi.get(self, "pgp_key")

    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pgp_key", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        The IAM user to associate with this access key.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


class UserPassword(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
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
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserPasswordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `UserPassword` resource sets and manages a password for a given
        user on a MySQL server.

        > **NOTE on MySQL Passwords:** This resource conflicts with the `password`
           argument for `User`. This resource uses PGP encryption to avoid
           storing unencrypted passwords in the provider state.

        > **NOTE on How Passwords are Created:** This resource **automatically**
           generates a **random** password. The password will be a random UUID.

        :param str resource_name: The name of the resource.
        :param UserPasswordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserPasswordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            UserPasswordArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserPasswordArgs.__new__(UserPasswordArgs)

            __props__.__dict__["host"] = host
            if pgp_key is None and not opts.urn:
                raise TypeError("Missing required property 'pgp_key'")
            __props__.__dict__["pgp_key"] = pgp_key
            if user is None and not opts.urn:
                raise TypeError("Missing required property 'user'")
            __props__.__dict__["user"] = user
            __props__.__dict__["encrypted_password"] = None
            __props__.__dict__["key_fingerprint"] = None
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

        __props__ = _UserPasswordState.__new__(_UserPasswordState)

        __props__.__dict__["encrypted_password"] = encrypted_password
        __props__.__dict__["host"] = host
        __props__.__dict__["key_fingerprint"] = key_fingerprint
        __props__.__dict__["pgp_key"] = pgp_key
        __props__.__dict__["user"] = user
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

