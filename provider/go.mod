module github.com/pulumi/pulumi-mysql/provider/v2

go 1.12

require (
	github.com/hashicorp/terraform-plugin-sdk v1.7.0
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.1.0
	github.com/pulumi/pulumi/sdk/v2 v2.0.1-0.20200424001829-090f390d7b1a
	github.com/terraform-providers/terraform-provider-mysql v1.9.0
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
