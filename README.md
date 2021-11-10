[![Actions Status](https://github.com/pulumi/pulumi-mysql/workflows/master/badge.svg)](https://github.com/pulumi/pulumi-mysql/actions)
[![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
[![NPM version](https://badge.fury.io/js/%40pulumi%2Fmysql.svg)](https://www.npmjs.com/package/@pulumi/mysql)
[![Python version](https://badge.fury.io/py/pulumi-mysql.svg)](https://pypi.org/project/pulumi-mysql)
[![NuGet version](https://badge.fury.io/nu/pulumi.mysql.svg)](https://badge.fury.io/nu/pulumi.mysql)
[![PkgGoDev](https://pkg.go.dev/badge/github.com/pulumi/pulumi-mysql/sdk/v3/go)](https://pkg.go.dev/github.com/pulumi/pulumi-mysql/sdk/v3/go)
[![License](https://img.shields.io/npm/l/%40pulumi%2Fpulumi.svg)](https://github.com/pulumi/pulumi-mysql/blob/master/LICENSE)

# MySQL Resource Provider

The MySQL resource provider for Pulumi lets you manage MySQL resources in your cloud programs.  To use
this package, please [install the Pulumi CLI first](https://pulumi.io/).

## Installing

This package is available in many languages in the standard packaging formats.

### Node.js (Java/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

    $ npm install @pulumi/mysql

or `yarn`:

    $ yarn add @pulumi/mysql

### Python

To use from Python, install using `pip`:

    $ pip install pulumi_mysql

### Go

To use from Go, use `go get` to grab the latest version of the library

    $ go get github.com/pulumi/pulumi-mysql/sdk/v3

### .NET

To use from .NET, install using `dotnet add package`:

    $ dotnet add package Pulumi.Mysql

## Configuration

The following configuration points are available:

- `mysql:endpoint` (required) - The address of the MySQL server to use. Most often a "hostname:port" pair, but may also
  be an absolute path to a Unix socket when the host OS is Unix-compatible. Can be set via `MYSQL_ENDPOINT` environment variable.
- `mysql:username` (required) - Username to use to authenticate with the server. Can be set via `MYSQL_USERNAME` environment variable.
- `mysql:password` - (optional) Password for the given user, if that user has a password. Can be set via `MYSQL_PASSWORD` environment variable.
- `mysql:tls` - (optional) The TLS configuration. One of false, true, or skip-verify. Defaults to `false`. Can be set via
  `MYSQL_TLS_CONFIG` environment variable.
- `mysql:proxy` - (Optional) Proxy socks url, can also be sourced from `ALL_PROXY` or `all_proxy` environment variables.

## Reference

For further information, please visit [the MySQL provider docs](https://www.pulumi.com/docs/intro/cloud-providers/mysql) or for detailed reference documentation, please visit [the API docs](https://www.pulumi.com/docs/reference/pkg/mysql).
