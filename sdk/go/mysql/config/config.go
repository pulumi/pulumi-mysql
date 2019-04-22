// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
	"github.com/pulumi/pulumi/sdk/go/pulumi/config"
)

func GetEndpoint(ctx *pulumi.Context) string {
	return config.Require(ctx, "mysql:endpoint")
}

func GetPassword(ctx *pulumi.Context) string {
	return config.Get(ctx, "mysql:password")
}

func GetTls(ctx *pulumi.Context) string {
	return config.Get(ctx, "mysql:tls")
}

func GetUsername(ctx *pulumi.Context) string {
	return config.Require(ctx, "mysql:username")
}
