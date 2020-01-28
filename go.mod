module github.com/pulumi/pulumi-mysql

go 1.12

require (
	github.com/hashicorp/terraform-plugin-sdk v1.0.0
	github.com/pkg/errors v0.8.1
	github.com/pulumi/pulumi v1.6.0
	github.com/pulumi/pulumi-terraform-bridge v1.5.3-0.20200116214742-68c8f56da38a
	github.com/terraform-providers/terraform-provider-mysql v1.9.0
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
