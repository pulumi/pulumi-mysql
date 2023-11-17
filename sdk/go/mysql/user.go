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

// The “User“ resource creates and manages a user on a MySQL
// server.
//
// ## Examples
//
// ### Basic Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-mysql/sdk/v3/go/mysql"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := mysql.NewUser(ctx, "jdoe", &mysql.UserArgs{
//				Host:              pulumi.String("example.com"),
//				PlaintextPassword: pulumi.String("password"),
//				User:              pulumi.String("jdoe"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ### Example Usage with an Authentication Plugin
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-mysql/sdk/v3/go/mysql"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := mysql.NewUser(ctx, "nologin", &mysql.UserArgs{
//				AuthPlugin: pulumi.String("mysql_no_login"),
//				Host:       pulumi.String("example.com"),
//				User:       pulumi.String("nologin"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type User struct {
	pulumi.CustomResourceState

	// Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintextPassword`.
	AuthPlugin pulumi.StringPtrOutput `pulumi:"authPlugin"`
	// The source host of the user. Defaults to "localhost".
	Host pulumi.StringPtrOutput `pulumi:"host"`
	// Deprecated alias of `plaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `plaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `authPlugin`.
	//
	// Deprecated: Please use plaintext_password instead
	Password pulumi.StringPtrOutput `pulumi:"password"`
	// The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `authPlugin`.
	PlaintextPassword pulumi.StringPtrOutput `pulumi:"plaintextPassword"`
	// An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
	TlsOption pulumi.StringPtrOutput `pulumi:"tlsOption"`
	// The name of the user.
	User pulumi.StringOutput `pulumi:"user"`
}

// NewUser registers a new resource with the given unique name, arguments, and options.
func NewUser(ctx *pulumi.Context,
	name string, args *UserArgs, opts ...pulumi.ResourceOption) (*User, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.User == nil {
		return nil, errors.New("invalid value for required argument 'User'")
	}
	if args.Password != nil {
		args.Password = pulumi.ToSecret(args.Password).(pulumi.StringPtrInput)
	}
	if args.PlaintextPassword != nil {
		args.PlaintextPassword = pulumi.ToSecret(args.PlaintextPassword).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"password",
		"plaintextPassword",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource User
	err := ctx.RegisterResource("mysql:index/user:User", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUser gets an existing User resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUser(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserState, opts ...pulumi.ResourceOption) (*User, error) {
	var resource User
	err := ctx.ReadResource("mysql:index/user:User", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering User resources.
type userState struct {
	// Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintextPassword`.
	AuthPlugin *string `pulumi:"authPlugin"`
	// The source host of the user. Defaults to "localhost".
	Host *string `pulumi:"host"`
	// Deprecated alias of `plaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `plaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `authPlugin`.
	//
	// Deprecated: Please use plaintext_password instead
	Password *string `pulumi:"password"`
	// The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `authPlugin`.
	PlaintextPassword *string `pulumi:"plaintextPassword"`
	// An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
	TlsOption *string `pulumi:"tlsOption"`
	// The name of the user.
	User *string `pulumi:"user"`
}

type UserState struct {
	// Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintextPassword`.
	AuthPlugin pulumi.StringPtrInput
	// The source host of the user. Defaults to "localhost".
	Host pulumi.StringPtrInput
	// Deprecated alias of `plaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `plaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `authPlugin`.
	//
	// Deprecated: Please use plaintext_password instead
	Password pulumi.StringPtrInput
	// The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `authPlugin`.
	PlaintextPassword pulumi.StringPtrInput
	// An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
	TlsOption pulumi.StringPtrInput
	// The name of the user.
	User pulumi.StringPtrInput
}

func (UserState) ElementType() reflect.Type {
	return reflect.TypeOf((*userState)(nil)).Elem()
}

type userArgs struct {
	// Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintextPassword`.
	AuthPlugin *string `pulumi:"authPlugin"`
	// The source host of the user. Defaults to "localhost".
	Host *string `pulumi:"host"`
	// Deprecated alias of `plaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `plaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `authPlugin`.
	//
	// Deprecated: Please use plaintext_password instead
	Password *string `pulumi:"password"`
	// The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `authPlugin`.
	PlaintextPassword *string `pulumi:"plaintextPassword"`
	// An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
	TlsOption *string `pulumi:"tlsOption"`
	// The name of the user.
	User string `pulumi:"user"`
}

// The set of arguments for constructing a User resource.
type UserArgs struct {
	// Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintextPassword`.
	AuthPlugin pulumi.StringPtrInput
	// The source host of the user. Defaults to "localhost".
	Host pulumi.StringPtrInput
	// Deprecated alias of `plaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `plaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `authPlugin`.
	//
	// Deprecated: Please use plaintext_password instead
	Password pulumi.StringPtrInput
	// The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `authPlugin`.
	PlaintextPassword pulumi.StringPtrInput
	// An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
	TlsOption pulumi.StringPtrInput
	// The name of the user.
	User pulumi.StringInput
}

func (UserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userArgs)(nil)).Elem()
}

type UserInput interface {
	pulumi.Input

	ToUserOutput() UserOutput
	ToUserOutputWithContext(ctx context.Context) UserOutput
}

func (*User) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (i *User) ToUserOutput() UserOutput {
	return i.ToUserOutputWithContext(context.Background())
}

func (i *User) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserOutput)
}

// UserArrayInput is an input type that accepts UserArray and UserArrayOutput values.
// You can construct a concrete instance of `UserArrayInput` via:
//
//	UserArray{ UserArgs{...} }
type UserArrayInput interface {
	pulumi.Input

	ToUserArrayOutput() UserArrayOutput
	ToUserArrayOutputWithContext(context.Context) UserArrayOutput
}

type UserArray []UserInput

func (UserArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*User)(nil)).Elem()
}

func (i UserArray) ToUserArrayOutput() UserArrayOutput {
	return i.ToUserArrayOutputWithContext(context.Background())
}

func (i UserArray) ToUserArrayOutputWithContext(ctx context.Context) UserArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserArrayOutput)
}

// UserMapInput is an input type that accepts UserMap and UserMapOutput values.
// You can construct a concrete instance of `UserMapInput` via:
//
//	UserMap{ "key": UserArgs{...} }
type UserMapInput interface {
	pulumi.Input

	ToUserMapOutput() UserMapOutput
	ToUserMapOutputWithContext(context.Context) UserMapOutput
}

type UserMap map[string]UserInput

func (UserMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*User)(nil)).Elem()
}

func (i UserMap) ToUserMapOutput() UserMapOutput {
	return i.ToUserMapOutputWithContext(context.Background())
}

func (i UserMap) ToUserMapOutputWithContext(ctx context.Context) UserMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserMapOutput)
}

type UserOutput struct{ *pulumi.OutputState }

func (UserOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (o UserOutput) ToUserOutput() UserOutput {
	return o
}

func (o UserOutput) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return o
}

// Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintextPassword`.
func (o UserOutput) AuthPlugin() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *User) pulumi.StringPtrOutput { return v.AuthPlugin }).(pulumi.StringPtrOutput)
}

// The source host of the user. Defaults to "localhost".
func (o UserOutput) Host() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *User) pulumi.StringPtrOutput { return v.Host }).(pulumi.StringPtrOutput)
}

// Deprecated alias of `plaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `plaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `authPlugin`.
//
// Deprecated: Please use plaintext_password instead
func (o UserOutput) Password() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *User) pulumi.StringPtrOutput { return v.Password }).(pulumi.StringPtrOutput)
}

// The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `authPlugin`.
func (o UserOutput) PlaintextPassword() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *User) pulumi.StringPtrOutput { return v.PlaintextPassword }).(pulumi.StringPtrOutput)
}

// An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
func (o UserOutput) TlsOption() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *User) pulumi.StringPtrOutput { return v.TlsOption }).(pulumi.StringPtrOutput)
}

// The name of the user.
func (o UserOutput) User() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.User }).(pulumi.StringOutput)
}

type UserArrayOutput struct{ *pulumi.OutputState }

func (UserArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*User)(nil)).Elem()
}

func (o UserArrayOutput) ToUserArrayOutput() UserArrayOutput {
	return o
}

func (o UserArrayOutput) ToUserArrayOutputWithContext(ctx context.Context) UserArrayOutput {
	return o
}

func (o UserArrayOutput) Index(i pulumi.IntInput) UserOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *User {
		return vs[0].([]*User)[vs[1].(int)]
	}).(UserOutput)
}

type UserMapOutput struct{ *pulumi.OutputState }

func (UserMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*User)(nil)).Elem()
}

func (o UserMapOutput) ToUserMapOutput() UserMapOutput {
	return o
}

func (o UserMapOutput) ToUserMapOutputWithContext(ctx context.Context) UserMapOutput {
	return o
}

func (o UserMapOutput) MapIndex(k pulumi.StringInput) UserOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *User {
		return vs[0].(map[string]*User)[vs[1].(string)]
	}).(UserOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserInput)(nil)).Elem(), &User{})
	pulumi.RegisterInputType(reflect.TypeOf((*UserArrayInput)(nil)).Elem(), UserArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*UserMapInput)(nil)).Elem(), UserMap{})
	pulumi.RegisterOutputType(UserOutput{})
	pulumi.RegisterOutputType(UserArrayOutput{})
	pulumi.RegisterOutputType(UserMapOutput{})
}
