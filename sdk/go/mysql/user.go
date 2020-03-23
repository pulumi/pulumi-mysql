// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package mysql

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The ``.User`` resource creates and manages a user on a MySQL
// server.
//
// > **Note:** The password for the user is provided in plain text, and is
// obscured by an unsalted hash in the state
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
// Care is required when using this resource, to avoid disclosing the password.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/user.html.markdown.
type User struct {
	pulumi.CustomResourceState

	// Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintextPassword`.  
	AuthPlugin pulumi.StringPtrOutput `pulumi:"authPlugin"`
	// The source host of the user. Defaults to "localhost".
	Host pulumi.StringPtrOutput `pulumi:"host"`
	// Deprecated alias of `plaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `plaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `authPlugin`.
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
	if args == nil || args.User == nil {
		return nil, errors.New("missing required argument 'User'")
	}
	if args == nil {
		args = &UserArgs{}
	}
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

