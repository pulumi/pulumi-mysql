[![Build Status](https://travis-ci.com/pulumi/pulumi-mysql.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https://travis-ci.com/pulumi/pulumi-mysql)

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

    $ go get github.com/pulumi/pulumi-mysql/sdk/go/...

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

For detailed reference documentation, please visit [the API docs](https://pulumi.io/reference/pkg/nodejs/@pulumi/mysql/index.html).
