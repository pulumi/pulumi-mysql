// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mysql

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-mysql/sdk/v3/go/mysql/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The provider type for the mysql package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	AuthenticationPlugin pulumi.StringPtrOutput `pulumi:"authenticationPlugin"`
	Endpoint             pulumi.StringOutput    `pulumi:"endpoint"`
	Password             pulumi.StringPtrOutput `pulumi:"password"`
	Proxy                pulumi.StringPtrOutput `pulumi:"proxy"`
	Tls                  pulumi.StringPtrOutput `pulumi:"tls"`
	Username             pulumi.StringOutput    `pulumi:"username"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Endpoint == nil {
		return nil, errors.New("invalid value for required argument 'Endpoint'")
	}
	if args.Username == nil {
		return nil, errors.New("invalid value for required argument 'Username'")
	}
	if args.Proxy == nil {
		if d := internal.GetEnvOrDefault(nil, nil, "ALL_PROXY", "all_proxy"); d != nil {
			args.Proxy = pulumi.StringPtr(d.(string))
		}
	}
	if args.Tls == nil {
		if d := internal.GetEnvOrDefault("false", nil, "MYSQL_TLS_CONFIG"); d != nil {
			args.Tls = pulumi.StringPtr(d.(string))
		}
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:mysql", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	AuthenticationPlugin *string `pulumi:"authenticationPlugin"`
	Endpoint             string  `pulumi:"endpoint"`
	MaxConnLifetimeSec   *int    `pulumi:"maxConnLifetimeSec"`
	MaxOpenConns         *int    `pulumi:"maxOpenConns"`
	Password             *string `pulumi:"password"`
	Proxy                *string `pulumi:"proxy"`
	Tls                  *string `pulumi:"tls"`
	Username             string  `pulumi:"username"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	AuthenticationPlugin pulumi.StringPtrInput
	Endpoint             pulumi.StringInput
	MaxConnLifetimeSec   pulumi.IntPtrInput
	MaxOpenConns         pulumi.IntPtrInput
	Password             pulumi.StringPtrInput
	Proxy                pulumi.StringPtrInput
	Tls                  pulumi.StringPtrInput
	Username             pulumi.StringInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

func (o ProviderOutput) AuthenticationPlugin() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.AuthenticationPlugin }).(pulumi.StringPtrOutput)
}

func (o ProviderOutput) Endpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringOutput { return v.Endpoint }).(pulumi.StringOutput)
}

func (o ProviderOutput) Password() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Password }).(pulumi.StringPtrOutput)
}

func (o ProviderOutput) Proxy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Proxy }).(pulumi.StringPtrOutput)
}

func (o ProviderOutput) Tls() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Tls }).(pulumi.StringPtrOutput)
}

func (o ProviderOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringOutput { return v.Username }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}
