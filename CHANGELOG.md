## HEAD (Unreleased)
* Add support for DotNet SDK Generation
* Update to v1.9.0 of the MySQL Terraform Provider

---

## 1.0.0 (2019-10-02)
* Regenerate SDK based on tf2pulumi 0.6.0
* Update to v1.8.0 of the MySQL Terraform Provider

## 0.18.11 (2019-09-05)
* Upgrade to Pulumi v1.0.0

## 0.18.10 (2019-08-29)
* Upgrade pulumi-terraform to 3f206601e7

## 0.18.9 (2019-08-20)
* Depend on latest pulumi package

## 0.18.8 (2019-08-09)
* Upgrade to pulumi-terraform@9db2fc93cd

## 0.18.7 (2019-08-08)
* Update to pulumi-terraform@013b95b1c8

## 0.18.6 (2019-07-24)
* Update to v1.7.0 of the MySQL Terraform Provider

## 0.18.5 (2019-07-09)
* Fix detailed diffs with nested computed values.

## 0.18.4 (2019-07-08)
* Communicate detailed information about the difference between a resource's desired and actual state during a Pulumi update

## 0.18.3 (2019-06-21)
* Update to pulumi-terraform@3635bed3a5 which stops maps containing `.` being treated as nested maps.

## 0.18.2 (2019-06-17)
* Upgrade to v1.5.2 of the MySQL Terraform provider
* Add TypeScript type guards for each resource class

## 0.18.1 (2019-05-16)
* Improve support for explicit providers by not requiring package level configuration when default provider is not used. [#6](https://github.com/pulumi/pulumi-mysql/pull/6)

## 0.18.0 (2019-05-10)
* Initial release of `pulumi-mysql`, based on `v1.5.1` of the MySQL Terraform provider.
