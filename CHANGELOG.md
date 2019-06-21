## HEAD (Unreleased)
___NULL___


## 0.18.3 (2019-06-21)
* Update to pulumi-terraform@3635bed3a5 which stops maps containing `.` being treated as nested maps.

## 0.18.2 (2019-06-17)
* Upgrade to v1.5.2 of the MySQL Terraform provider
* Add TypeScript type guards for each resource class

## 0.18.1 (2019-05-16)
* Improve support for explicit providers by not requiring package level configuration when default provider is not used. [#6](https://github.com/pulumi/pulumi-mysql/pull/6)

## 0.18.0 (2019-05-10)
* Initial release of `pulumi-mysql`, based on `v1.5.1` of the MySQL Terraform provider.
